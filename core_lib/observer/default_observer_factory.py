from core_lib.factory.default_factory import DefaultFactory
from core_lib.observer.observer import Observer


class DefaultObserverFactory(DefaultFactory):

    def __init__(self):
        DefaultFactory.__init__(self, Observer)
