""" implement own dict for data hook """


class RedisDict(dict):
    """
        store the data to the redis when new item setted
    """

    def __init__(self, covconfig=None, **kw):
        super(RedisDict, self).__init__(**kw)
        self.covconfig = covconfig
        self.tracename = None

    def __setitem__(self, key, item):
        if isinstance(item, self.__class__):
            item.tracename = key
            if not getattr(item, "covconfig", None):
                setattr(item, "covconfig", self.covconfig)
        else:
            pass
        super(RedisDict, self).__setitem__(key, item)

    def __getitem__(self, key):
        return super(RedisDict, self).__getitem__(key)

    def __repr__(self):
        return "<RedisDict> %s" % self.keys()

    __str__ = __repr__
