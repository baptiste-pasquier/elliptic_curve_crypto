# -*- coding: utf-8 -*-
import os
from distutils.core import setup
from setuptools import find_packages

here = os.path.dirname(__file__)
if here == "":
    here = '.'
packages = find_packages(where=here)
package_dir = {k: os.path.join(here, k.replace(".", "/")) for k in packages}

with open(os.path.join(here, "requirements.txt"), "r") as f:
    requirements = f.read().strip(' \n\r\t').split('\n')
if len(requirements) == 0 or requirements == ['']:
    requirements = []

setup(name='eccrypto',
      version='0.1',
      description="Cryptographie sur les courbes elliptiques",
      long_description=""
                       "",
      author='Baptiste Pasquier',
      author_email='pasquierbaptiste@hotmail.fr',
      url='https://github.com/baptiste-pasquier/elliptic_curve_crypto/',
      packages=packages,
      package_dir=package_dir,
      requires=requirements)
