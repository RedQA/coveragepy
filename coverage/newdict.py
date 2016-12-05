""" implement own dict for data hook """


class RedisDict(dict):
    """
        store the data to the redis when new item setted
    """

    def __init__(self):
        super(RedisDict, self).__init__()

    def __setitem__(self, key, item):
        print "111" , key, item

    def __getitem__(self, key):
        print "adsfasdf"
        return self.__dict__[key]
