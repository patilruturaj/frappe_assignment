from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in assignment/__init__.py
from assignment import __version__ as version

setup(
	name="assignment",
	version=version,
	description="We do assignments",
	author="ruturaj.p@nomail.com",
	author_email="ruturaj.p@nomail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
