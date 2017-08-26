import ctypes
my_test_lib=ctypes.cdll.LoadLibrary('/home/linaro/sliding.so')
my_test_lib.main()


