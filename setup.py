from setuptools import find_packages,setup
from typing import List

setup(
    name='HousePrice',
    version='0.0.4',
    author='rugvedp',
    author_email='rugvedbpatil2003@gmail.com',
    install_requires=["scikit-learn","pandas","numpy"],
    packages=find_packages()
)