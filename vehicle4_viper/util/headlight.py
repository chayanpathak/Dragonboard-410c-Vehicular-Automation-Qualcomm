from GPIOlibrary import GPIOProcessor
import time


def head_light():
		GP= GPIOProcessor()

		Pin24=GP.getPin24()
		Pin24.out()
		Pin24.high()
		time.sleep(5)
		GP.cleanup()	

