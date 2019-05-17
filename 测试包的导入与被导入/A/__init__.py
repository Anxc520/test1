#!/usr/bin/env python
#-*- coding:utf8 -*-
def ac():
    print("__init()__导入包成功！")
import os,sys
Path=os.path.dirname(os.path.abspath(__file__))
sys.path.append(Path)
from A1 import *