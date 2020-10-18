# Getting Started

Tutorial Example: https://packaging.python.org/tutorials/packaging-projects/

How to install and use package:

First set up a virtual environment in root directory and add to .gitignore

```sh
$ python -m venv env

# Source the virtual env

$ source env/bin/activate
```

Now to install the source files in the virtual environment

```sh
# In the root directory run

$ pip install -e .

# Check to see if its installed in virtual env

$ pip list

# example-pkg-tiri1992 0.0.1
```

### Additional: Development

To install example_pkg, along with the tools you need to develop and run tests, run the following in your virtual environment:

```sh
$ pip install -e .[dev]
```


### Creating a distribution package with sdist

First look inside MANIFEST.in to include files that are not python files but want to be part of the distribution package.

```sh
# In root directory run

$ python setup.py sdist
```

This should create a dist/ directory in the root directory. Now to check everything was pacakaged correctly run:

```sh
# This should show a list of files that were distributed with your package
# Check to see if LICENCE was include 

$ tar --list -f dist/example-pkg-tiri1992-0.0.1.tar.gz
```