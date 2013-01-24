#!/usr/bin/env python
import os


pwd_tmp = os.getcwd()
script_dir = os.path.dirname(__file__)

os.chdir(script_dir)

os.mkdir('forupload')









os.chdir(pwd_tmp)