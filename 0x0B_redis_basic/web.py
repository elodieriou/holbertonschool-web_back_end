#!/usr/bin/env python3
""" Web cache and tracker """
import redis
import requests
from functools import wraps
from typing import Callable, Any

r = redis.Redis()


def tracker(method: Callable) -> Callable:
    """ Track and cache the result with an expiration time """
    @wraps(method)
    def wrapper(url) -> Any:
        """ Wrapper method """
        key = f'count:{url}'
        r.incr(key)
        cache = r.get(url)
        if cache:
            return cache.decode('utf-8')

        r.expire(key, 10)
        return method(url)

    return wrapper


@tracker
def get_page(url: str) -> str:
    """ Track how many times a particular URL was accessed """
    response = requests.get(url)
    return response.text
