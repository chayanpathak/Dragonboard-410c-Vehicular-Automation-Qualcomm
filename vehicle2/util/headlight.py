from GPIOlibrary import GPIOProcessor
import time
GP= GPIOProcessor()

Pin24=GP.getPin24()
Pin24.out()

def head_light():
		Pin24.high()
		time.sleep(5)
		GP.cleanup()	

