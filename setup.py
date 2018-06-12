#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 andy <andy@AndyDen>
#
# Distributed under terms of the MIT license.

"""
install
"""
try:
    from setuptools import setup
except ImportError:
    from disutils.core import setup


setup(
    name="yamlutil",
    version="0.0.2",
    packages = ['yamlutil'],
    entry_points = {
        "console_scripts":[
        'yamlutil = yamlutil.util:main'
    ]}
)


