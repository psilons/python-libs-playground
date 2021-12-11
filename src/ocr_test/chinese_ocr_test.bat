REM To fix error: OMP: Error #15: Initializing libiomp5md.dll, but found libiomp5md.dll already initialized.
set KMP_DUPLICATE_LIB_OK=TRUE
REM this is installed from the python lib
paddleocr --image_dir chinese_test.png --use_angle_cls true --use_gpu false
