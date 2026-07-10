#!/usr/bin/env python
import os, os.path, argparse, datetime, shutil

def copy_year_leaf_folders(year, root, target, dry_run=False):
    if not os.path.exists(root):
        raise ValueError('Source directory %s does not exist' % root)
    if not os.path.exists(target):
        os.mkdir(target)
    leaf_folders = [dirname for dirname, subdirs, _ in os.walk(root) if len(subdirs) == 0]
    copy_folders = [dirname for dirname in leaf_folders if datetime.datetime.fromtimestamp(os.stat(dirname).st_birthtime).year == year]
    for copy_folder in copy_folders:
        target_folder = os.path.join(target, os.path.split(copy_folder)[1])
        target_folder_template = '%s_%%s' % target_folder
        count = 0
        while os.path.exists(target_folder):
            target_folder = target_folder_template % count
            count += 1
        print('copying %s to %s' % (copy_folder, target_folder))
        if not dry_run:
            shutil.copytree(copy_folder, target_folder)
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-y', '--year', type=int, default=datetime.datetime.now().year,
                        help='Year to copy folders from default=current year')
    parser.add_argument('source', type=str, help="Source directory to copy directories from")
    parser.add_argument('target', type=str, help="Target directory to copy directories to")
    parser.add_argument('--dry-run', type=bool, default=False,
                        help="Don't do any actual operations")
    args = parser.parse_args()
    copy_year_leaf_folders(args.year, args.source, args.target, args.dry_run)