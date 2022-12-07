import redis
import json
import cPickle
from django.conf import settings

class RedisCache:

    def __init__(self):
        self.init()

    def init(self):
        self.r = redis.Redis(host=settings.REDIS_HOST, socket_timeout=300, retry_on_timeout=True)

    def check_and_set(self, key, value, ex=None):
        try:
            return self.r.set(key, value, ex)
        except Exception as e:
            print "Check and set exception for ", key,  str(e)
            self.__init__()
            return None

    def check_and_setex(self, key, ex, value):
        return self.check_and_set(key, value, ex)

    def check_and_get(self, key):
        try:
            value = self.r.get(key)
        except Exception as e:
            print "Check and get exception ", str(e)
            value = None
        return value

    def delete(self, key):
        return self.r.delete(key)

    def delete_pattern(self, pattern):
        try:
            for key in self.r.keys(pattern):
                self.delete(key)
        except Exception as e:
            print "Check and get exception ", str(e)

    def save(self, key, value, ex=None):
        value = json.dumps(value)
        try:
            return self.check_and_set(key, value, ex)
        except Exception as e:
            print "Set key failed with exception : ", str(e)
            return None

    def increment(self, key, value=1):
        try:
            return self.r.incr(key, value)
        except Exception as e:
            print "Increment key failed with exception : ", str(e)
            return None

    def get(self, key):
        try:
            return json.loads(self.check_and_get(key))
        except Exception as e:
            #print str(e)
            return None

    def save_pickle(self, key, data, ex=None):
        pickled = cPickle.dumps(data)
        res = self.check_and_set(key, pickled, ex)
        return res

    def get_pickle(self, key):
        pickled = self.check_and_get(key)
        res = cPickle.loads(pickled) if pickled else None
        return res