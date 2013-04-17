import os


def ExtractZipWithPermissions(src, dst):
  """Extract all members from the archive to the `dst` directory.
     with  preserving the file permissions
  """
  import zipfile
  zip = zipfile.ZipFile(src, 'r')
  zip.extractall(dst)
  
  # build the destination pathname, replacing
  # forward slashes to platform specific separators.
  # Strip trailing path separator, unless it represents the root.
  if (dst[-1:] in (os.path.sep, os.path.altsep)
      and len(os.path.splitdrive(dst)[1]) > 1):
    dst = dst[:-1]
  
  members = zip.infolist()
  for member in members:
    targetpath = dst
    # don't include leading "/" from file name if present
    if member.filename[0] == '/':
      targetpath = os.path.join(targetpath, member.filename[1:])
    else:
      targetpath = os.path.join(targetpath, member.filename)
    
    targetpath = os.path.normpath(targetpath)
    if os.path.isfile(targetpath):
      mode = member.external_attr >> 16 & 0x1FF
      os.chmod(targetpath, mode)
  zip.close()