# _*_ coding: utf-8 _*_
__author__ = 'cheng'


import redis
from srvframe.database import Connection

#redis db on localhost
token_redis = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
