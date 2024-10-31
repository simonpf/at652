# Machine Learning for Remote Sensing

This document contains the slides for the short course on "Machine Learning for Remote Sensing" given as part of AT652 at the Deparment of Atmospheric Science at Colorado State University.

## Overview

The course is is designed to teach both theoretical and practical basics of modern machine learning techniques applied to remote sensing observations. To this end, the course has been designed using Jupyter Notebooks. The provided code can be executed interactively and aims to illustrate the theoretical concepts introduced in the course and serve as a basis for the student's own exploration of the topics.

## Following along with the lectures

### On your own machine 

All lecture content is available from the github repository [https://github.com/simonpf/at652](https://github.com/simonpf/at652). 

To download a copy of the notebooks execute the following in a terminal.

``` 
git clone https://github.com/simonpf/at652
```

Running the interactive lecture slides requires installing a limited number of Python packages. In order to avoid conflicts with the existing compute environment it is recommeded to create a new conda environment and install the dependencies in there.

```
conda create --name at652 python=3.11
conda activate at652
```

Finally, all necessary packages can be installed by installing the ``at652`` package as follows.

```
cd at652
pip install .
```

You can then launch a Jupyter Lab. The lecture slides are contained in the ``notebooks`` folder.

### On Goolge Colab

You can use the following link to follow along with the lecuters on Google Colab:


 - [Lecture 1](https://colab.research.google.com/github/simonpf/at652/blob/main/notebooks/introduction.ipynb)
 - [Example 1: MLP precipitation retrieval](https://colab.research.google.com/github/simonpf/at652/blob/main/notebooks/precipitation_retrieval_mlp.ipynb)
 - [Lecture 2](https://colab.research.google.com/github/simonpf/at652/blob/main/notebooks/introduction.ipynb)
 - [Example 2: U-net precipitation retrieval](https://colab.research.google.com/github/simonpf/at652/blob/main/notebooks/precipitation_retrieval_unet.ipynb)
