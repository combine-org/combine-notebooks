.. image:: https://raw.githubusercontent.com/combine-org/combine-notebooks/main/docs/images/combine.png
   :align: left
   :alt: COMBINE logo
 
combine-notebooks - COMBINE jupyter notebooks in python
=======================================================

.. image:: https://github.com/combine-org/combine-notebooks/actions/workflows/main.yml/badge.svg
   :target: https://github.com/combine-org/combine-notebooks/actions/workflows/main.yml
   :alt: GitHub Actions CI/CD Status

.. image:: https://img.shields.io/pypi/v/combine-notebooks.svg
   :target: https://pypi.org/project/combine-notebooks/
   :alt: Current PyPI Version

.. image:: https://img.shields.io/pypi/pyversions/combine-notebooks.svg
   :target: https://pypi.org/project/combine-notebooks/
   :alt: Supported Python Versions

.. image:: https://img.shields.io/pypi/l/combine-notebooks.svg
   :target: http://opensource.org/licenses/LGPL-3.0
   :alt: GNU Lesser General Public License 3

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/ambv/black
   :alt: Black

.. image:: http://www.mypy-lang.org/static/mypy_badge.svg
   :target: http://mypy-lang.org/
   :alt: mypy

Project Overview
----------------
This repository contains Jupyter notebooks that showcase
`COMBINE <http://co.mbine.org/standards>`__ standards and their libraries.  Each of the standards has a simple hello world example, or a repressilator model example, or both.

.. image:: https://img.shields.io/badge/Blogger-FF5722?style=for-the-badge&logo=blogger&logoColor=white
   :target: https://combine-notebooks-gsoc-2022.blogspot.com/
   :alt: Blogger

The following standards are demonstrated

.. list-table:: 
   :widths: 30 30 30 30
   :header-rows: 1

   * - Standard
     - Description
     - Basic Example
     - Repressilator Example
   * - Systems Biology Graphical Notation (`SBGN <https://sbgn.github.io/>`__)
     - Used to describe visually biological knowledge.
     - `sbgn.ipynb <https://github.com/combine-org/combine-notebooks/blob/main/notebooks/sbgn.ipynb>`__
     - `example_sbgn.ipynb <https://github.com/combine-org/combine-notebooks/blob/main/notebooks/example_sbgn.ipynb>`__
   * - Systems Biology Markup Language (`SBML <https://sbml.org/>`__)
     - Used for representing models of biological processes.
     - `sbml.ipynb <https://github.com/combine-org/combine-notebooks/blob/main/notebooks/sbml.ipynb>`__
     - `example_sbml_libsbml.ipynb <https://github.com/combine-org/combine-notebooks/blob/main/notebooks/example_sbml_libsbml.ipynb>`__
   * - Simulation Experiment Description Markup Language (`SED-ML <https://sed-ml.org/>`__)
     - Used for encoding experiments. SED-ML allows defining the models to use, the experimental tasks to run, and which results to produce. It is a computer-readable format for representing the models of biological processes.
     - `sedml.ipynb <https://github.com/combine-org/combine-notebooks/blob/main/notebooks/sedml.ipynb>`__
     - `example_sedml.ipynb <https://github.com/combine-org/combine-notebooks/blob/main/notebooks/example_sedml.ipynb>`__
   * - `CellML <https://www.cellml.org/>`__
     - Used to store and exchange computer-based mathematical models.
     - `cellml.ipynb <https://github.com/combine-org/combine-notebooks/blob/main/notebooks/cellml.ipynb>`__
     - `example_cellml.ipynb <https://github.com/combine-org/combine-notebooks/blob/main/notebooks/example_cellml.ipynb>`__
   * - Synthetic Biology Open Language (`SBOL <https://sbolstandard.org/>`__)
     - Used for description and the exchange of synthetic biological parts, devices, and systems.
     - `sbol.ipynb <https://github.com/combine-org/combine-notebooks/blob/main/notebooks/sbol.ipynb>`__
     - \-
   * - `NeuroML <https://neuroml.org/>`__
     - Used for XML based description language that provides a common data format for defining and exchanging descriptions of neuronal cell and network models.
     - `neuroml.ipynb <https://github.com/combine-org/combine-notebooks/blob/main/notebooks/neuroml.ipynb>`__
     - \-
   * - `COMBINE Archive <https://combinearchive.org/index/>`__
     - Used to bundle the various documents necessary for a modelling and simulation project, and all relevant information.
     - `omex.ipynb <https://github.com/combine-org/combine-notebooks/blob/main/notebooks/omex.ipynb>`__
     - `example_omex.ipynb <https://github.com/combine-org/combine-notebooks/blob/main/notebooks/example_omex.ipynb>`__
   * - Biological Pathway Exchange (`BioPAX <http://www.biopax.org/>`__)  
     - Used to enable integration, exchange and analysis of biological pathway data. 
     - \-
     - `example_biopax.ipynb <https://github.com/combine-org/combine-notebooks/blob/main/notebooks/example_biopax.ipynb>`__

Setup/Installation
------------------

To work with the notebooks create a virtual environment and install the dependencies::

    mkvirtualenv combine_notebooks --python=python3.10
    (combine_notebooks) pip install -e .[development] --upgrade


To setup pre-commit hooks (optional) run the following command::

    pre-commit install

After changes ensure code formatting via::

    ./fcode.sh


Tests can be run via pytest and tox. To run all tests use::

    tox -p

To run individual tests use the following targets `flake8`, `mypy`, `py38`, `py39`, `py310`::

    tox -e flake8


Notebooks
---------
To run the notebooks install a notebook environment::

    pip install jupyterlab

Register the created virtual environment `combine_notebooks` as jupyter kernel::

    ipython kernel install --user --name=combine_notebooks

Or alternatively install the package in an existing virtual environment to get all the dependencies. I.e.::

    pip install combine-notebooks

Start the notebooks::

    cd ./notebooks
    jupyter lab

© 2022 Matthias König & Aditya Singhal
