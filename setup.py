import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="chess_server",
    version="0.0.1",
    author="Eugene Bordunov",
    author_email="feugenix@gmail.com",
    description="A small server for playing chess online",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/feugenix/chess-server",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD",
        "Operating System :: OS Independent",
    ],
)
