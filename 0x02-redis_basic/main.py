#!/usr/bin/env python3
"""
Main file
"""
import redis

Cache = __import__('exercise1').Cache

cache = Cache()

data = b"hello"
key = cache.store(data)
print(key)

        
