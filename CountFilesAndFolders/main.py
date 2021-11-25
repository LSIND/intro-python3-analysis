#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''py -3 main.py C:\\Users\\Admin\\Downloads\\intro-to-python3-analysis-master'''

import os
import sys

def main():
    userpath = ''
    if len(sys.argv)==2:
        userpath = sys.argv[1]
    else:
        print('input command parameter!, f.e. py -3 main.py C:\\Users\\Admin\\Downloads')

    if os.path.isdir(userpath): 
        for root, dirs, files in os.walk(userpath):
            path = root.split(os.sep)

            count_dirs = count_files = 0
            for f in dirs:
                count_dirs += 1

            for file in files:
                count_files += 1
            print((len(path) - 2) * '--'+'>', os.path.basename(root), ':\t', count_dirs, 'folders, ', count_files, 'files')
    else:
        print('{} is not a folder or it doesnt exist. input correct folder!'.format(userpath))

main()
