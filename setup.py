from setuptools import setup, Extension


setup(
    ext_modules=[
        Extension(
            "spam",
            sources=["spam.c"],
            define_macros=[("Py_LIMITED_API", "0x03060000")],
            py_limited_api=True,
        )
    ],
    options={"bdist_wheel": {"py_limited_api": "cp36"}},
)
