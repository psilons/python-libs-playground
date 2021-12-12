# Python Library Playground

Besides commonly used libraries in the enterprise world, here are the collections of other 
interesting libraries.

## Install Python

To install from environment.yml:
- `conda deactivate`
- `conda update -n base -c defaults conda`
- `conda env create -f environment.yml`
- `conda info --envs`

To remove this environment: 
- ```conda env remove -n python_libs_playground```
- remove the directory in the file system.

These 2 libs for Chinese OCR are not compatible with conda, so install them manually
via pip on the command line.
- paddlepaddle
- paddleocr 

To activate the environment: `conda activate python_libs_playground`

