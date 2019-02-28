'''
Created on Feb 13, 2019

@author: mrane
'''
import logging


log = logging.getLogger('CORE')
log.setLevel(logging.DEBUG)
fh = logging.FileHandler('test.log')
fh.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
formatter = logging.Formatter('%(name)s %(asctime)s %(filename)s L %(lineno)d %(funcName)s:  %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
log.addHandler(fh)
log.addHandler(ch)