# -*- coding: utf-8 -*-
import os

def get_name(dir_path):
    if dir_path[-1] == '/':
        dir_path = dir_path[:-1]
    return os.path.basename(dir_path)

def get_seasons()
    pass

def main(dir_path):
    name = get_name(dir_path)
