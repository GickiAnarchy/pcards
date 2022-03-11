#setup.py

from setuptools import setup

setup(
   name='pcards',
   version='0.1.0',
   author='GickiAnarchy',
   author_email='fatheranarchy@programmer.net',
   url='https://github.com/GickiAnarchy/pcards.git',
   scripts = ['bin/pcardsbin']
   license='NONE',
   description='Basic Playing Card(s) package',
   long_description=open('README.txt').read(),
)
