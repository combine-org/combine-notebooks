.. image:: https://raw.githubusercontent.com/combine-org/combine-notebooks/main/docs/images/combine.png
   :align: left
   :alt: COMBINE logo

combine-notebooks - COMBINE jupyter notebooks in python
=======================================================

.. image:: https://github.com/combine-org/combine-notebooks/workflows/CI-CD/badge.svg
   :target: https://github.com/combine-org/combine-notebooks/workflows/CI-CD
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
`COMBINE <http://co.mbine.org/standards>`__ standards and their libraries around one common theme; the repressilator model.

.. image:: https://img.shields.io/badge/Blogger-FF5722?style=for-the-badge&logo=blogger&logoColor=white
   :target: https://combine-notebooks-gsoc-2022.blogspot.com/
   :alt: Blogger

The following standards are demonstrated

- Systems Biology Graphical Notation (`SBGN <https://sbgn.github.io/>`__): Used to describe visually biological knowledge.
- Systems Biology Markup Language (`SBML <https://sbgn.github.io/>`__): Used for representing models of biological processes.
- Simulation Experiment Description Markup Language (`SED-ML <https://sed-ml.org/>`__): Used for encoding experiments. SED-ML allows defining the models to use, the experimental tasks to run, and which results to produce. It is a computer-readable format for representing the models of biological processes.
- `CellML <https://www.cellml.org/>`__: Used to store and exchange computer-based mathematical models.
- Synthetic Biology Open Language (`SBOL <https://sbolstandard.org/>`__): Used for description and the exchange of synthetic biological parts, devices, and systems.
- `NeuroML <https://neuroml.org/>`__: Used for XML based description language that provides a common data format for defining and exchanging descriptions of neuronal cell and network models.

Setup/Installation
------------------

To work with the notebooks create a virtual environment and install the dependencies::

    mkvirtualenv combine_notebooks --python=python3.10
    (combine_notebooks) pip install -e .[development] --upgrade


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