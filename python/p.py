import os
import sys



if sys.platform == 'win32':
  print 'win32'
  os.system('copy /b nw.exe+app.nw app-win.exe')
  
if sys.platform == 'cygwin':
  print 'cygwin'
  os.system('cat nw.exe app.nw > app-c.exe')