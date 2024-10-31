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

## Running the lectures on Google Colab

 - [Lecture 1](https://colab.research.google.com/github/simonpf/at652/blob/main/notebooks/introduction.ipynb)
 - [Example 1: MLP precipitation retrieval](https://colab.research.google.com/github/simonpf/at652/blob/main/notebooks/precipitation_retrieval_mlp.ipynb)
 - [Lecture 2](https://colab.research.google.com/github/simonpf/at652/blob/main/notebooks/introduction.ipynb)
 - [Example 2: U-net precipitation retrieval](https://colab.research.google.com/github/simonpf/at652/blob/main/notebooks/precipitation_retrieval_unet.ipynb)
