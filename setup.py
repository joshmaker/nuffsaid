# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = ""

setup(
    long_description=readme,
    name="nuffsaid",
    version="0.1.0",
    python_requires=">=3.7.0",
    author="Josh West",
    author_email="18324+joshmaker@users.noreply.github.com",
    entry_points={
        "console_scripts": [
            "count_schools = nuffsaid.cli:cli_print_counts",
            "search_schools = nuffsaid.cli:cli_search_schools",
        ]
    },
    packages=["nuffsaid"],
    package_dir={"": "src"},
    package_data={},
    install_requires=[],
)
