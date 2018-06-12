#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 andy <andy@AndyDen>
#
# Distributed under terms of the MIT license.

"""
该脚本将yaml文件转换成properties文件
"""
import yaml
import sys
import os


def print_value(dict_values,prefix=None):
    for key in sorted(dict_values):
        value = dict_values[key]
        if isinstance(value,dict):
            if prefix is None:
                print_value(value,key)
            else:
                new_prefix=prefix+"."+key
                print_value(value,new_prefix)
        else:
            if prefix is None:
               print("%s = %s"%(key,value))
            else:
                print("%s.%s = %s"%(prefix,key,value))


def change_yaml(file_name):
    """
    将yaml文件中内容以properties形式打印出来
    """
    f = open(file_name,'r')
    dd = yaml.load(f.read())
    print_value(dd)

def main():
   argv_length = len(sys.argv)
   if argv_length<2:
       print("must input the yaml file name")
       raise SystemError("input the yaml name")
   else:
       file_name = sys.argv[1]
       change_yaml(file_name)

if __name__=='__main__':
    main()
