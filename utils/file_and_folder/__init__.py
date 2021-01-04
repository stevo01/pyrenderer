#!/usr/bin/python3
# encoding: utf-8

import os

'''
remove file if exists
'''
def remove_file(filename):
    if os.path.exists(filename):
        os.remove(filename)

'''
create directory if not exists
'''
def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)