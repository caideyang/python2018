#encoding:utf-8

import sys,time

for i in range(20):
    time.sleep(0.5)
    sys.stdout.write('#')
    sys.stdout.flush()
sys.stdout.write("【Done】")