from setuptools import setup, find_packages
import os

PACKAGE_NAME = 'Crazy Connect 4'
VERSION = '0.0.0'
DESCRIPTION = 'A relatively hard Connect 4 implementation (PvAI).'
STATUS = '1 - Planning'
PYTHON_VERSION_REQUIRED = '>=3.10'
URL = ''

HERE = os.path.dirname(__file__)

try:
    with open(os.path.abspath(os.path.join(HERE, 'README.md')), 'r', encoding='utf-8') as file:
        README = '\n' + file.read()
except FileNotFoundError:
    README = DESCRIPTION

try:
    with open(os.path.abspath(os.path.join(HERE, 'LICENSE')), 'r', encoding='utf-8') as file:
        LICENSE = '\n' + file.read()
except FileNotFoundError:
    LICENSE = 'MIT License'

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type='text/markdown',
    author='Yacine BOUKARI',
    author_email='steeveboukari9@gmail.com',
    url=URL,
    download_url=URL,
    license=LICENSE,
    scripts=['main.py'],
    packages=find_packages(exclude=('tests',)),
    classifiers=[
        f'Development Status :: {STATUS}',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Environment :: X11 Applications :: Qt',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires=PYTHON_VERSION_REQUIRED,
)
