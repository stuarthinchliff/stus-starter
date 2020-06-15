from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="new_api",
    version="0.0.1",
    description="API for *blank*",
    license="MIT",
    long_description=long_description,
    author="Stuart Hinchliff",
    packages=["api"],
)
