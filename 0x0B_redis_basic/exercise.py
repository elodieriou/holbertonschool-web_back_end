#!/usr/bin/env python3
""" Redis module """
import redis
import uuid
from typing import Union


class Cache:
    """ Writing strings to Redis """

    def __init__(self) -> None:
        """ Create redis instance """

        # Create an instance Redis using 'localhost' and port 6379 by default
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Generate a random key, store it in Redis and return the key """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
