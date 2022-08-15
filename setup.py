# Copyright Alan (AJ) Pryor, Jr. 2018

from setuptools import setup, find_packages

setup(
    name="flask_accepts",
    author='Alan "AJ" Pryor, Jr.',
    author_email="apryor6@gmail.com",
    version="0.19.1",
    description="Easy, opinionated Flask input/output handling with Flask-restx and Marshmallow",
    ext_modules=[],
    packages=find_packages(),
    install_requires=[
        "marshmallow>=3.17.0",
        "flask-restx>=0.5.1",
        "werkzeug<2.1"
    ],
)
