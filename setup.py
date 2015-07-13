#!/usr/bin/env python
from setuptools import setup

INSTALL_REQUIRES = [
    "suds-jurko >= 0.6",
]

setup(
    name='turbosmsua3',
    version='0.1dev',
    packages=['turbosmsua3',],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md').read(),

    install_requires = INSTALL_REQUIRES,
)

from distutils.core import setup

setup(
  name = 'turbosmsua',
  packages = ['turbosmsua3'], # this must be the same as the name above
  version = '0.1',
  description = 'Client for https://turbosms.ua',
  author = 'Serbokryl Oleg',
  author_email = 'chezar1995@gmail.com',
  url = 'https://github.com/Krokop/turbosmsua3', # use the URL to the github repo
  download_url = 'https://github.com/peterldowns/mypackage/tarball/0.1', # I'll explain this in a second
  keywords = ['testing', 'logging', 'example'], # arbitrary keywords
  classifiers = [],
)