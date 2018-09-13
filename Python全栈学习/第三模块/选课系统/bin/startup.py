#!/usr/bin/python3
#@Author:CaiDeyang
#@Time: 2018/9/11 22:38

import os
import sys

BaseDir = os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))
sys.path.append(BaseDir)
from core import main

if __name__ == "__main__":
    main.run()