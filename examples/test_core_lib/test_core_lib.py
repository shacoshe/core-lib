import pysolr
from memcache import Client
from omegaconf import DictConfig
from sqlalchemy import create_engine

from core_lib.cache.cache import Cache
from core_lib.cache.cache_client_factory import CacheClientFactory
from core_lib.cache.cache_client_memcached import CacheClientMemcached
from core_lib.core_lib import CoreLib
from core_lib.data_layers.data.data_helpers import build_url
from core_lib.data_layers.data.db.base import Base
from core_lib.data_layers.data_access.sessions.db_data_session_factory import DBDataSessionFactory
from core_lib.data_layers.data_access.sessions.object_data_session import ObjectDataSession
from core_lib.data_layers.data_access.sessions.object_data_session_factory import ObjectDataSessionFactory
from core_lib.session.session_manager import SessionManager
from examples.objects_core_lib.data_layers.data_access.objects_data_access import ObjectsDataAccess
from examples.test_core_lib.data_layers.data_access.test1_data_access import Test1DataAccess
from examples.test_core_lib.data_layers.data_access.test2_data_access import Test2DataAccess
from examples.test_core_lib.data_layers.data_access.user_data_access import UserDataAccess
from examples.test_core_lib.data_layers.service.test1_service import Test1Service
from examples.test_core_lib.data_layers.service.test2_service import Test2Service
from examples.test_core_lib.data_layers.service.user_service import UserService


class TestCoreLib(CoreLib):

    def __init__(self, conf: DictConfig):
        self.config = conf

        SessionManager.init(self.config.app.secret)

        cache_client_memcached = CacheClientMemcached(Client([build_url(**self.config.memcached)]))
        cache_factory = CacheClientFactory()
        cache_factory.register("memcached", cache_client_memcached)
        Cache.set_cache_factory(cache_factory)

        self.__engine = create_engine(build_url(**self.config.db), echo=self.config.db.log_queries)
        self.__engine.connect()

        db_data_session = DBDataSessionFactory(self.__engine)
        solr_data_session_factory = ObjectDataSessionFactory(pysolr.Solr(build_url(**self.config.solr), always_commit=True))

        class Test(object):
            def __init__(self):
                self.test_1 = Test1Service(Test1DataAccess([db_data_session]))
                self.test_2 = Test2Service(Test2DataAccess([db_data_session, solr_data_session_factory]))

        self.test = Test()
        self.user = UserService(UserDataAccess([db_data_session]))

        if self.config.db.create_db:
            Base.metadata.create_all(self.__engine)
