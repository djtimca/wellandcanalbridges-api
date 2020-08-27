from setuptools import setup

with open("README.md","r") as fh:
  long_description = fh.read()

setup(
  name = 'wellandcanalbridges',
  packages = ['wellandcanalbridges'],
  version = '0.1.1',
  license='apache-2.0',
  description = 'Integration for Welland Canal Bridge Status',
  long_description = long_description,
  long_description_content_type = "text/markdown",
  author = 'Tim Empringham',
  author_email = 'tim.empringham@live.ca',
  url = 'https://github.com/djtimca/wellancanalbridges',
  download_url = 'https://github.com/djtimca/wellandcanalbridges/archive/v_011.tar.gz',
  keywords = ['Niagara', 'Canal', 'Welland Canal', 'Bridge', 'Status'],
  install_requires=[
          'aiohttp',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)