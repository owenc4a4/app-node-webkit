#!/usr/bin/env python
import os
import sys

pwd_tmp = os.getcwd()
script_dir = os.path.dirname(__file__)
if sys.platform == 'cygwin':
  nw_dir = '/home/Administrator/node-webkit/content/nw/tools'
  nw_build_dir = '/home/Administrator/node-webkit/out/Release'

elif sys.platform == 'win32':
  nw_dir = 'E:\\cygwin\\home\\Administrator\\code\\node-webkit\\src\\content\\nw\\tools'
  nw_build_dir = 'E:\\cygwin\\home\\Administrator\\code\\node-webkit\\src\\out\\Release'
else:
  quit()

if sys.platform != 'cygwin':
  quit()

os.system('python ' + os.path.join(nw_dir, 'package_binaries.py'))

sys.path.insert(0, nw_dir)
import getnwisrelease
import getnwversion

nw_version = 'v' + getnwversion.nw_version
is_release = getnwisrelease.release

if is_release == 0:
  nw_version += getnwisrelease.postfix

binary_tar = 'node-webkit-' + nw_version + '-win-ia32.zip'
require_files = ['nw.exp', 'nw.lib', 'nw.pdb']
os.chdir(script_dir)

if not os.path.isdir('forupload'):
  os.mkdir('forupload')

os.chdir('forupload')

if not os.path.isdir(nw_version):
  os.mkdir(nw_version)

print 'copy files.'
import shutil
for file in require_files:
  shutil.copy(os.path.join(nw_build_dir, file),
              os.path.join(nw_version, file))

shutil.copy(os.path.join(nw_build_dir, 'node-webkit-binaries', binary_tar),
              os.path.join(nw_version, binary_tar))

os.system('scp -r %s owen-cloud@10.0.2.2:/home/owen-cloud/release'
          % (nw_version))

os.chdir(pwd_tmp)
