# coding: utf-8

"""
    Sematext Cloud API Python Client

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # mypy: disable=W0611 # noqa:

NAME = "sematext-cloud-client"
VERSION = "0.1.7"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23"
]


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="sematext-cloud-client",
    version=VERSION,
    description="Sematext Cloud API",
    author_email="packages@sematext.com ",
    url="https://github.com/sematext/sematext-api-client-python",
    keywords=["Sematext", "Cloud", "API", "Monitoring", "Logging", "Metrics"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
