import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-tiri1992",
    version="0.0.1",
    author="Tiri Georgiou",
    author_email="tirigeorgiou@gmail.com",
    description="A small package example",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Tiri1992/example_pkg",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Licence :: OSI Approved :: MIT Licence",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.8'
)
