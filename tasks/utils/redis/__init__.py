# -*- coding: utf-8 -*-
import redis

from tasks import config

# global redis pool connt 
# pool = redis.ConnectionPool.from_url(config.REDIS_URL)
# RedisPool = redis.Redis(connection_pool=pool)

class RedisConnt(redis.Redis):

    def __init__(self, **kwargs):
        return super(RedisConnt,self).__init__(**kwargs)

    def get(self, key, **kwargs):
        value = super(RedisConnt,self).get(key)
        return value if value else kwargs.get('default',value)

pool = redis.ConnectionPool.from_url(config.REDIS_URL)
redis_connt = RedisConnt(connection_pool=pool)