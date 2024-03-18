# Copyright (C) 2020  Davis E. King (davis@dlib.net)
# License: Boost Software License   See LICENSE.txt for the full license.

def add_lib_to_dll_path(path):
    """ On windows you must call os.add_dll_directory() to allow linking to external DLLs.  See
    https://docs.python.org/3.8/whatsnew/3.8.html#bpo-36085-whatsnew.  This function adds the folder
    containing path to the dll search path. 
    """
    try:
        import os
        os.add_dll_directory(os.path.join(os.path.dirname(path), '../../bin'))
    except (AttributeError,KeyError,FileNotFoundError):
        pass

if 'ON' == 'ON':
    add_lib_to_dll_path('/usr/lib/x86_64-linux-gnu/libcudnn.so')
    add_lib_to_dll_path('/usr/local/cuda/lib64/libcudart.so')

from _dlib_pybind11 import *
from _dlib_pybind11 import __version__, __time_compiled__