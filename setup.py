#!/usr/bin/env python
from setuptools import setup

setup(
    name="turbosmsua-python3",
    packages=["turbosmsua-python3"],
    version="0.4",
    description="Client for https://turbosms.ua",
    author="Oleksii Orzeshkovskyi",
    author_email="al.orzh@gmail.com",
    url="https://github.com/aorzh/turbosmsua",
    keywords=["turbosmsua", "turbosms", "sms ua"],
    classifiers=[],
    install_requires=[
        "suds",
    ],
)
