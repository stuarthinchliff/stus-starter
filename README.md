# New Project!

New project!

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 
See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Will require some things!

### Installing


You can build and run the environment using:

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

Coding style adheres to flake8 for which a linter script is used and can be run as per below:

```
python linters/flake_lint.py
```

Code quality is measured by radon. The project aims to adhere to a maximum code complexity of 15.
A wrapper script is used to monitor code complexity.
```
python linters/radon_cc.py
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Flake8](https://flake8.pycqa.org/en/latest/) - Linting
* [Radon](https://radon.readthedocs.io/en/latest/) - Code Quality

## Authors

* **Stuart Hinchliff** - *Initial work*

See also the list of [contributors](https://github.com/stuarthinchliff/stus-starter/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* 
