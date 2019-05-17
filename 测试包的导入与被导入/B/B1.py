#!/usr/bin/env python
#-*- coding:utf8 -*-

import os,sys
Path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(Path)
sys.path.append(Path)
from A import *
ac()
a1=A_Class("张三")