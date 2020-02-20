#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

requirements = []

setup_requirements = ["pytest-runner"]

test_requirements = ["pytest>=3"]

setup(
    author="Morgan Bye",
    author_email="morgan@morganbye.com",
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: General audience",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    description="Museum to city size correlation.",
    install_requires=requirements,
    long_description=readme,
    include_package_data=True,
    keywords="museum",
    name="museums",
    packages=find_packages(include=["src", "tests"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="http://morganbye.com",
    version="0.1.0",
    zip_safe=False,
)
