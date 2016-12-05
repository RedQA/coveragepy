import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir)))

def method_for_cover():
    import time
    ctime = time.time()
    if ctime % 2 == 0:
        print "Hello Red"
    else:
        print "Hello Blue"

from coverage import Coverage
coverage = Coverage()
coverage.start()
method_for_cover()
coverage.stop()
coverage.save()