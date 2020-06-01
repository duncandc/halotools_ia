from setuptools import setup, find_packages


PACKAGENAME = "halotools_ia"
VERSION = "0.1"


setup(
    name=PACKAGENAME,
    version=VERSION,
    setup_requires=["pytest-runner"],
    author="Duncan Campbell",
    author_email="duncanc@andrew.cmu.edu",
    description="Python tools for studying intrinsic alignments in simulations",
    long_description="An add-on package for Halotools which contains python tools for studying intrinsic alignments in simulations",
    install_requires=["numpy, halotools"],
    packages=find_packages(),
    url="https://github.com/duncandc/halotools_ia",
)