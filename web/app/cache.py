class CacheDefinition:
    def push(self, key, value):
        """ Set value on cache """
        pass

    def peak(self, key):
        """ Retrieve and delete value from cache """
        pass

    def isConnected(self):
        """ Should return if it's okay to run """
        pass

    def name(self):
        """ Return the name of the cache instance """
        pass

    def exists(self, key):
        """ Return if the value exists for that key """
        pass


class RedisCacheManager(CacheDefinition):

    def __init__(self, rcache):
        self.redisCache = rcache

    def push(self, key, value):
        self.redisCache.set(key, value)

    def peak(self, key):
        m = self.redisCache.get(key)
        self.redisCache.delete(key)
        return m

    def isConnected(self):
        return self.redisCache is not None and self.redisCache.ping()

    def name(self):
        return "REDIS"

    def exists(self, key):
        if self.redisCache.get(key) is not None:
            return True
        return False


class SessionCacheManager(CacheDefinition):
    def __init__(self, s):
        self.sessionCache = s

    def push(self, key, value):
        self.sessionCache[key] = value

    def peak(self, key):
        m = self.sessionCache[key]
        self.sessionCache.pop(key, None)
        return m

    def isConnected(self):
        return self.sessionCache is not None

    def name(self):
        return "FLASK_SESSION"
    
    def exists(self, key):
        if self.sessionCache[key] is not None:
            return True
        return False


class CacheFacade(CacheDefinition):

    def __init__(self, sessionCache, rcache):
        redisCache = RedisCacheManager(rcache)

        self.currentCacheManager: CacheDefinition = None
        if redisCache.isConnected():
            self.currentCacheManager = redisCache
        else:
            self.currentCacheManager = SessionCacheManager(sessionCache)

    def push(self, key, value):
        self.currentCacheManager.push(key, value)

    def peak(self, key):
        return self.currentCacheManager.peak(key)

    def isConnected(self):
        return self.currentCacheManager.isConnected()

    def name(self):
        return self.currentCacheManager.name()

    def exists(self, key):
        return self.currentCacheManager.exists(key)

