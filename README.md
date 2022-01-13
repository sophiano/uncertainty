
# Uncertainty

Uncertainty is a module written in Python to study the sunspot numbers.

It is composed of functions that compute robust estimators for the number of sunspots (Ns), the number of sunspot groups (Ng) and the composite (Nc=Ns+10Ng). 
It also contains functions to estimate three types errors that corrupt the observations at short term, long-term time scale and solar minima.

This package was written by Sophie Mathieu (UCLouvain/Royal Observatory of Belgium). 

## Installation 

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install uncertainty:

````
pip install git+https://gitlab-as.oma.be/SIDC/SILSO_USET/valusun_group/sunspot_numbers/uncertainty.git
````


## Folder contents

* **uncertainty** <br>
The main functions of the package are contained in the folder uncertainty.

* **data** <br>
The data are composed of the number of sunspots (Ns), the number of sunspot groups (Ng) and the composite (Nc=Ns+10Ng). 
They are provided into zip, txt and serialized format (pickling).

* **docs** <br>
This folder contains the doumentation of the package in the form of Jupyter notebooks. 

* **scripts** <br>
This folder contains the scripts of the package.

## References

* Mathieu, S., von Sachs, R., Delouille, V., Lefèvre, L. & Ritter, C. (2019).
_Uncertainty quantification in sunspot counts_. The Astrophysical Journal, 886(1):7. Available on [arXiv](https://arxiv.org/abs/2009.09810).

## License
[MIT](https://choosealicense.com/licenses/mit/)



