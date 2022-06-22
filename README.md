# combine-notebooks

## Project Overview

This repository contains Jupyter notebooks that showcase [COMBINE](http://co.mbine.org/standards) standards and their libraries around one common theme; the repressilator model.

## COMBINE Standards

- Systems Biology Graphical Notation ([SBGN](https://github.com/sbgn/libsbgn)): Used to describe visually biological knowledge.
- Systems Biology Markup Language ([SBML](https://github.com/sbmlteam/libsbml)): Used for representing models of biological processes.
- Simulation Experiment Description Markup Language ([SED-ML](https://github.com/fbergmann/libSEDML)): Used for encoding experiments. SED-ML allows defining the models to use, the experimental tasks to run, and which results to produce. It is a computer-readable format for representing the models of biological processes.
- [CellML](https://github.com/cellml/libcellml): Used to store and exchange computer-based mathematical models.
- Synthetic Biology Open Language ([SBOL](https://github.com/SynBioDex/pySBOL3)): Used for description and the exchange of synthetic biological parts, devices, and systems.
- [NeuroML](https://github.com/NeuroML/pyNeuroML): Used for XML based description language that provides a common data format for defining and exchanging descriptions of neuronal cell and network models.

## Setup/Installation

To work with the notebooks create a virtual environment and install the dependencies

``` 
mkvirtualenv combine_notebooks --python=python3.9
pip install -e .[development] --upgrade
```