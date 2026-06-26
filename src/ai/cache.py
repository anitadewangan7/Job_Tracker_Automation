import hashlib


class AICache:

    _cache = {}

    @classmethod
    def get(cls, key):

        return cls._cache.get(key)

    @classmethod
    def set(
        cls,
        key,
        value
    ):

        cls._cache[key] = value

    @staticmethod
    def hash_text(text):

        return hashlib.md5(
            text.encode()
        ).hexdigest()