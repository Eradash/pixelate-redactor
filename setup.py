#!/usr/bin/env python
# coding: utf-8

import sys
from setuptools import setup, find_packages

requires=[
    'pillow',
]

setup(
    name='pixelate-redactor',
    version='0.1',
    author='Vincent Poirier',
    author_email='poirier.20.100@hotmail.com',
    description='Library provides pixelation for images for redaction',
    long_description="""
# pixelate-redactor

Redact images with blur

Works with Python >= 2.6, Python >= 3.2.

## Installation

    pip install pixelate-redactor

## Example

    pixelate-redactor --input=img/bps.jpg --output=img/bps.png --pixel-size=10 --start-x=100 --start-y=100 --size-x=500 --size-y=60

see more https://github.com/Eradash/pixelate-redactor
""",
    url='https://github.com/Eradash/pixelate-redactor',
    packages=find_packages(),
    include_package_data=True,
    license="BSD",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite="runtests",
    requires=requires,
    tests_require=requires,
    setup_requires=requires,
    scripts=['bin/pixelate-redactor'],
)
