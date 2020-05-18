import os

import pymysql
from alembic import command
from alembic.config import Config
from alembic.script import ScriptDirectory
from omegaconf import DictConfig
from sqlalchemy import create_engine

from core_lib.data_layers.data.data_helpers import build_url


pymysql.install_as_MySQLdb()



class Alembic(object):

    def __init__(self, config: DictConfig):
        self.config = config.core_lib.alembic
        self.alembic_cfg = Config()

        self.config['sqlalchemy.url'] = build_url(**config.core_lib.data.sqlalchemy.url)

        self.__engine = create_engine(self.config['sqlalchemy.url'], echo=config.core_lib.data.sqlalchemy.log_queries)

        self.script_location = None
        if self.config.script_location:
            self.script_location = self.config.script_location if os.path.isabs(self.config.script_location) else os.path.join(os.getcwd(), self.config.script_location)
            self.script_location = os.path.normpath(self.script_location)

        if not self.script_location or not os.path.isdir(self.script_location):
            raise ValueError("config.alembic.script_location dose not exists `{}`".format(self.script_location))

        if not self.config.version_file_name:
            raise ValueError("config.alembic.version_file_name cannot be None")

        for key, value in self.config.items():
            if isinstance(value, str):
                self.alembic_cfg.set_main_option(key, value)
        # alembic_cfg.set_main_option("script_location", self.config.script_location)
        # alembic_cfg.set_main_option("version_table", self.config.version_table)

    def __migrate_to_revision(self, update_rev: str, migrate_up: bool = True):
        with self.__engine.begin() as connection:
            # self.config.attributes['connection'] = connection
            script = ScriptDirectory.from_config(self.alembic_cfg)

            def downgrade(rev, context):
                return script._downgrade_revs(update_rev, rev)

            def upgrade(rev, context):
                return script._upgrade_revs(update_rev, rev)

            fn = upgrade
            if not migrate_up:
                fn = downgrade

            from alembic.runtime.environment import EnvironmentContext
            with EnvironmentContext(self.alembic_cfg,
                                    script,
                                    fn=fn) as context:
                context.configure(version_table=self.config.version_table, connection=connection)
                with context.begin_transaction():
                    context.run_migrations()

    def upgrade(self, revision: str = "base"):
        self.__migrate_to_revision(revision, True)

    def downgrade(self, revision: str = "base"):
        self.__migrate_to_revision(revision, False)

    def create_migration(self, migration_name):
        if not migration_name:
            raise ValueError("Migration name must be set")

        version = self._read_version()
        new_version = version + 1
        command.revision(self.alembic_cfg, message=migration_name, rev_id=str(new_version))
        self._write_version(new_version)

    def _read_version(self):
        script = ScriptDirectory.from_config(self.alembic_cfg)
        count = 0
        for _ in script.walk_revisions():
            count = count + 1
        return count

    def _write_version(self, version):
        with open(os.path.join(self.script_location, self.config.version_file_name), 'w') as file:
            file.write(str(version))
