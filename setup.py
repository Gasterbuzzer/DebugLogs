"""
Setup for Package
"""

from setuptools import setup, find_packages

from DebugLog import __version__

setup(
    name="debuglog",
    version=__version__,

    url="https://github.com/Gasterbuzzer/DebugLog",
    author="Gasterbuzzer",

    packages=find_packages(),
)
