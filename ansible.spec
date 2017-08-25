# -*- mode: python -*-
import os
import six
import ansible
from ansible import plugins
 
block_cipher = None

if six.__file__.endswith('pyc'):
    six_dependency = six.__file__[:-1]
else:
    six_dependency = six.__file__

a = Analysis(['ansible'],
             pathex=None,
             binaries=None,
             datas=[
               (six_dependency, '.'),
               (os.path.dirname(ansible.__file__), 'ansible'),
               (os.path.dirname(plugins.__file__), 'ansible/plugins')
             ],
             hiddenimports=[
              'ConfigParser',
              'ansible.cli.adhoc',
              'ansible.vars',
              'winrm',
              'ansible.plugins.cache.base',
              'ansible.plugins.action',
              'ansible.plugins.cache',
              'ansible.plugins.callback',
              'ansible.plugins.connection',
              'ansible.plugins.filter',
              'ansible.plugins.lookup',
              'ansible.plugins.shell',
              'ansible.plugins.strategy',
              'ansible.plugins.terminal',
              'ansible.plugins.test',
              'ansible.plugins.vars',
              'ansible.modules',
              'ansible.plugins.lookup',
              'ansible.plugins.callback.default',
              'ansible.module_utils.urls',
              'ansible.parsing.yaml.dumper',
              'ansible.utils.hashing',
              'ansible.utils.unicode',
              'crypt',
              'smtplib',
              'logging.handlers'
             ],
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
