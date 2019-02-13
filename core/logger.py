'''
Created on Feb 13, 2019

@author: mrane
'''
import logging

log = logging.Logger("FRAMEWORK")
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler().setFormatter(logging.Formatter("%(name)s - %(levelname)s - %(asctime)s - %(message)s")))