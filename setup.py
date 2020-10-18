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
    # Add main dependencies
    install_requires=[
        "requests>=2.24.0"
    ],
    # Development dependencies: Not required to run package
    extras_require={
        "dev": [
            "pytest>=3.7",
            "autopep8==1.5.4",
            "mypy==0.790"
        ]
    },
    # Exclude the tests package
    packages=setuptools.find_packages(exclude=['tests']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8"
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.8'
)
