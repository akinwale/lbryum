#!/usr/bin/env python2

# python setup.py sdist --format=zip,gztar

from setuptools import setup, find_packages
import sys
import os
import lbryum

if sys.version_info[:3] < (2, 7, 0):
    sys.exit("Error: lbryum requires Python version >= 2.7.0...")

data_files = []

requires = [
    'slowaes>=0.1a1',
    'ecdsa==0.13',
    'pbkdf2',
    'requests',
    'qrcode',
    'protobuf==3.2.0',
    'dnspython',
    'jsonrpclib',
    'six>=1.9.0',
    'appdirs==1.4.3',
    'lbryschema==0.0.7'
]

console_scripts = [
    'lbryum = lbryum.main:main',
    # 'lbrynet-cli = lbrynet.lbrynet_daemon.DaemonCLI:main'
]


base_dir = os.path.abspath(os.path.dirname(__file__))

setup(
    name="lbryum",
    version=lbryum.__version__,
    install_requires=requires,
    packages=find_packages(base_dir, exclude=['tests'], include=['lbryum/wordlist/*.txt']),
    entry_points={'console_scripts': console_scripts},
    data_files=data_files,
    description="Lightweight LBRYcrd Wallet",
    author="LBRY Inc.",
    author_email="hello@lbry.io",
    license="GNU GPLv3",
    url="https://lbry.io",
    long_description="""Lightweight LBRYcrd Wallet"""
)
