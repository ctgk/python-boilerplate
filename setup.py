"""setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject/blob/main/setup.py
"""

import pathlib

from setuptools import find_packages, setup


long_description = pathlib.Path(__file__).parent.joinpath(
    'README.md',
).read_text(encoding='utf-8')

install_requires = []
develop_requires = [
    'pre-commit',
    'pytest',

    # format
    'autopep8',
    'flake8',
    'flake8-absolute-import',
    'flake8-broken-line',
    'flake8-builtins',
    'flake8-commas',
    'flake8-docstrings',
    'flake8-import-order',
    'flake8-multiline-containers',
    'flake8-mutable',
    'pep8-naming',

    # documentation
    'sphinx',
    'sphinx_rtd_theme',
    'livereload',
]


setup(
    name='pyboilerplate',
    version='0.0.1',
    author='ctgk',
    author_email='r1135nj54w@gmail.com',
    description='pyboilerplate',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ctgk/python-boilerplate',

    packages=find_packages(
        exclude=('tests', 'tests.*'),
        include=('pyboilerplate', 'pyboilerplate.*')),
    python_requires='>=3',
    install_requires=install_requires,
    extras_require={
        'develop': develop_requires,
    },

    zip_safe=False,
)
