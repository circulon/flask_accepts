# Copyright Alan (AJ) Pryor, Jr. 2018

from setuptools import setup, find_packages

setup(
    name="flask_accepts",
    author='Alan "AJ" Pryor, Jr.',
    author_email="apryor6@gmail.com",
    version="2.0.0",
    description="Easy, opinionated Flask input/output handling with Flask-restx and Marshmallow",
    ext_modules=[],
    packages=find_packages(),
    package_dir={"": "src"},
    install_requires=[
        "marshmallow>=3.17",
        "flask-restx>=1.3",
        "werkzeug>=3,<4",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
