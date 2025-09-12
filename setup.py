import sys

from setuptools import setup, Extension
from wheel.bdist_wheel import bdist_wheel


class bdist_wheel_abi3(bdist_wheel):
    def finalize_options(self):
        if sys.implementation == "cpython":
            # on CPython, our wheels are abi3 and compatible back to 3.6
            self.py_limited_api = "cp36"
        super().finalize_options()

setup(
    ext_modules=[
        Extension(
            "spam",
            sources=["spam.c"],
            define_macros=[("Py_LIMITED_API", "0x03060000")],
            py_limited_api=True,
        )
    ],
    cmdclass={"bdist_wheel": bdist_wheel_abi3},
)
