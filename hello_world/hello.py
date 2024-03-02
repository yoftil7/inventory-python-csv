
import sys
from optparse import OptionParser



def main():


    usage = "\n%prog  [options]"
    parser = OptionParser(usage,version="%prog version___")
    parser.add_option("-n","--name",action="store",dest="name",help="name ") 


    (options,args) = parser.parse_args()
    for key in ([options.name]):
        if not (key):
            parser.print_help()
            sys.exit(0)

    try:
        print ("hello %s" % (options.name))
    except Exception as err:
        print (err)


if __name__ == '__main__':
    main()

