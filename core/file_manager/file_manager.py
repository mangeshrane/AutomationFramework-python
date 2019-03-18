'''
Created on Jan 24, 2019

'''
import os
import re


class FileManager(object):
    '''
    File Manager 
    '''
    __rootdir__ = None
    
    @staticmethod
    def create_folder_structure(folders_string):
        os.makedirs(folders_string)
        
        
    @classmethod
    def get_project_root(cls):
        if(cls.__rootdir__ != None):
            return cls.__rootdir__

        path = os.getcwd()
        seperator_matches = re.finditer("/|\\\\", path)

        paths_to_search = [path]
        for match in seperator_matches:
            p = path[:match.start()]
            paths_to_search.insert(0, p)

        for path in paths_to_search:
            target_path = os.path.join(path, ".rootfile")
            if os.path.isfile(target_path):
                cls.__root_folder__ = path
                return cls.__root_folder__
