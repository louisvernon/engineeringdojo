#!/usr/bin/env python 
import sys
sys.path.append("/Users/vernon/usr/lib")
import libmym
import math

# test tan func
if(round(libmym.newtan(12312), 3) == round(math.tan(12312), 3)): sys.exit(0)
else: sys.exit(1)

