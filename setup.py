import os
from setuptools import setup, find_packages

NAME = 'ly-cdn-tools'
DESCRIPTION = "longyuan cdn tools"
TOPDIR = os.path.dirname(__file__) or "."
VERSION ='0.2'

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author="smartwang",
    author_email="407718756@qq.com",
    maintainer='wangying',
    maintainer_email='wangying@dragonest.com',
    license="LGPL",
    include_package_data=True,
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'aliyun-python-sdk-cdn',
    ],
)

