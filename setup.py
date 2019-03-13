'''
Created on Mar 13, 2019

@author: mrane
'''

#!usr/bin/python
from setuptools import setup , find_packages

setup (
    name = 'Pyxer',
    description = 'An automation framework based on selenium and pytest',
    version = '0.1.0',
    packages=['config',
              'core.api',
              'core.browsers',
              'core.configuration',
              'core.data_providers',
              'core.decorators',
              'core.file_manager',
              'core.page',
              'core.reporter',
              'core.runner',
              'core.web'
              ],
    install_requires = ['pytest', 'pytest-html', 'pytest-forked', 'pytest-metadata','allure-pytest', 'xlrd', 'selenium', 'requests', 'pytest-xdist', 'pytest-json-report', 'PyYAML'],
    python_requires='>=2.7', # any python greater than 2.7
    entry_points = {
        'console_scripts': [
            'pyxer = core.runner.runner:main'
            ]
        }
    )