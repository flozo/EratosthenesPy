#!/usr/bin/env python3
"""Setup module for Eratosthenes."""

from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Use README.md file as long description
long_description = (here/'README.md').read_text(encoding='utf-8')

setup(
        name='eratosthenes',
        version='0.14',
        description='A program for testing implementations of the sieve of Eratosthenes.',
        long_description=long_description,
        long_description_content_type='text/markdown',
        url='https://github.com/flozo/Eratosthenes',
        author='flozo',
        author_email='github.mail@flozo.de',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Topic :: Education',
            'Topic :: Education :: Testing',
            'Topic :: Scientific/Engineering',
            'Topic :: Scientific/Engineering :: Mathematics',
            ],
        keywords='prime numbers, sieve of Eratosthenes, sieve algorithms, divisors, number theory',
        package_dir={'': 'src'},
        packages=find_packages(where='src'),
        install_requires=['argparse', 'numpy', 'tqdm'],
    )
