from src.collectors.registry import (
    CollectorRegistry
)


class CollectorFactory:

    @staticmethod
    def create(name):

        return CollectorRegistry.get(name)