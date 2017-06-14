#! /usr/bin/env python
# -*- coding: utf-8 -*-
# S.D.G

# Imports
from setuptools import setup, find_packages
from turkmarker.__init__ import __version__ as ver

__author__ = 'Ben Johnston'
__revision__ = '0.1'
__date__ = '09-Jun-2017 15:51:52 AEST'
__license__ = 'BSD 3-Clause'

setup(
    name='turkmarker',
    description='',
    url='',
    author='',
    author_email='',
    version=ver,
    packages=find_packages(),
    package_data = {
        'turkmarker': ['data/*',
                       'data/static/*'],
    },
    entry_points = {
        'console_scripts': [
            'turk-admin = turkmarker.manage:_main',
        ]
    },
    license=open('LICENSE.md').read(),
    long_description=open('README.md').read())
