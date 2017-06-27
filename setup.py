from setuptools import setup, find_packages
import sys
import os

VERSION = '0.2.1'
DESCRIPTION = ("The Python interface to the Stanford "
               "Named Entity Recognizer Server.")

with open('README.rst') as f:
    long_description = f.read()


setup(
    name='sner',  # 文件名
    version=VERSION,  # 版本(每次更新上传Pypi需要修改)
    description=DESCRIPTION,
    long_description=long_description,  # 放README.rst文件,方便在Pypi页展示
    keywords='python ner nlp stanford Named Entity Recognizer',  # 关键字
    author='caihaoyu',  # 用户名
    author_email='chywj7@gmail.com',  # 邮箱
    url='https://github.com/caihaoyu/sner',  # github上的地址,别的地址也可以
    license='MIT',  # 遵循的协议
    packages=['sner'],  # 发布的包名
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
