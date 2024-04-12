# 跨目录访问
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from config import *
from httpServer import *

if __name__ == "__main__":
    sh = Server(**httpServer)
    sh.run()