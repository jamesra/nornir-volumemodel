'''
Created on Aug 30, 2013

@author: u0490822
'''




# from ez_setup import use_setuptools
# from setuptools import setup, find_packages
import os
import glob

from ez_setup import use_setuptools

if __name__ == '__main__':
    use_setuptools()

    from setuptools import setup, find_packages

    packages = find_packages()

    install_requires = []

    dependency_links = []

    classifiers = ['Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 2.7',
                   'Topic :: Scientific/Engineering']

    setup(name='nornir_volumemodel',
          classifiers=classifiers,
          version='1.2.0',
          description="Python objects for Nornir volume meta-data",
          author="James Anderson",
          author_email="James.R.Anderson@utah.edu",
          url="https://github.com/nornir/nornir-volumemodel",
          packages=packages,
          scripts=None,
          test_suite='test',
          install_requires=install_requires,
          dependency_links=dependency_links)