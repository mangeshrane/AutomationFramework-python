import os
import yaml

# import core.project_root
import core


class Config(object):

    def __init__(self, filename=None):
        self.yml_dict = None
        if os.environ.get('AUTO_CONFIG', None):
            self.filename = os.environ['AUTO_CONFIG']
        elif filename:
            self.filename = filename
        else:
            self.filename = os.path.join(core.project_root, "config", "default.yml")
        self._load_config(filename)

    def _load_config(self, filename):
        config_yaml = open(filename, 'r')
        self.yml_dict = yaml.load(config_yaml)
        print(self.yml_dict)
        config_yaml.close()

    def get(self, key):
        if "." in key:
            tmp = self.yml_dict
            keys = key.split(".")
            for k in keys:
                tmp = tmp[k]
            return tmp
        else:
            return None
