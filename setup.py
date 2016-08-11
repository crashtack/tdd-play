# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="ackermann",
    description="A Python implementation of the Ackermann Function.",
    version=0.1,
    author="David Banks",
    author_email="crashtack@gmail.com",
    license='MIT',
    py_modules=['ackermann'],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-watch', 'tox']},
)
