import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir)))

def method_for_cover():
    import time
    ctime = time.time()
    if ctime % 2 == 0:
        return "Hello Red"
    else:
        return "Hello Blue"

from coverage import Coverage
coverage = Coverage(config_file="/Users/shaoyuliang/xiaohongshu/code/gitlab/coveragepy/lab/.coveragerc")
coverage.start()
method_for_cover()
coverage.stop()
coverage.save()