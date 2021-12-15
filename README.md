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

To install paddlepaddle, check [paddlepaddle.org.cn](https://www.paddlepaddle.org.cn/install/quick?docurl=/documentation/docs/zh/install/conda/windows-conda.html)

```conda install paddlepaddle==2.2.1 --channel https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/Paddle/```

These 2 libs for Chinese OCR are not compatible with conda, so install them manually
via pip on the command line.
- paddlepaddle
- paddleocr 

To activate the environment: `conda activate python_libs_playground`


## Python Libraries

### Utilities
- Console color print: https://github.com/willmcgugan/rich
- Progress bars: https://github.com/rsalmei/alive-progress
- https://github.com/tqdm/tqdm from https://blog.csdn.net/qq_36807888/article/details/121902791
- cloud client: https://pypi.org/project/free-storage/

### Graphviz
- https://pycallgraph.readthedocs.io/en/master/
- https://blog.csdn.net/qq_37177765/article/details/95886071
- https://blog.csdn.net/Bit_Coders/article/details/120722430
- Cyberbrain: https://blog.csdn.net/Px01Ih8/article/details/115257777
- https://graph-tool.skewed.de/

### Serialization
- https://github.com/marshmallow-code/marshmallow

### Configuration
- https://dzone.com/articles/run-hundreds-of-experiments-with-opencv-and-hydra
- Hydra: https://engineering.fb.com/open-source/hydra/
- Omegaconf: https://omegaconf.readthedocs.io/en/latest/usage.html#variable-interpolation
- https://gist.github.com/techtonik/2151727
- https://github.com/fzumstein/jsondiff

### SDLC
- https://realpython.com/pypi-publish-python-package/
- https://github.com/kyrus/python-junit-xml
- https://github.com/rubik/radon, SDLC metrics
- https://github.com/PyCQA/prospector


### Others
- https://github.com/vinta/awesome-python
- https://github.com/ml-tooling/best-of-python-dev
- https://tryolabs.com/blog/2020/12/21/top-10-python-libraries-of-2020
- https://www.infoworld.com/article/3008915/24-python-libraries-for-every-python-developer.html
- 
- Design Patterns: https://github.com/tylerlaberge/PyPattyrn
- https://stackabuse.com/creational-design-patterns-in-python/
- text to audio: https://github.com/formazione/pytextaudio
- 
- https://pypi.org/project/kelly-criterion/
