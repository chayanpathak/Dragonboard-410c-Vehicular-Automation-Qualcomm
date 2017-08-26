import ctypes
from GPIOlibrary import GPIOProcessor

def security_on():

	GP= GPIOProcessor()


 	my_test_lib=ctypes.cdll.LoadLibrary('/home/linaro/touch.so')
	value=my_test_lib.main()
	if (value<2):
		print('NO SMS')
	else:
		print('SMS')

	GP.cleanup()
