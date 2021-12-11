# https://blog.csdn.net/Bit_Coders/article/details/121561632
from paddleocr import PaddleOCR  # , draw_ocr

import os
# fix error: OMP: Error #15: Initializing libiomp5md.dll, but found libiomp5md.dll already initialized.
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

# Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
# 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
ocr = PaddleOCR(use_angle_cls=True, lang="ch") # need to run only once to download and load model into memory

for line in ocr.ocr('chinese_test.png', cls=True):
    print(line)
