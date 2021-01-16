#!/usr/bin/env python

import re
import sys

from codecs import open
from setuptools import setup, find_packages


if sys.argv[-1] == 'publish':
    sys.stderr.write('vehicle_api should not be published')
    sys.exit()

version='0.1'

packages = find_packages()

with open('requirements.txt', 'r', 'utf-8') as f:
    requires = [s.strip() for s in f.readlines()]

if not version:
    raise RuntimeError('Cannot find version information')

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name='vehicle_api',
    version='0.1',
    description='vehicle_api',
    long_description=readme,
    author='Maria',
    author_email='mane.salcedo@gmail.com',
    url='http://www.thispagecannotbedisplayed.com',
    packages=packages,
    package_dir={'vehicle_api': 'vehicle_api'},
    classifiers=[
        'Development Status :: 1 - Interviewing',
        'Programming Language :: Python',
        'Topic :: Software Development',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.9',
    ],
    install_requires=requires,
)
