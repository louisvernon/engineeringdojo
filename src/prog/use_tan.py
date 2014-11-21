import sys
sys.path.append("/Users/vernon/usr/lib")
import libmym


if __name__ == "__main__":
        if len(sys.argv) != 2:
                print "Incorrect args"
                sys.exit()
        else:
                x = float(sys.argv[1])
                print libmym.newtan(x)
