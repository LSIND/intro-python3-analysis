#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''py -3 main.py C:\\Users\\Admin\\Downloads\\intro-to-python3-analysis-master .jpg'''

import os
import sys

def count_files(userpath, ext = None):
    '''Count files and folders in folders and subfolders if there is no ext parameter
    If user pass and ext parameter - count files with specified extension (.jpg, .txt etc) in each subfolder''' 

    if os.path.isdir(userpath):
        if (ext is not None):
            print(f'Searching files with specified extension {ext}...')
            
            for root, dirs, files in os.walk(userpath):
                count_files = 0   
                for filename in files:
                    if filename.endswith(ext):
                        #print(os.path.join(root, filename))  # full file name
                        count_files += 1
                if count_files > 0:          
                    print(f'{(len(root.split(os.sep))-2)* "-"}> {root} -> {count_files} {ext} files')
        else:
            print(f'Count all files...')
            for root, dirs, files in os.walk(userpath):
                path = root.split(os.sep)
                count_dirs = count_files = 0
                for f in dirs:
                    count_dirs += 1
                    
                for filename in files:
                    count_files += 1
                if count_files < 60:
                    print(f'{(len(path) - 2) * "--"}> {os.path.basename(root)} \t {count_dirs} folders, {count_files} files')
    else:
        print(f'{userpath} is not a folder or it doesnt exist. Input correct folder!')

if __name__ == '__main__':
    userpath = ''
    file_ext = None # insert file extension if necessary
    if len(sys.argv)>=2:
        userpath = sys.argv[1]
        if len(sys.argv)==3:
            file_ext = sys.argv[2]
        count_files(userpath, file_ext)
    else:
        print('input command parameter!, f.e. py -3 main.py C:\\Users\\Admin\\Downloads or user/downloads/data')