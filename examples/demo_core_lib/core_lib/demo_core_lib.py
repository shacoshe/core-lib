import pysolr
from omegaconf import DictConfig
from sqlalchemy import create_engine

from core_lib.core_lib import CoreLib
from core_lib.data_layers.data.data_helpers import build_url

from core_lib.data_layers.data.session.db_data_session_factory import DBDataSessionFactory
from core_lib.data_layers.data.session.object_data_session_factory import ObjectDataSessionFactory
from examples.demo_core_lib.core_lib.data_layers.data_access.demo_data_access import DemoDataAccess
from examples.demo_core_lib.core_lib.data_layers.data_access.demo_search_data_access import DemoSearchDataAccess
from examples.demo_core_lib.core_lib.data_layers.service.demo_search_service import DemoSearchService
from examples.demo_core_lib.core_lib.data_layers.service.demo_service import DemoService


class DemoCoreLib(CoreLib):

    def __init__(self, conf: DictConfig):
        self.config = conf

        self.__engine = create_engine(build_url(**self.config.db), echo=self.config.db.log_queries)
        self.__engine.connect()

        db_data_session = DBDataSessionFactory(self.__engine)
        solr_data_session = ObjectDataSessionFactory(pysolr.Solr(build_url(**self.config.solr), always_commit=True))

        self.info = DemoService(DemoDataAccess(db_data_session))
        self.search = DemoSearchService(DemoSearchDataAccess(solr_data_session))


