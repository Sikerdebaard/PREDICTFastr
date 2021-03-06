[![Build Status](https://travis-ci.com/MStarmans91/WORC.svg?token=qyvaeq7Cpwu7hJGB98Gp&branch=master)](https://travis-ci.com/MStarmans91/WORC)

# WORC v3.0.0

## Workflow for Optimal Radiomics Classification

WORC is an open-source python package for the easy execution of full radiomics pipelines.

<img src="images/WORC.jpg" alt="Overview"/>

We aim to establish a general radiomics platform supporting easy integration of other tools. With our modular build
and support of different software languages (python, MATLAB, ruby, java etc.), we want to facilitate and stimulate
collaboration, standardisation and comparison of different radiomics approaches. By combining this in a single framework,
we hope to find a universal radiomics strategy that can address various problems.

## Disclaimer
This package is still under development. We try to thoroughly test and evaluate every new build and function, but
bugs can off course still occur. Please contact us through the channels below if you find any and we will try to fix
them as soon as possible, or create an issue on this Github.

## Tutorial and Documentation
The WORC tutorial is hosted in a [separate repository](https://github.com/MStarmans91/WORCTutorial).

The official documentation can be found at [https://worc.readthedocs.io](https://worc.readthedocs.io).

## Installation

WORC currently only supports Unix with Python 3.6+ (tested on 3.7.2 and 3.7.3) systems and
has been tested on Ubuntu 16.04 and 18.04 and Windows 10.

The package can be installed through pip:

      pip install WORC

Alternatively, you can directly install WORC from this repository:

      python setup.py install

Make sure you install the requirements first:

      pip install -r requirements.txt

### Fastr Configuration
The installation will create a FASTR configuration file in the $HOME/.fastr/config.d folder called WORC_config.py.
This file is used for configuring fastr, the pipeline execution toolbox we use. More information can be found at
[the FASTR website](http://fastr.readthedocs.io/en/stable/static/file_description.html#config-file).
In this file, so called mounts are defined, which are used to locate the WORC tools and your inputs and outputs.
Please inspect the mounts and change them if neccesary.

```
echo "machine images.xnat.org
>     login admin
>     password admin" > ~/.netrc
chmod 600 ~/.netrc
```

## 3rd-party packages used in WORC:

 - [FASTR (Workflow design and building)](http://fastr.readthedocs.io)
 - xnat (Collecting data from XNAT)
 - SimpleITK (Image loading and preprocessing)
 - [Pyradiomics](https://github.com/radiomics/pyradiomics)
 - [PREDICT](https://github.com/Svdvoort/PREDICTFastr)

See for other requirements the [requirements file](requirements.txt).

## Start
We suggest you start with the [WORC Tutorial](https://github.com/MStarmans91/WORCTutorial).
Besides a Jupyter notebook with instructions, we provide there also an example script for you to get started with.
Make sure you input your own data as the sources. Also, check out the unit tests of several tools in the
WORC/resources/fastr_tests directory. The example is explained in more detail in the  [documentation](https://worc.readthedocs.io).

## WIP
- We are working on improving the documentation.
- We are working on organizing clinically relevant datasets for examples and unit tests.
- We are writing the paper on WORC.

## License
This package is covered by the open source [APACHE 2.0 License](APACHE-LICENSE-2.0).

When using WORC, please cite this repository.

## Contact
We are happy to help you with any questions. Please sent us a mail or place an issue on the Github.

We welcome contributions to WORC. For the moment, converting your toolbox into a FASTR tool is satisfactory.

## Optional
Besides the default installation, there are several optional packages you could install to support WORC.

### Graphviz
WORC can draw the network and save it as a SVG image using [graphviz](https://www.graphviz.org/). In order to do so,
please make sure you install graphviz. On Ubuntu, simply run

      apt install graphiv

### Elastix
Image registration is included in WORC through [elastix and transformix](http://elastix.isi.uu.nl/).
In order to use elastix, please download the binaries and place them in your
fastr.config.mounts['apps'] path. Check the elastix tool description for the correct
subdirectory structure. For example, on Linux, the binaries and libraries should be in "../apps/elastix/4.8/install/"  and
"../apps/elastix/4.8/install/lib" respectively.

Note: optionally, you can tell WORC to copy the metadata from the image file
to the segmentation file before applying the deformation field. This requires
ITK and ITKTools: see  [the ITKTools github](https://github.com/ITKTools/ITKTools)
for installation instructions.

### XNAT
We use the XNATpy package to connect the toolbox to the XNAT online database platforms. You will only
need this when you want to download or upload data from or to XNAT. We advise you to specify
your account settings in a .netrc file when using this feature,  such that you do not need to input them on every request:
