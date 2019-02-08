'''
Created on Jan 24, 2019

@author: mrane
'''
import os

root = None

class FileManager(object):
    '''
    File Manager 
    '''
    @staticmethod
    def create_folder_structure(folders_string):
        os.makedirs(folders_string)
    
    
    