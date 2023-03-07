#!/usr/bin/env python3
""" Redis module """
import redis
import uuid
from typing import Union, Optional, Callable, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ Count how many times methods of the Cache class are called"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """ Wrapper method """
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """ Store history of inputs and outputs into list """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """ Wrapper method """
        input = str(args)
        self._redis.rpush(key + ':inputs', input)

        output = str(method(self, *args, **kwargs))
        self._redis.rpush(key + ':outputs', output)

        return output

    return wrapper


class Cache:
    """ Writing strings to Redis """

    def __init__(self) -> None:
        """ Create redis instance """

        # Create an instance Redis using 'localhost' and port 6379 by default
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Generate a random key, store it in Redis and return the key """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """ Get data and convert it the desired format """
        data = self._redis.get(key)
        if not data:
            return None

        if fn is None:
            return self._redis.get(key)
        else:
            data = self._redis.get(key)
            return fn(data)

    def get_str(self, data: str) -> str:
        """Convert data to str """
        return data.decode("utf-8")

    def get_int(self, data: str) -> int:
        """ Convert data to int """
        try:
            data = int(data.decode("utf-8"))
        except Exception:
            data = 0
        return data
