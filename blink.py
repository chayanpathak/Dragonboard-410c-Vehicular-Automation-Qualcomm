import ctypes
my_test_lib=ctypes.cdll.LoadLibrary('/home/linaro/blink.so')
my_test_lib.main()


