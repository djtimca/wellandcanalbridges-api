from distutils.core import setup

setup(
  name = 'wellandcanalbridges',
  packages = ['wellandcanalbridges'],
  version = '0.1.0',
  license='apache-2.0',
  description = 'Integration for Welland Canal Bridge Status',
  author = 'Tim Empringham',
  author_email = 'tim.empringham@live.ca',
  url = 'https://github.com/djtimca/wellancanalbridges',
  download_url = 'https://github.com/djtimca/wellandcanalbridges/archive/v_010.tar.gz',
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