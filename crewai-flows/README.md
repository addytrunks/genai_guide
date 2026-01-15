# Project Setup

This project requires certain dependencies to be installed for proper functioning. Follow the instructions below to set up your environment.

## Conda Environment

To create a conda environment with Python 3.12, use the following command:

conda create --name crewai-flows python=3.12

To activate the conda environment, use:

conda activate crewai-flows

## Virtualenv

If you prefer using virtualenv, first install it:

pip install virtualenv

Then create a virtual environment with Python 3.12:

virtualenv -p python3.12 myenv

Activate the virtualenv environment with:

- On Windows: myenv\Scripts\activate
- On macOS/Linux: source myenv/bin/activate

## Installing Dependencies

To install the dependencies listed in the `requirements.txt` file, use:

pip install -r requirements.txt
