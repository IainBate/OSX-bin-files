#!/usr/bin/python
 
import argparse
import sys
import os, time
 
def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("inputfile",
                        help="The file from which the timestamps will be copied.")
    parser.add_argument("target",
                        help="The target file or directory.")
    args = parser.parse_args()
 
    inputfile = args.inputfile
    target = args.target
     
    def visit(arg, dirname, names):
        for file_name in names:
            path = dirname + "/" + file_name
            os.utime(path ,(atime,mtime))
        return
     
    (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime)=(0,0,0,0,0,0,0,0,0,0)
 
    if os.path.exists(inputfile):
          (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(inputfile)
    else:
        print "{} does not exist.".format(inputfile)
        return
 
    if os.path.exists(target):
        if os.path.isdir(target):
            os.path.walk(target, visit, target)
        else:  #file
            os.utime(target,(atime,mtime))
                 
    else:
        print "{} does not exist.".format(target)
        return
     
     
 
if __name__ == "__main__":
    main(sys.argv[1:])
