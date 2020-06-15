# New Project!

[![stuarthinchliff](https://circleci.com/gh/stuarthinchliff/stus-starter.svg?style=shield)](https://app.circleci.com/pipelines/github/stuarthinchliff/stus-starter)

New project! Always good to start with a new project with a good basis. This project is to act as a template for python projects. 

It starts with some basics such as conda to manage the environment, a circleci yml to be used for continuous integration, unittests and some linting.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

Select the "Use this template" to kick off a new project with this basis.

### Prerequisites

Will require some things:
* [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

### Installing


You can build and run the environment using conda:

```
conda env create -f env.yml -n myenv
conda activate myenv
```

Scripts, tests and linters should all be run from the home directory.

To add examples...

## Tests and CI

Continuous integration is run on this project using CircleCI.

Unittests are based off the standard library unittest framework. They can be run as follows.

Example:

```
python tests/unittests/test_something.py
```

### And coding style tests

Code quality and style is maintained with the help of scripts in the "linters" folder. These are wrappers of the cli provided by these packages to be tailored specifically at a project level. 

Coding style adheres to flake8 for which a linter script is used and can be run as per below:

```
python linters/flake_lint.py
```
Note that E203 is ignored to allow Black to format the code.

Code quality is measured by radon. The project aims to adhere to a maximum code complexity of 15.
A wrapper script is used to monitor code complexity.
```
python linters/radon_cc.py
```

Black is used to format code. It complies to the line length set by Flake8 (79) in this project. Providing the '-f' option will automatically format code.
```
python linters/black_formatter.py -f
```

## Built With

* [Flake8](https://flake8.pycqa.org/en/latest/) - Linting
* [Radon](https://radon.readthedocs.io/en/latest/) - Code Quality
* [Black](https://black.readthedocs.io/en/stable/) - Automatic code formatting

## Authors

* **Stuart Hinchliff** - *Initial work*

See also the list of [contributors](https://github.com/stuarthinchliff/stus-starter/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
