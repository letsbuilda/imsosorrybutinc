"""
Set up the package
TODO: switch to pyproject.toml
"""
from setuptools import Extension, setup

setup(
    ext_modules=[
        Extension(
            name="uwuifier",
            sources=["src/uwuifier.c"],
        ),
    ]
)
