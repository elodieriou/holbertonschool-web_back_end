#!/usr/bin/env python3
""" Redis module """
import redis
import uuid
from typing import Union, Optional, Callable


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

    def get(self, key: str, fn: Optional[Callable]) -> Union[str, bytes, int, float]:
        """ Get data and convert it the desired format """
        if fn is None:
            return self._redis.get(key)
        else:
            data = self._redis.get(key)
            return fn(data)

    def get_str(self, data: str) -> str:
        """ Get data and convert it to str """
        return data.decode("utf-8")

    def get_int(self, data: str) -> int:
        """ Get data and convert it to int """
        try:
            data = int(data.decode("utf-8"))
        except Exception:
            data = 0
        return data
