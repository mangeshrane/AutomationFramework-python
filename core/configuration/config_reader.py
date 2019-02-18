import os
import yaml

# import core.project_root


class Config(object):

    def __init__(self, filename=None):
        self.yml_dict = None
        if os.environ.get('AUTO_CONFIG', None):
            self.filename = os.environ['AUTO_CONFIG']
        elif filename:
            self.filename = filename
        else:
            self.filename = os.path.join(r'D:\Workspace\AutomationProject', "config", "default.yml")
        self._load_config(self.filename)

    def _load_config(self, filename):
        config_yaml = open(filename, 'r')
        self.yml_dict = yaml.load(config_yaml)
        config_yaml.close()

    def get(self, key, default=None):
        if "." in key:
            tmp = self.yml_dict
            keys = key.split(".")
            for k in keys:
                tmp = tmp[k]
            return tmp
        else:
            return default
