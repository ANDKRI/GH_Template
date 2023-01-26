"""Python setup.py for gh_template package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("gh_template", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="gh_template",
    version=read("gh_template", "VERSION"),
    description="Awesome gh_template created by ANDKRI",
    url="https://github.com/ANDKRI/GH_Template/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="ANDKRI",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["gh_template = gh_template.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
