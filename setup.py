"""
Setup file
"""

import setuptools

with open("README.md", "r") as f:
    LONG_DESCRIPTION = f.read()

with open(".meta/packages_base", "r") as f:
    REQUIREMENTS = f.read().split('\n')

with open("LICENSE") as f:
    LICENSE_TEXT = f.read()

setuptools.setup(
    name="chess_server",
    version="0.0.1",
    author="Eugene Bordunov",
    author_email="feugenix@gmail.com",
    description="A small server for playing chess online",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/feugenix/chess-server",
    packages=setuptools.find_packages(),
    license=LICENSE_TEXT,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=REQUIREMENTS,
)
