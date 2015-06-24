#!/usr/bin/env python
from setuptools import setup
import os
import sys

# Publish the library to PyPI.
if "publish" in sys.argv[-1]:
    os.system("python setup.py sdist upload")
    sys.exit()

# Push a new tag to GitHub.
if "tag" in sys.argv:
    os.system("git tag -a {0} -m 'version {0}'".format(version))
    os.system("git push --tags")
    sys.exit()

setup(
    name="wig3j-grid",
    version='0.1',
    author="Timothy D. Morton",
    author_email="tim.morton@gmail.com",
    url="https://github.com/timothydmorton/wig3j-grid",
    license="MIT",
    description="writes grids of Wigner 3j symbols",
    long_description=open("README.md").read(),
    scripts=['calc-wig3j'],
    classifiers=[
        # "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GPL License",
        "Programming Language :: Python",
    ],
)
