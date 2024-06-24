from setuptools import setup, Extension, find_packages
from os import path

working_directory = path.abspath(path.dirname(__file__))

with open(path.join(working_directory, 'README.MD'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="example_package_irshad_calculator",
    version="0.3",
    author="Irshad",
    author_email="",
    description="Packaging concept",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="",
    packages=find_packages(),
    install_requires=[]
)
