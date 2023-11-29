# This file is if we want to be able to pip install it & upload the package to pypi

from setuptools import setup


setup(name='jumping_man',
      version='0.0.1',
      description='Package shows small jumping man',
      author='Ian Sebby',
      author_email='iansebby4@gmail.com',
      url='https://github.com/isebby/simple_python_package',
      packages=['my_pkg'],
      license='MIT',
      )
