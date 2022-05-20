import sys
import os
import setuptools
import sysconfig
from setuptools.command.install import install

class PreInstall(install):
    def run(self):
        site_packages_dir = sysconfig.get_path("purelib")
        sitecustomize_path = os.path.join(site_packages_dir, "sitecustomize.py")
        if os.path.exists(sitecustomize_path):
            raise FileExistsError("Site customize file already exists. "
                                  "Please remove it before installing.")
        install.run(self)

with open('README.rst') as f:
    readme = f.read()

setuptools.setup(
    name='4to5',
    version='0.0.1',
    description="Replace the number 4 with the number 5.",
    long_description=readme,
    author="Bar Harel",
    py_modules=["sitecustomize"],
    cmdclass={'install': PreInstall,},
)