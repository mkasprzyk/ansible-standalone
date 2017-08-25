# -*- mode: python -*-
from ansible import plugins
import ansible
import six
import sys
import os

sys.path.append(os.path.join(os.getcwd()))
from utils import get_ansible_plugins_modules
 
block_cipher = None

if six.__file__.endswith('pyc'):
    six_dependency = six.__file__[:-1]
else:
    six_dependency = six.__file__

plugin_modules = get_ansible_plugins_modules()

a = Analysis(['ansible'],
             pathex=None,
             binaries=None,
             datas=[
               (six_dependency, '.'),
               (os.path.dirname(ansible.__file__), 'ansible'),
               (os.path.dirname(plugins.__file__), 'ansible/plugins')
             ],
             hiddenimports=[
              'ansible.plugins.callback.default',
              'ansible.parsing.yaml.dumper',
              'ansible.module_utils.urls',
              'ansible.plugins.lookup',
              'ansible.utils.hashing',
              'ansible.utils.unicode',
              'ansible.cli.adhoc',
              'logging.handlers'
              'ansible.modules',
              'ansible.vars',
              'ConfigParser',
              'smtplib',
              'crypt',
              'winrm',
             ] + plugin_modules,
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
