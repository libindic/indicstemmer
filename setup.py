#!/usr/bin/env python

from setuptools import setup, find_packages

name = "stemmer"

setup(
    name=name,
    version="0.1",
    license="LGPL-3.0",
    description="Malayalam word stemmer",
    author="Santhosh Thottingal",
    author_email="santhosh.thottingal@gmail.com",
    long_description="""This application helps you to stem the words
    in the given text. Currently supports only Malayalam.
    Note that this is very experimental and uses a rule based approach.

    """,
    packages=find_packages(),
    include_package_data=True,
    setup_requires=['setuptools-git'],
    install_requires=['setuptools', 'silpa_common'],
    zip_safe=False,
)
