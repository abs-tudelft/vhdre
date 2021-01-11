#!/usr/bin/env python3

import os
from setuptools import setup

def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()

setup(
    name = "vhdre",
    version = "0.3",
    author = "Jeroen van Straten",
    author_email = "j.vanstraten-1@tudelft.nl",
    description = (
        "VHDL code generator for matching regular expressions."
    ),
    license = "MIT",
    keywords = "vhdl regular expression generator",
    url = "http://packages.python.org/vhdre",
    long_description = read('README.md'),
    long_description_content_type = 'text/markdown',
    classifiers = [
        "Development Status :: 4 - Beta",
        "Topic :: Software Development :: Code Generators",
        "License :: OSI Approved :: MIT License",
    ],
    packages = ['vhdre'],
    install_requires = ['funcparserlib'],
)
