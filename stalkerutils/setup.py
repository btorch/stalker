#!/usr/bin/env python
""" setuptools for stalkerutils """

from setuptools import setup, find_packages
from stalkerutils import __version__ as version

setup(
    name='stalkerutils',
    version=version,
    author="Florian Hines",
    author_email="syn@ronin.io",
    description="Simple Monitoring System",
    url="http://github.com/pandemicsyn/stalker",
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.6',
        'Environment :: No Input/Output (Daemon)',
    ],
    install_requires=[
    ],
    include_package_data=True,
    zip_safe=False,
    data_files=[('share/doc/stalkerutils',
                 ['README.md', 'INSTALL',
                 ])]
)
