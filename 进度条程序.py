#!/usr/bin/python3

import time,sys
for sum in range(50):

    sys.stdout.write('\r'+'['+"|"*sum+']'+'%s%%'%(sum+1))
    sys.stdout.flush()
    time.sleep(0.05)