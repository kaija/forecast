#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of forecast.
# https://github.com/kaija/forecast.git

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2020, Kaija <kaija.chang@gmail.com>

from setuptools import setup, find_packages
from forecast import __version__

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'preggy',
    'tox',
    'ipdb',
    'coveralls',
    'sphinx',
]

setup(
    name='forecast',
    version=__version__,
    description='A library for metric forecast',
    long_description='''
A library for metric forecast
''',
    keywords='cloudwatch, dataframe, forecast',
    author='Kaija',
    author_email='kaija.chang@gmail.com',
    url='https://github.com/kaija/forecast.git',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # add your dependencies here
        # remember to use 'package-name>=x.y.z,<x.y+1.0' notation (this way you get bugfixes)
    ],
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            # add cli scripts here in this form:
            # 'forecast=forecast.cli:main',
        ],
    },
)
