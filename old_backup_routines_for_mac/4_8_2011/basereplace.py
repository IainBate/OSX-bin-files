#!/usr/bin/python

# basereplace.py 0.3 - Replace files with one extension with files that have the same base but another extension.
# Original verison written by Sitsofe Wheeler.
# This code is public domain - do with it as you wish!

import os, sys, shutil
from optparse import OptionParser

# Function to only print debugging output
def debugprint(output, verbose):
    if verbose:
        print >> sys.stderr, output

# Parse command line options
def getopts():
    usage = "usage: %prog [options] SRCDIR [DSTDIR]"
    parser = OptionParser(usage=usage)
    parser.add_option("-d", "--destination-extension", dest="dstextension",
            help="extension of files in destination directories [default: %default]", action="store", default=".avi")
    parser.add_option("-s", "--source-extension", dest="srcextension",
            help="extension of files to move [default: %default]", action="store", default=".mp4")
    parser.add_option("-n", "--dry-run",
            help="simulate but don't move/delete files", action="store_true")
    parser.add_option("-f", "--force", dest="force",
            help="overwrite files that already exist and use the first matching path if a file matches multiple destinations", action="store_true")
    parser.add_option("-v", "--verbose", dest="verbose", default=False,
            help="print debugging output", action="store_true", )

    (options, args) = parser.parse_args()
    if len(args) < 1 or len(args) > 2:
        parser.error("Need at least one input directory and optionally a destination directory.")
    
    options.srcdir = args[0]
    if len(args) == 1:
        options.dstdir = options.srcdir
    else:
        options.dstdir = args[1]

    return options

# Replaces the extension on filename with newextension. NB: newextension is expected to contain the extension seperator (e.g.
# ".mp4")
def replaceext(filename, newextension):
    (root, ext) = os.path.splitext(filename)
    return root + newextension

# Move files and delete unwanted files
def domove(movemapping, dryrun, newextension, verbose):
    for fromfile in movemapping:
        tofile = movemapping[fromfile]

        debugprint("mv %s %s" % (fromfile, tofile), verbose)
        if not(dryrun):
            shutil.move(fromfile, tofile)

        oldfile = replaceext(tofile, newextension)
        debugprint("rm %s" % (oldfile), verbose)
        if not(dryrun):
            os.remove(oldfile)

    print >> sys.stderr, "Processed %d file(s)." % len(movemapping)

# Return a list of file paths that end with extension. Works recursively.
def getfilesrecursive(srcdir, extension, verbose):
    paths = []
    for root, dirs, files in os.walk(srcdir):
        for name in files:
            paths += [os.path.join(root, name)]

    filepaths = filter(os.path.isfile, paths)
    debugprint("Unfiltered file paths: %s" % (filepaths), verbose)
    
    if extension:
        hasext = lambda path: path.endswith(extension)
        filepaths = filter(hasext, filepaths)

    debugprint("Keeping files ending with %s" % (extension), verbose)
    debugprint("Filtered file paths: %s" % (filepaths), verbose)

    return filepaths

# Creates a mapping of source file paths to destination file paths based on the locations of files with similar names
def makemapping(srcpaths, dstpaths, srcextension, dstextension, verbose):
    dstmap = {}
    for path in dstpaths:
        searchname = os.path.basename(path)
        if searchname in dstmap:
            dstmap[searchname] += [path]
        else:
            dstmap[searchname] = [path]
    
    unsafe = False
    srcdstmap = {}
    for path in srcpaths:
        debugprint("Checking if %s has a destination" % (path), verbose)
        srcname = os.path.basename(path)
        searchname = replaceext(srcname, dstextension)
        if searchname in dstmap:
            # Check whether a source file can map to multiple destinations
            if len(dstmap[searchname]) > 1:
                unsafe = True
                debugprint("%s matches multiple destinations %s" %
                        (path, dstmap[searchname]), verbose)
            
            dstdir = os.path.dirname(dstmap[searchname][0])
            dstfile = os.path.join(dstdir, srcname)

            if os.path.exists(dstfile):
                print >> sys.stderr, "Processing '%s' would create file '%s' which already exists. See --help on how to disable this check.\n" % (path, dstfile),
                unsafe = True
            srcdstmap[path] = dstfile

    debugprint("File move mapping: %s" % srcdstmap, verbose)
    result = {"unsafe": unsafe, "mapping": srcdstmap}
    return result

def main():
    options = getopts()
    debugprint("Source extension: '%s', destination/search extension: '%s'" %
            (options.srcextension, options.dstextension), options.verbose)

    # Get the files inside a directory that end with a particular extension
    srcpaths = getfilesrecursive(options.srcdir, options.srcextension, options.verbose)
    # Same as above but for candidate destination files
    dstpaths = getfilesrecursive(options.dstdir, options.dstextension, options.verbose)

    movemapping = makemapping(srcpaths, dstpaths, options.srcextension, options.dstextension, options.verbose)

    if movemapping["unsafe"] and not(options.force):
        print >> sys.stderr, "Forcing unsafe operation"
        return 1

    domove(movemapping["mapping"], options.dry_run, options.dstextension, options.verbose)

if __name__ == "__main__":
    main()
