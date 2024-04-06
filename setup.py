"""Dynamic configuration for Setuptools."""

from setuptools import Extension, setup

setup(
    ext_modules=[
        Extension(
            name="uwuifier",
            include_dirs=["src"],
            sources=["src/uwuifier.c"],
        ),
    ],
)
