"""
Setup for Package
"""

from setuptools import setup, find_packages

from DebugLog import __version__

setup(
    name="debuglog",
    version=__version__,

    description='A package for easy colored debug logs.',

    url="https://github.com/Gasterbuzzer/DebugLog",
    author="Gasterbuzzer",

    packages=find_packages(),

    classifiers=[
        'Intended Audience :: Developers',

        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ]
)
