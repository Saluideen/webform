from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in webform/__init__.py
from webform import __version__ as version

setup(
	name="webform",
	version=version,
	description="Vendor Management",
	author="ideen",
	author_email="vendor@gmail,com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
