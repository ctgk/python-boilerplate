"""setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject/blob/main/setup.py
"""

from setuptools import find_packages, setup


setup(
    packages=find_packages(
        exclude=('docs', 'tests'),
        include=('pyboilerplate', 'pyboilerplate.*')),
)
