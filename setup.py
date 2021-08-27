# Copyright 2020-2021 The MathWorks, Inc.
import os
from setuptools.command.install import install
import setuptools
from pathlib import Path
from shutil import which


tests_require = [
    "pytest",
    "pytest-env",
    "pytest-cov",
    "pytest-mock",
    "pytest-aiohttp",
    "requests",
    "psutil",
]

HERE = Path(__file__).parent.resolve()
long_description = (HERE / "README.md").read_text()

setuptools.setup(
    name="dummy-basic",
    version="0.1.4",
    url="https://github.com/chimmy-change/dummy-basic",
    author="Chimmy",
    author_email="chimmy-changa@gmail.com",
    license="Generic License",
    description="Gets strings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(exclude=["devel", "tests"]),
    keywords=["Jupyter"],
    classifiers=["Framework :: Jupyter"],
    python_requires="~=3.7",
    install_requires=["jupyter-server-proxy", "aiohttp>=3.7.4"],
    # setup_requires=["pytest-runner"],
    setup_requires=[],
    tests_require=tests_require,
    extras_require={"dev": ["aiohttp-devtools"] + tests_require},
    entry_points={
        "jupyter_serverproxy_servers": ["matlab = jupyter_matlab_proxy:setup_matlab"],
        "console_scripts": ["get_hello = dummy_basic.get:get_hello"],
    },
    include_package_data=True,
    zip_safe=False,
)
