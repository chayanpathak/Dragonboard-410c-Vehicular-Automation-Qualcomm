from GPIOlibrary import GPIOProcessor
import time


GP= GPIOProcessor()

Pin23=GP.getPin23()
Pin25=GP.getPin25()

Pin23.out()
Pin25.out()

 	
def viper_on():
		for i in range(3):
			Pin23.high()
			Pin25.low()
			time.sleep(1.5)
			Pin23.low()
			Pin25.high()
			time.sleep(1.5)
		

def cleanup():
		Pin23.low()
		Pin25.low()

		GP.cleanup()

viper_on()
cleanup()
GP.cleanup()
