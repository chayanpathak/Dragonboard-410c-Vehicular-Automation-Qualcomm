import ctypes
from GPIOlibrary import GPIOProcessor
from send_mail import send_mail
GP= GPIOProcessor()

my_test_lib=ctypes.cdll.LoadLibrary('/home/linaro/touch.so')
value=my_test_lib.main()
if (value<=5):
	print('\n          OWNER MISTAKENLY TOUCHED           NO EMAIL SENT\n')
else:
	print('\n          OWNER HAS REALISED THE THEFT.      EMAIL SENT \n')
	send_mail("Intruder alert")

GP.cleanup()
