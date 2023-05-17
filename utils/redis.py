import redis
from django.conf import settings

class Redis:
    def __init__(self, redisUri):
        self.client = redis.Redis.from_url(redisUri, decode_responses=True)

    def setValue(self, key, value, expiry = None):
        if expiry:
            return self.client.set(key, value, ex = expiry)
        else:
            return self.client.set(key, value)

    def getValue(self, key):
        return self.client.get(key)

    def deleteValue(self, key):
        return self.client.delete(key)

RedisClient = Redis(settings.REDIS_URL)