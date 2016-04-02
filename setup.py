#!/usr/bin/env python3

from distutils.core import setup

def read(fname):
    import os
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="battery_charge",
    version="0.0.1",
    author="Yifei Zhang",
    author_email="njzhangyifei@gmail.com",
    description=("A tiny python package for getting laptop battery " \
                  "charge information on Linux/OS X/Windows."),
    license="MIT",
    keywords="battery charge laptop utility",
    packages=["battery_charge"],
    scripts=["script/battery_charge"],
    long_description=read("README.md"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)



