from setuptools import setup, find_packages
from os import path


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name = 'PyServerlessDB',
    author='Dhrumil Mistry',
    author_email='contact@dmdhrumilmistry.me',
    version = '0.0.1',
    license='MIT License',
    description = 'ServerLess Local DB for python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    test_suite="tests",
    include_package_data = True,
    install_requires = [],
)