from setuptools import setup, find_packages
import sys
import os

VERSION = '0.2.2'
DESCRIPTION = ("The Python interface to the Stanford "
               "Named Entity Recognizer Server.")

with open('README.rst') as f:
    long_description = f.read()


setup(
    name='sner',
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    keywords='python ner nlp stanford Named Entity Recognizer',
    author='caihaoyu',
    author_email='chywj7@gmail.com',
    url='https://github.com/caihaoyu/sner',
    license='MIT',
    packages=['sner'],
    include_package_data=True,
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
)
