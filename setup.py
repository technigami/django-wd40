#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

setup(
    name='django-wd40',
    version='0.0.1 alpha',
    description='A set of tools to facilitate Django development',
    author='Daniel Gray',
    author_email='dan@technigami.com',
    url='https://github.com/Technigami/django-wd40',
    long_description=open('README.rst', 'r').read(),
    packages=[
        'wd40',
        'wd40.management',
        'wd40.management.apptemplate',
        'wd40.management.commands',
    ],
   
    zip_safe=False,
    #requires=[
    #],
    #install_requires=[
    #    'mimeparse',
    #    'python_dateutil >= 1.5, != 2.0',
    #],
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
)