from setuptools import setup, find_packages

setup(name='onecv',
      version='0.2',
      description='A Python package for making CVs of all kinds from one json file.',
      url='http://github.com/j2kun/onecv',
      author='Jeremy Kun',
      author_email='jkun2@uic.edu',
      license='MIT',
      packages=find_packages(),
      scripts=['bin/onecv-moderncv',
               'bin/onecv-website'],
      include_package_data=True,
      zip_safe=False)
