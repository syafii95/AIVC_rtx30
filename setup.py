"""import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["MvImport","pyqt5","tensorboard.summary","cv2","wrapt","absl","gast",\
"astor","termcolor","opt_einsum","google.protobuf","matplotlib","os", "tensorflow", "numpy", "PIL","darknet","ctypes"],\
 "include_files": ["core", "color_mask_threshold.txt", "data","classes.names", "Login.ini", "aivcMonitor","lib","coco.data","yolo_cpp_dll.dll"],  \
 "excludes": ["matplotlib.tests", "numpy.random._examples"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
# if sys.platform == "win32":
#     base = "Win32GUI"

setup(  name = "AIVC",
        version = "2.3.63.0",
        description = "AIVC 2",
        author = "Syafii",
        options = {"build_exe": build_exe_options},
        executables = [Executable("AIVC.py", base=base, icon='utils/icons/TG_icon.ico')])
"""

import sys
import os
from cx_Freeze import setup, Executable
files = ["core", "color_mask_threshold.txt", "data","classes.names", "Login.ini", "aivcMonitor","lib","coco.data","yolo_cpp_dll.dll","yolov3.cfg","zlibwapi.dll","yolov3_glove.weights","cublas64_10.dll","cublasLt64_10.dll","cudart64_101.dll","cudnn64_7.dll","cufft64_10.dll","curand64_10.dll","cusolver64_10.dll","cusparse64_10.dll","config.json","mkl_core.dll","mkl_def.dll","mkl_intel_thread.dll","mkl_mc3.dll"]
exFiles = ["matplotlib.tests", "numpy.random._examples"]

target = Executable(
    script="AIVC.py",
    base=None,
    icon='utils/icons/TG_icon.ico'
)

setup(
    name = "AIVC",
    version = "2.3.63.0",
    description = "AIVC 2",
    author = "Syafi'i",
    options = {'build_exe' : {'include_files' : files , 'excludes' : exFiles}},
    executables = [target]
)
