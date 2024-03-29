import os
import yaml
from os.path import dirname, abspath
from core.logger import LOG


class Config(object):

    def __init__(self, filename=None):
        self.yml_dict = None
        if os.environ.get('AUTO_CONFIG', None):
            LOG.info("getting AUTO_CONFIG configuration file")
            self.filename = os.environ['AUTO_CONFIG']
        elif filename:
            LOG.info("using log file: " + filename)
            self.filename = filename
        else:
            self.filename = os.path.join(dirname(dirname(abspath(__file__))), "..", "config", "default.yml")
            LOG.info("using default config file: " + self.filename)
        self._load_config(self.filename)

    def _load_config(self, filename):
        config_yaml = open(filename, 'r')
        self.yml_dict = yaml.load(config_yaml, Loader=yaml.FullLoader)
        LOG.info("Succesfully Loaded config")
        config_yaml.close()

    def get(self, key, default=None):
        if "." in key:
            tmp = self.yml_dict
            keys = key.split(".")
            for k in keys:
                tmp = tmp[k]
            LOG.info("config returning {0}: {1}".format(key, tmp))
            return tmp
        else:
            return default


