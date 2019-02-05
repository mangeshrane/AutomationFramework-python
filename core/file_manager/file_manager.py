'''
Created on Jan 24, 2019

@author: mrane
'''
import os


root = None


class FileManager(object):
    '''
    classdocs
    '''
    
    def create_folder_structure(self, folders_string):
        os.makedirs(folders_string)
