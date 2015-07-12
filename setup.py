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