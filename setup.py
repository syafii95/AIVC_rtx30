import sys
import os
from cx_Freeze import setup, Executable
files = ["core", "color_mask_threshold.txt", "data","classes.names", "Login.ini", "aivcMonitor","lib","yolo_cpp_dll.dll","yolov3.cfg","zlibwapi.dll","yolov3_glove.weights","cublas64_10.dll","cublasLt64_10.dll","cudart64_101.dll","cudnn64_7.dll","cufft64_10.dll","curand64_10.dll","cusolver64_10.dll","cusparse64_10.dll","config.json","mkl_core.dll","mkl_def.dll","mkl_intel_thread.dll","mkl_mc3.dll"]
exFiles = ["matplotlib.tests", "numpy.random._examples"]

target = Executable(
    script="AIVC.py",
    base=None,
    icon='utils/icons/TG_icon.ico'
)

setup(
    name = "AIVC",
    version = "5.0.0.0",
    description = "AIVC 5.0 by Syafii",
    author = "Muhammad Syafi'i",
    options = {'build_exe' : {'include_files' : files , 'excludes' : exFiles}},
    executables = [target]
)
