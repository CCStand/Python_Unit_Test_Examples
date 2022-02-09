# Python_Unit_Test_Examples
*Examples of Python unit testing.*

## Video learning
You might find some of these resources useful for learning more about the tech used in this repo:
* [Poetry](https://www.youtube.com/watch?v=6ey-nNRvBrk)
* [Pytest](https://www.lambdatest.com/blog/end-to-end-tutorial-for-pytest-fixtures-with-examples/)
* [Hypothesis](https://www.hillelwayne.com/talks/beyond-unit-tests/)

## Set up with Poetry
This repo uses Poetry to manage package dependencies. You can follow these steps to set-up your own repos with Poetry (you won't need to do this for this repo as it's already been done):
* [Install poetry](https://python-poetry.org/docs/#installation)
```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```
* [Create a new Poetry repo](https://python-poetry.org/docs/basic-usage/#project-setup) **or** [Initialise Poetry in an existing repo](https://python-poetry.org/docs/basic-usage/#initialising-a-pre-existing-project)
```
poetry new [repo_name]
```
**or**
```
poetry init
```
* [Add any required packages to `pyproject.toml`](https://python-poetry.org/docs/basic-usage/#specifying-dependencies)
```
poetry add pytest
poetry add jupyter
poetry add ipykernel
...
```
* [Lock in packages as specified in `pyproject.toml`](https://python-poetry.org/docs/basic-usage/#installing-dependencies)
```
poetry install
```


## Running the code
If you want to open this repo in Jupyter, you will need to:
* Create a kernel for this environment to use in Jupyter 
```
poetry run python -m ipykernel install --user --name=[kernel_name]
```
* Run Jupyter within Poetry
```
poetry run jupyter notebook
```
* Select that kernel in the Jupyter notebook to use it


If you want to run pytest or individual scripts, simply run on top of the `poetry` command, e.g.
```
poetry run pytest
```
