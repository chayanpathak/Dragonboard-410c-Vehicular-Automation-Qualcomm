import ctypes
my_test_lib=ctypes.cdll.LoadLibrary('/home/linaro/slide.so')
my_test_lib.main()


