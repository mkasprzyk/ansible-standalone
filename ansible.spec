# -*- mode: python -*-
import os
import six
 
block_cipher = None

if six.__file__.endswith('pyc'):
    six_dependency = six.__file__[:-1]
else:
    six_dependency = six.__file__

a = Analysis(['ansible'],
             pathex=None,
             binaries=None,
             datas=[(six_dependency, '.')],
             hiddenimports=['ConfigParser', 'ansible.cli.adhoc'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='ansible',
          debug=False,
          strip=False,
          upx=True,
          console=True)
