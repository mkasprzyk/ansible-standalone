# -*- mode: python -*-
import os
import six
import ansible
from ansible import plugins
from ansible import playbook

block_cipher = None

if six.__file__.endswith('pyc'):
    six_dependency = six.__file__[:-1]
else:
    six_dependency = six.__file__

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
              'ConfigParser',
              'ansible.cli.adhoc',
              'ansible.cli.playbook',
              'ansible.vars',
              'winrm',
              'ansible.playbook',
              'ansible.plugins.cache.base',
              'ansible.plugins.action',
              'ansible.plugins.action.copy',
              'ansible.plugins.cache',
              'ansible.plugins.callback',
              'ansible.plugins.connection',
              'ansible.plugins.filter',
              'ansible.plugins.lookup',
              'ansible.plugins.shell',
              'ansible.plugins.shell.sh',
              'ansible.plugins.strategy',
              'ansible.plugins.terminal',
              'ansible.plugins.test',
              'ansible.plugins.vars',
              'ansible.compat.selectors',
              'ansible.modules',
              'ansible.plugins.lookup',
              'ansible.plugins.callback.default',
              'ansible.module_utils.urls',
              'ansible.parsing.yaml.dumper',
              'ansible.utils.hashing',
              'ansible.utils.unicode',
              'yaml',
              'crypt',
              'smtplib',
              'logging.handlers',
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
          name='ansible-playbook',
          debug=False,
          strip=False,
          upx=True,
          console=True)
