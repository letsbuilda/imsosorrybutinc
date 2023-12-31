""" Set up the package
TODO: switch to pyproject.toml
"""
from setuptools import Extension, setup

setup(
    name = "imsocorry",
    version = "0.1.0",
    url = "https://github.com/letsbuilda/imsosorrybutinc",
    description = "Sometimes it can be necessary to call upon the ancient arts... But in C!"
    ext_modules=[
        Extension(
            name="uwuifier",
            sources=["src/uwuifier.c"],
            include_dirs=["src"]
        ),
    ]
)
