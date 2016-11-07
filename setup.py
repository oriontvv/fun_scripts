from setuptools import setup, find_packages
from os.path import join, dirname

import scripts

def read(fname):
    return open(join(dirname(__file__), fname)).read()

setup(
    name='fun_scripts',
    author='oriontvv',
    author_email='taranov.vv@gmail.com',
    license='apache2',
    version=scripts.__version__,
    packages=find_packages(),
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache2 License",
        "Programming Language :: Python :: 3",
    ],

)
