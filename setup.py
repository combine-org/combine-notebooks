#!/usr/bin/env python
"""Setup script."""
from setuptools import setup  # type: ignore
import os


if __name__ == "__main__":
    setup(version="0.1.4")
    os.system('pre-commit install')
