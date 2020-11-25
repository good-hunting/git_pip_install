from setuptools import setup

setup(
    name='testfirstpkg',
    version='0.0.1',
    description='package test pip install test ',
    url='https://github.com/good-hunting/git_pip_install.git',
    author='ikhyun.roh',
    license='ikhyun.roh',
    packages=['testfirstpkg'],
    zip_safe=False,
    install_requires=['numpy==1.18.3']

)