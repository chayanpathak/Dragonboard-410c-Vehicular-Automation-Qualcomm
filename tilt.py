import ctypes
my_test_lib=ctypes.cdll.LoadLibrary('/home/linaro/tilt.so')
my_test_lib.main()


