# Getting Started

We've selected the src/ package structure from the official [docs](https://packaging.python.org/tutorials/packaging-projects/) and moved most of the boilerplate setup configs to ``setup.cfg``. Also, we defined a pyproject.toml which tells python which build method to use.

### Best solution using ``make``

We've introduced a ``Makefile`` to automate alot of the build and getting setup stages.

Setting up a **development environment** requires python version 3.7 or above. Then simply run:

```sh
$ make dev
```

To run test suites on the project:

```sh
$ make test
```

To package the project as a wheel and sdist:

```sh
$ make build-package
```

To remove cache files (*.pyc, __pycache__ etc):

```sh
$ make clean-cache
```

To remove builds, env as well as cache files:

```sh
$ make clean
```

For more information about what is available in the ``make`` commands type:

```sh
# All options will be revealed
$ make
```

### Alternative (more manual solution)

To install the package in editable mode (to run tests while developing):

```sh
# cd into root dir
$ pip install -e .
```

To build the package as either a wheel or source distribution (sdist), make sure you have upgraded your build method via pip (in a venv) by typing:

```sh
$ python3 -m pip install --upgrade build
```

And then to build:

```sh
# --sdist to build a source distribution
# --wheel to build a wheel, Nothing specified builds both
$ python -m build
```

The files will now be present in ``/dist`` directory, which we can now use to install our package in our virtual environment by doing:

```sh
# installing via wheel (fastest method)
$ pip install dist/dist/example_pkg_tiri-0.1.0-py3-none-any.whl 
```

## How to develop with our code

### Best solution

Although according to pythons official docs are moving towards a stand alone setup.cfg, pyproject.toml project structure, they have still recommended keeping the setup.py script to install package in editable mode. This makes it easier to develop with (package discovery with /tests).

```sh
# cd into root folder
# aside from [all], there exists [test], [docs], [style]
$ pip install -e .[all]
```

Now to run test suite we have our package referenced in our virtual environment, so any changes made in our source code will be reflected. It also means in our tests we can import directly from the module because its now in our python path (see ``test_calculator.py`` for an example).

```sh
pytest -v tests
```