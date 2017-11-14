This will provide a command line interface for you to generate a Secret Santa list

# Pre-requisites
1. python 3
1. pip3
1. setuptools (for testing or building & installing the package)

# Running the program
There are two suggested options for running this program (assuming you have cloned the repo).

## Building and installing the package
1. Make sure you have setuptools installed
1. Run `python setup.py bdist_wheel --universal` to create a wheel
1. Run `pip3 install dist/command_line_secret_santa-0.1.0-py2.py3-none-any.whl` to install the wheel
1. On the command line, run `secret_santa` to use the program

## Running in a Virtual Environment
1. Create virtual environment `python -m venv myven`
1. Activate the virtual environment `source myvenv/bin/activate`
1. Run `python secret_santa/main.py` in secret_santa directory
    1. Once you're done, you can use `deactivate` to leave the virtual environment

# Running the tests
1. Make sure you have setuptools installed
1. In the secret_santa directory run `python setup.py test` (this will give you coverage as well)
