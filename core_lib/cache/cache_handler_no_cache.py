import datetime

from core_lib.cache.cache_handler import CacheHandler


class CacheHandlerNoCache(CacheHandler):

    def __init__(self):
        self.cached_function_responses = {}

    def from_cache(self, key):
        return None

    def to_cache(self, key: str, value, expire: datetime.timedelta):
        pass

    def invalidate_cache(self, key: str):
        pass