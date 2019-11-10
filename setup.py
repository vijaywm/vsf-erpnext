# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in vsf_erpnext/__init__.py
from vsf_erpnext import __version__ as version

setup(
	name='vsf_erpnext',
	version=version,
	description='vue storefront api for erpnext',
	author='vijay_wm@yahoo.com',
	author_email='vijay_wm@yahoo.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
