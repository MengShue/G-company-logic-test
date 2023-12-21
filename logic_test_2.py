#!/usr/bin/python
# -*- coding: utf-8 -*-

def calculate_distinction(string):
    string = string.upper()
    set_string = set(string)
    set_string.remove(' ')
    set_string = sorted(set_string)
    for item in set_string:
        print(item + " " + str(string.count(item)))

if __name__ == '__main__':
    print("python file is running directly")
    calculate_distinction("Hello welcome to Cathay 60th year anniversary")
