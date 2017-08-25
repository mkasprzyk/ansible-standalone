# -*- mode: python -*-
from ansible import plugins
from ansible import playbook
import ansible
import sys
import six
import os

sys.path.append(os.path.join(os.getcwd()))
from utils import get_ansible_plugins_modules

block_cipher = None

if six.__file__.endswith('pyc'):
    six_dependency = six.__file__[:-1]
else:
    six_dependency = six.__file__

plugin_modules = get_ansible_plugins_modules()

a = Analysis(['ansible-playbook'],
             pathex=None,
             binaries=None,
             datas=[
               (six_dependency, '.'),
               (os.path.dirname(ansible.__file__), 'ansible'),
               (os.path.dirname(plugins.__file__), 'ansible/plugins'),
               (os.path.dirname(playbook.__file__), 'ansible/playbook')
             ],
             hiddenimports=[
              'ansible.parsing.yaml.dumper',
              'ansible.module_utils.urls',
              'ansible.compat.selectors',
              'ansible.utils.hashing',
              'ansible.utils.unicode',
              'ansible.cli.playbook',
              'ansible.cli.adhoc',
              'ansible.playbook',
              'logging.handlers',
              'ansible.modules',
              'ansible.vars',
              'ConfigParser',
              'smtplib',
              'winrm',
              'site',
              'yaml',
              'crypt',
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
          name='ansible-playbook',
          debug=False,
          strip=False,
          upx=True,
          console=True)
