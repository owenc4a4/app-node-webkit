print 12

import os
import sys



script_dir = os.path.dirname(__file__)

print script_dir

sys.path.insert(0, os.path.join(script_dir, 'd'))
import d


import p1
