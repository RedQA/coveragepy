""" implement own dict for data hook """

import os
import redis

DB_CONN = None


def redis_db(redis_host, redis_port, redis_db):
    global DB_CONN
    if not DB_CONN:
        DB_CONN = redis.StrictRedis(
            host=redis_host, port=redis_port, db=redis_db)
    return DB_CONN


class RedisDict(dict):
    """
        store the data to the redis when new item setted
    """

    def __init__(self, covconfig=None, **kw):
        super(RedisDict, self).__init__(**kw)
        self.__inited = False
        self.covconfig = covconfig

        if self.covconfig:
            self.init_redis()
        self.__tracename = None

    @property
    def tracename(self):
        return self.__tracename

    @tracename.setter
    def tracename(self, tracename):
        if not self.covconfig.xhs_project_root.endswith(os.path.sep):
            self.covconfig.xhs_project_root = self.covconfig.xhs_project_root + os.path.sep

        root_find = tracename.find(self.covconfig.xhs_project_root)
        if not root_find == -1:
            self.__tracename = tracename[
                len(self.covconfig.xhs_project_root):]
        else:
            self.__tracename = tracename

    def init_redis(self):
        if not self.__inited:
            self.db = redis_db(redis_host=self.covconfig.xhs_redis_host,
                               redis_port=self.covconfig.xhs_redis_port,
                               redis_db=self.covconfig.xhs_redis_db)
            self.pipeline = self.db.pipeline(transaction=False)
            self.__inited = True

            # set the project_root
            if self.covconfig.xhs_project_root.endswith(os.path.sep):
                self.project_root = self.covconfig.xhs_project_root
            else:
                self.project_root = self.covconfig.xhs_project_root + os.path.sep

    def __setitem__(self, key, item):
        if isinstance(item, self.__class__):
            if not getattr(item, "covconfig", None) and self.covconfig:
                setattr(item, "covconfig", self.covconfig)
                item.init_redis()
                item.tracename = key
        else:
            print self.tracename
            self.pipeline.sadd(self.tracename, key)
        super(RedisDict, self).__setitem__(key, item)

    def __getitem__(self, key):
        return super(RedisDict, self).__getitem__(key)

    def __repr__(self):
        return "<RedisDict> %s" % self.keys()

    def flush_pipe(self):
        """
            flush the pipeline to the redis
        """
        return self.pipeline.execute()

    __str__ = __repr__
