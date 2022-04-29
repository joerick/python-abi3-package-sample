from setuptools import setup, Extension
from wheel.bdist_wheel import bdist_wheel


class bdist_wheel_abi3(bdist_wheel):
    def get_tag(self):
        python, abi, plat = super().get_tag()

        if python.startswith("cp"):
            # on CPython, our wheels are abi3 and compatible back to 3.6
            return "cp36", "abi3", plat

        return python, abi, plat


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
