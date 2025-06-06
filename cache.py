import redis

class Cache:
    def __init__(self):
        self.client = None

    def init_app(self, app):
        self.client = redis.Redis(host="redis", port=6379, decode_responses=True)

    def incr(self, key):
        if self.client:
            return self.client.incr(key)
        raise RuntimeError("Redis client not initialized")

# Singleton instance
cache = Cache()
