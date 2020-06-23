# -*- coding: utf-8 -*-
"""
@Time   ： 2020/6/22 10:45 下午
@Author ： guos
@File   ：redis_config.py
@IDE    ：PyCharm

"""
import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=2, max_connections=10)
cache_redis = redis.Redis(connection_pool=pool)

