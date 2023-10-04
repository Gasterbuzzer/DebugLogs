"""
Setup for Package
"""

from setuptools import setup

from DebugLog.debug import __version__

setup(
    name="debuglog",
    version=__version__,

    url="https://github.com/Gasterbuzzer/DebugLog",
    author="Gasterbuzzer",

    py_modules=['DebugLog'],
)
