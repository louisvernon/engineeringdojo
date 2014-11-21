import sys
import math

def newtan(x):
	return math.sin(x)/math.cos(x)

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print "Incorrect args"
		sys.exit()
	else:
		x = float(sys.argv[1])
		print newtan(x)
