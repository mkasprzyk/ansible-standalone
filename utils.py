#!/usr/bin/env python

from ansible import plugins as ansible_plugins
from glob import glob
import os


def get_ansible_plugins_modules():
  modules = []
  plugins = glob(os.path.join(os.path.dirname(ansible_plugins.__file__), '*'))
  for plugin_path in filter(os.path.isdir, plugins):
    for plugin_source_path in glob(os.path.join(plugin_path, '*.py')):
      plugin_module = plugin_source_path[:-3].split('/')[-4:]
      modules.append('.'.join(plugin_module))
  return modules
