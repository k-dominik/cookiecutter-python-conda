# Python cookiecutter for conda-based projects

A [cookiecutter](https://www.github.com/audreyr/cookiecutter "cookiecutter") template for conda-based Python projects

## Features

 - Basic conda recipe found in conda.recipe/meta.yaml
 - CI-integration with for Travis CI
 - `setup.cfg`
 - Versioning with `bumpversion`

## Usage

This cookiecutter is for conda-base Python projects. 
In order to use it, the `cookiecutter` package needs to be installed.
Of course this package is readily available from conda:

```bash
conda install cookiecutter
```

In order to start a new Python project using this cookiecutter just type:

```bash
cookiecutter https://github.com/k-dominik/cookiecutter-python-conda.git
bash

## Features of your new repo:

### Continuous integration (CI)

In order to use Travis CI, you need get the created repo into version control that integrates with Travis CI.
Information about activating the repo for Travis can be found [here](https://docs.travis-ci.com/user/getting-started/#To-get-started-with-Travis-CI).
However, first things first:

```bash
git init
git add .
git commit "Initial commit"
# Do more stuff, configure remotes.
git push
```

### Automatic versioning with bumpversion

TODO

### Dependency management

There are two different types of dependencies:

1) Package dependencies for deployment: These dependencies should be added to your project's `setup.py` under the requirements section. These packages are automatically added to the conda recipe in `conda-recipe/meta.yaml`. 
2) Development dependencies: All packages that are needed for development, should be added to your package's `dev/environment-dev.yaml`.
