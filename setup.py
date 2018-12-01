#!/usr/bin/env python
# coding: utf-8

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requires = [
    'pillow',
]

setuptools.setup(
    name='pixelate-redactor',
    version='0.3',
    author='Vincent Poirier',
    author_email='vincent.poirier@tlmgo.com',
    description='Library that provides pixelation for image redaction',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Eradash/pixelate-redactor',
    packages=setuptools.find_packages(),
    include_package_data=True,
    license="BSD",
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    test_suite="runtests",
    requires=requires,
    tests_require=requires,
    setup_requires=requires,
    scripts=['bin/pixelate-redactor'],
)
