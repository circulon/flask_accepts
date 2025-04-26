# Copyright Alan (AJ) Pryor, Jr. 2018

from setuptools import setup, find_packages

setup(
    name="flask_accepts",
    author='Alan "AJ" Pryor, Jr.',
    author_email="apryor6@gmail.com",
    version="1.1.0",
    description="Easy, opinionated Flask input/output handling with Flask-restx and Marshmallow",
    ext_modules=[],
    packages=find_packages(),
    install_requires=[
        "marshmallow>=3.26,<4",
        "flask-restx>=1.2",
        "werkzeug>=3,<4",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
