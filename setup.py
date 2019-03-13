'''
Created on Mar 13, 2019

@author: mrane
'''

#!usr/bin/python
from distutils.core import setup

setup (
    name = 'Pyxer',
    description = 'An automation framework based on selenium and pytest',
    version = '0.1.0',
    packages=['pyxer',
              'pyxer.core',
              'pyxer.core.api',
              'pyxer.core.browsers',
              'pyxer.core.configuration',
              'pyxer.core.data_providers',
              'pyxer.core.decorators',
              'pyxer.core.file_manager',
              'pyxer.core.page',
              'pyxer.core.reporter',
              'pyxer.core.web'
              ],
    install_requires = ['pytest', 'pytest-html', 'pytest-forked', 'pytest-metadata','allure-pytest', 'xlrd', 'selenium', 'requests', 'pytest-xdist', 'pytest-json-report', 'PyYAML'],
    python_requires='>=2.7', # any python greater than 2.7
    entry_points = {
        'console_scripts': [
            'pyxer = pyxer.core.runner:main'
            ]
        }
    )