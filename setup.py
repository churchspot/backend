#!/usr/bin/env python

from distutils.core import setup

setup(name='backend',
      version='1.0',
      description='Python Distribution Utilities',
      author='Kamil Michna',
      packages=['distutils', 'distutils.command','flask','requests'],
     )