import sys
import os
import setuptools
import sysconfig
from setuptools.command.install import install

class PreInstall(install):
    def run(self):
        site_packages_dir = sysconfig.get_path("purelib")
        usercustomize_path = os.path.join(site_packages_dir, "usercustomize.py")
        if os.path.exists(usercustomize_path):
            raise FileExistsError("User customize file already exists. "
                                  "Please remove it before installing.")
        install.run(self)


setuptools.setup(
    name='4to5',
    version='0.0.1',
    author="Bar Harel",
    py_modules=["usercustomize"],
    cmdclass={'install': PreInstall,},
        data_files=[
        ('.', ['startup.pth'])
    ]
)
)