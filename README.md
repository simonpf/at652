# AT652: Machine learning for remote sensing

This repository contains the lecture slides and source code for the "Machine Learning for Remote Sensing" lectures of AT652.

## Setting up your compute environment

### Obtain the lecture notebooks

``` shellsession
git clone https://github.com/simonpf/at652
```

### Create a new conda environment

In order to run the interactive lecture slides, you will need to install a limited number of Python packages. In order to avoid conflicts with the existing compute environment it is recommeded to create a new conda environment and install the dependencies in there.

``` shellsession
conda create --name at652 python=3.11
conda activate at652
```

### Install the at652 package.

``` shellsession
cd at652
pip install .
```
