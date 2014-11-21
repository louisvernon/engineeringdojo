import sys
sys.path.append("/Users/vernon/usr/lib")
import libmym
import math

# test tan func
print round(libmym.newtan(12312), 3) == round(math.tan(12312), 3)

