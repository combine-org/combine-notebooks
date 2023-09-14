![COMBINE logo](https://raw.githubusercontent.com/combine-org/combine-notebooks/main/docs/images/combine.png)

# Examples of Jupyter notebooks demonstrating COMBINE standards

[![GitHub Actions CI/CD Status](https://github.com/combine-org/combine-notebooks/actions/workflows/main.yml/badge.svg)](https://github.com/combine-org/combine-notebooks/actions/workflows/main.yml)
[![Current PyPI Version](https://img.shields.io/pypi/v/combine-notebooks.svg)](https://pypi.org/project/combine-notebooks/)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/combine-notebooks.svg)](https://pypi.org/project/combine-notebooks/)
[![GNU Lesser General Public License 3](https://img.shields.io/pypi/l/combine-notebooks.svg)](http://opensource.org/licenses/LGPL-3.0)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)

## Project Overview

This repository contains Jupyter notebooks that showcase [COMBINE](http://co.mbine.org/standards) standards and their libraries.
Each of the standards has a simple "Hello world" example (demonstrating the core concepts of the format), or an example file building the [repressilator model](https://pubmed.ncbi.nlm.nih.gov/10659856/), or both.

This work was initially carried out as part of a Google Summer of Code 2022 project. See here for more details:

[![Blogger](https://img.shields.io/badge/Blogger-FF5722?style=for-the-badge&logo=blogger&logoColor=white)](https://combine-notebooks-gsoc-2022.blogspot.com/)

The following standards are demonstrated:

| Standard | Description | Basic Example | Repressilator Example |
|---|---|---|---|
| Systems Biology Graphical Notation ([SBGN](https://sbgn.github.io/)) | Used to describe visually biological knowledge. | [sbgn.ipynb](https://github.com/combine-org/combine-notebooks/blob/main/notebooks/sbgn.ipynb) | [example_sbgn.ipynb](https://github.com/combine-org/combine-notebooks/blob/main/notebooks/example_sbgn.ipynb) |
| Systems Biology Markup Language ([SBML](https://sbml.org/)) | Used for representing models of biological processes. | [sbml.ipynb](https://github.com/combine-org/combine-notebooks/blob/main/notebooks/sbml.ipynb) | [example_sbml_libsbml.ipynb](https://github.com/combine-org/combine-notebooks/blob/main/notebooks/example_sbml_libsbml.ipynb) |
| Simulation Experiment Description Markup Language ([SED-ML](https://sed-ml.org/)) | Used for encoding experiments. SED-ML allows defining the models to use, the experimental tasks to run, and which results to produce. It is a computer-readable format for representing the models of biological processes. | [sedml.ipynb](https://github.com/combine-org/combine-notebooks/blob/main/notebooks/sedml.ipynb) | [example_sedml.ipynb](https://github.com/combine-org/combine-notebooks/blob/main/notebooks/example_sedml.ipynb) |
| [CellML](https://www.cellml.org/) | Used to store and exchange computer-based mathematical models. | [cellml.ipynb](https://github.com/combine-org/combine-notebooks/blob/main/notebooks/cellml.ipynb) [View on Binder](https://mybinder.org/v2/gh/combine-org/combine-notebooks/main?labpath=notebooks%2Fcellml.ipynb) [(Dev version)](https://mybinder.org/v2/gh/combine-org/combine-notebooks/development?labpath=notebooks%2Fcellml.ipynb) | [example_cellml.ipynb](https://github.com/combine-org/combine-notebooks/blob/main/notebooks/example_cellml.ipynb) |
| Synthetic Biology Open Language ([SBOL](https://sbolstandard.org/)) | Used for description and the exchange of synthetic biological parts, devices, and systems. | [sbol.ipynb](https://github.com/combine-org/combine-notebooks/blob/main/notebooks/sbol.ipynb) | - |
| [NeuroML](https://neuroml.org/) | An XML based description language that provides a common data format for defining and exchanging descriptions of neuronal cell and network models. | [neuroml.ipynb](https://github.com/combine-org/combine-notebooks/blob/main/notebooks/neuroml.ipynb) [View on Binder](https://mybinder.org/v2/gh/combine-org/combine-notebooks/main?labpath=notebooks%2Fneuroml.ipynb) [(Dev version)](https://mybinder.org/v2/gh/combine-org/combine-notebooks/development?labpath=notebooks%2Fneuroml.ipynb) | - |
| [COMBINE Archive](https://combinearchive.org/index/) | Used to bundle the various documents necessary for a modelling and simulation project, and all relevant information. | [omex.ipynb](https://github.com/combine-org/combine-notebooks/blob/main/notebooks/omex.ipynb) | [example_omex.ipynb](https://github.com/combine-org/combine-notebooks/blob/main/notebooks/example_omex.ipynb) |
| Biological Pathway Exchange ([BioPAX](http://www.biopax.org/)) | Used to enable integration, exchange and analysis of biological pathway data. | - | [example_biopax.ipynb](https://github.com/combine-org/combine-notebooks/blob/main/notebooks/example_biopax.ipynb) |


## Setup/Installation

To work with the notebooks, create a virtual environment and install the dependencies:

    mkvirtualenv combine_notebooks --python=python3.10
    (combine_notebooks) pip install -e .[development] --upgrade

To setup pre-commit hooks (optional) run the following command:

    pre-commit install

After changes ensure code formatting via:

    ./fcode.sh

Tests can be run via pytest and tox. To run all tests use:

    tox -p

To run individual tests use the following targets: flake8, mypy, py38, py39, py310:

    tox -e flake8

## Notebooks

To run the notebooks install a notebook environment:

    pip install jupyterlab

Register the created virtual environment [combine_notebooks]{.title-ref}
as jupyter kernel:

    ipython kernel install --user --name=combine_notebooks

Or alternatively install the package in an existing virtual environment
to get all the dependencies. I.e.:

    pip install combine-notebooks

Start the notebooks:

    cd ./notebooks
    jupyter lab

© 2022-2023 Matthias König & Aditya Singhal and [contributors](https://github.com/combine-org/combine-notebooks/graphs/contributors).

