#
# Copyright 2020 Stephan Mueller
#
# Licensed under the MIT license

"""Setup for td_kernel_dmvw module."""

import json
import logging
import os
import subprocess

import setuptools

logger = logging.getLogger(__name__)


def get_install_requirements() -> list:
    """Retrieves list of packages from Pipfile.lock required for installation.

    Returns: List of packages
    """
    with open("Pipfile.lock") as file:
        pipfile = file.read()

    packages = list()
    for name, options in json.loads(pipfile)["default"].items():
        packages.append(name + options['version'])
    return packages


def long_description() -> str:
    """Reads README.md

    Returns: Content of ``README.md``
    """
    with open("README.md", "r") as file:
        return file.read()


def version() -> str:
    """Tries to detect version based on selected strategy.

    Returns: Project version
    """

    version_strategy = os.getenv("VERSION_STRATEGY", "GIT_REF_NAME")

    if version_strategy == "GIT_COMMIT_SHA":

        if os.getenv("CI_COMMIT_SHA", "") != "":
            return os.getenv("CI_COMMIT_SHA")

        process = subprocess.run(["git", "rev-parse", "--quiet", "HEAD"], capture_output=True, check=True)
        commit_sha = process.stdout.decode().strip()
        if commit_sha is not None and commit_sha != "":
            return "0.0.0.commit" + commit_sha

    elif version_strategy == "GIT_REF_NAME":

        if os.getenv("CI_COMMIT_REF_NAME", "") != "":
            return os.getenv("CI_COMMIT_REF_NAME")

        process = subprocess.run(["git", "symbolic-ref", "--quiet", "HEAD"], capture_output=True, check=True)
        branch = process.stdout.decode().strip().replace("refs/heads/", "", 1)
        if branch is not None and branch != "":
            return branch

    raise ValueError("Version could not be detected.")


setuptools.setup(
    name="td_kernel_dmvw",
    version=version(),
    author="Stephan Müller",
    license_file="LICENSE",
    description="This project provides an algorithm for calculating gas distribution maps.",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    url="https://gitlab.com/smueller18/TDKernelDMVW",
    packages=setuptools.find_packages(),
    install_requires=get_install_requirements(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    project_urls={
        'Documentation': 'https://smueller18.gitlab.com/TDKernelDMVW/',
        'Source': 'https://gitlab.com/smueller18/TDKernelDMVW',
        'Tracker': 'https://gitlab.com/smueller18/TDKernelDMVW/issues',
    },
)
