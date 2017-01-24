
===========
Coverage.py
===========

realtime code coverage collection for python base on redis

Coverage.py is forked from the `coveragepy <http://bitbucket.org/ned/coveragepy>`. The original version is based on the rewrite for the `settrace()` function.
It depends on quit the process if we need the result of collecting. We change the way how the coverage data is stored, migrate it from memeory dictionary to
redis, so that we can retrieve the collect result in realtime.


Getting Started
---------------


License
-------

Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0.