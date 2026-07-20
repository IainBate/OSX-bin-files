#!/usr/bin/env python 
import shutil
import os, os.path
import sys

input_dir = sys.argv[1]
output_dir = sys.argv[2]

valid_directories = []
delete_directories = []

for dirpath, dirnames, filenames in os.walk(input_dir):
    valid_directories.extend([os.path.relpath(os.path.join(dirpath, dirname), input_dir) for dirname in dirnames])
    
for dirpath, dirnames, filenames in os.walk(output_dir):
    rel_directories = [os.path.relpath(os.path.join(dirpath, dirname), output_dir) for dirname in dirnames]
    delete_directories.extend([x for x in rel_directories if x not in valid_directories])

delete_directories = [x for x in delete_directories if not x.startswith('.')]

for delete_directory in delete_directories:
    print("will delete %s" % os.path.join(output_dir, delete_directory))
    #shutil.rmtree(os.path.join(output_dir, delete_directory), ignore_errors=True)