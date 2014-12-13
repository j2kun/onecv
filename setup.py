from setuptools import setup

setup(name='onecv',
      version='0.2',
      description='A Python package for making CVs of all kinds from one json file.',
      url='http://github.com/j2kun/onecv',
      author='Jeremy Kun',
      author_email='jkun2@uic.edu',
      license='MIT',
      packages=['onecv'],
      scripts=['bin/onecv-moderncv',
               'bin/onecv-website'],
      zip_safe=False)
