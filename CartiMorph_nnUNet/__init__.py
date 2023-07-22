from __future__ import absolute_import

print("\n\nThis is a modified version of nnU-Net (1.7.0) tailored for the CartiMorph framework (https://github.com/YongchengYAO/CartiMorph).\n")
print("If you are using CartiMorph, please cite the paper: \n")
print("Yongcheng Yao, Junru Zhong, Liping Zhang, Sheheryar Khan, Weitian Chen.\n"
      "\"CartiMorph: a framework for automated knee articular cartilage morphometrics.\"\n"
      "Medical Image Analysis \(in progress\). \n\n")

print("Please also cite the following nnUNet paper: \n"
      "Isensee, F., Jaeger, P.F., Kohl, S.A.A. et al. \n "
      "\"nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation.\" \n"
      "Nat Methods (2020). https://doi.org/10.1038/s41592-020-01008-z \n\n")

from . import *

# set version
__version__ = '1.7.14'
