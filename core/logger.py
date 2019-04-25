'''
Created on Feb 13, 2019

@author: mrane
'''
import logging
import os
from core.file_manager.file_manager import FileManager

_log = logging.getLogger('CORE')
_log.setLevel(logging.DEBUG)
try:
    fh = logging.FileHandler(os.path.join(FileManager.get_project_root(), "logs.log"))
    fh.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)s-%(filename)s-%(lineno)d-%(funcName)s: %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # add the handlers to the logger
    _log.addHandler(fh)
    _log.addHandler(ch)
except Exception as e:
    print(e)
LOG = _log