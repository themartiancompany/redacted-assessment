"""Setup for Mysterious Shop"""
from setuptools import setup, find_packages

with open(
  "README.md",
  "r") as _fh:
  _long_description = _fh.read()

_name = "mysterious-shop"
_version = "0.0.0.0.0.0.0.0.0.0.0.1"
_setup_kwargs={
  'name':
    f"{_name}",
  'version':
    f"{_version}",
  'author':
    "Pellegrino Prevete",
  'author_email':
    "pellegrinoprevete@gmail.com",
  'description':
    ("A simple online shop application written "
     "for an job interview."),
  'long_description':
    f"{_long_description}",
  'long_description_content_type':
    "text/markdown",
  'url':
    f"https://github.com/themartiancompany/{_name}",
  'packages':
    find_packages(),
  'entry_points': {
    'console_scripts': [
      'mysterious-shop = mysterious_shop:_main']
  },
  'install_requires': [
    'appdirs'
  ],
  'classifiers': [
    ("Programming Language :: "
       "Python :: "
         "3"),
    ("License :: "
     "OSI Approved :: "
       "GNU Affero General Public License v3 or later (AGPLv3+)"),
    ("Operating System :: "
     "Unix"),
  ],
}

setup(
  **_setup_kwargs)
