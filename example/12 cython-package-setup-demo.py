"""利用 Cython 对 Python 包进行加密 demo,
MANIFEST.in and include_package_data=True, 打包资源文件
"""

import os
import glob

from setuptools import setup, find_packages
from setuptools.extension import Extension
from setuptools.command.build_py import build_py as build_py_orig
from Cython.Build import cythonize

# 项目根目录
SRC_DIR = "."

# 不进行加密的文件
excluded = ["app_test.py", "db_config.py", "mpc_config", "__init__.py"]


def find_package_modules(package, package_dir):
    module_files = glob.glob(os.path.join(package_dir, "*.py"))
    modules = []
    for f in module_files:
        module = os.path.splitext(os.path.basename(f))[0]
        modules.append((package, module, f))
    return modules


def format_extensions():
    packages = find_packages(SRC_DIR)
    extension_list = []
    for package in packages:
        package_dir = os.path.join(SRC_DIR, *package.split("."))
        print(package_dir)
        for pkg, mod, file in find_package_modules(package, package_dir):
            if os.path.basename(file) in excluded:
                continue
            extension_list.append(
                Extension(
                    f"{pkg}.{mod}",
                    [file, ]
                )
            )
    return extension_list


class build_py(build_py_orig):

    def find_package_modules(self, package, package_dir):
        modules = super().find_package_modules(package, package_dir)
        modules_inculed = [
            (pkg, mod, file)
            for (pkg, mod, file) in modules
            if os.path.basename(file) in excluded
        ]
        return modules_inculed


setup(
    name="iao_app_test",
    version="2.0",
    include_package_data=True,
    packages=find_packages(),
    ext_modules=cythonize(format_extensions()),
    cmdclass={'build_py': build_py}
)
