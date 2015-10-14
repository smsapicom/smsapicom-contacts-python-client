#!/usr/bin/env python

from smsapicontacts import __version__

from setuptools import setup, find_packages

setup(
    name='smsapicom-contacts',
    version=__version__,
    description='Python client for SMSAPI.com contacts rest API.',
    long_description=open('README.md').read(),
    author='SMSAPI',
    author_email='support@smsapi.com',
    url='https://github.com/smsapicom/smsapicom-contacts-python-client',
    packages=find_packages(),
    license=open('LICENSE').read(),
    install_requires=[
        'requests',
    ],
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: Apache 2.0',
        'Topic :: Software Development :: Libraries :: Python Modules'
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ),
    test_suite='tests.suite'
)