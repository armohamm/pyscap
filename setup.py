#!/usr/bin/env python

from glob import glob
from os.path import join
from os.path import dirname
import re
from setuptools import find_packages
from setuptools import setup

with open(join(dirname(__file__), 'VERSION.txt'), 'r') as f:
    VERSION = f.read().strip()

with open(join(dirname(__file__), 'README.rst'), 'r') as f:
    README = f.read()

with open(join(dirname(__file__), 'CHANGELOG.rst'), 'r') as f:
    CHANGELOG = f.read()

with open(join(dirname(__file__), 'CLASSIFIERS.txt'), 'r') as f:
    CLASSIFIERS = list(f)

with open(join(dirname(__file__), 'KEYWORDS.txt'), 'r') as f:
    KEYWORDS = list(f)

with open(join(dirname(__file__), 'requirements.txt'), 'r') as f:
    REQUIREMENTS = list(f)

long_description = README + '\n' + CHANGELOG

setup(name='PySCAP',
    version=VERSION,
    license='GPL',
    description='A security scanner consuming and generating SCAP content',
    long_description=long_description,
    author='Casey Jaymes',
    author_email='cjaymes@gmail.com',
    url='https://github.com/cjaymes/pyscap',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=CLASSIFIERS,
    keywords=KEYWORDS,
    install_requires=REQUIREMENTS,
    tests_require=[
        'pytest',
    ],
    zip_safe=True,
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'pyscap = pyscap:main',
        ]
    },
)
