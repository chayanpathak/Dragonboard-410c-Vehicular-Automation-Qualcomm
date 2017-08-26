import ctypes
my_test_lib=ctypes.cdll.LoadLibrary('/home/linaro/new.so')
a=my_test_lib.main(65)
my_test_lib.printf("hello")
print (a)
