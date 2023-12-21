#!/usr/bin/python
# -*- coding: utf-8 -*-

def string_revert(list):
    ans = []
    for item in list:
        item = str(item)
        rev_str = item[::-1]
        ans.append(int(rev_str))
    return ans

if __name__ == '__main__':
    print("python file is running directly")
    print(string_revert([35, 46, 57, 91, 29]))
