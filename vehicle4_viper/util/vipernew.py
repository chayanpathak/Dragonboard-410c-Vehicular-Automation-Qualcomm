from GPIOlibrary import GPIOProcessor
import time



def viper_on():
		GP= GPIOProcessor()

		Pin23=GP.getPin23()
		Pin23.out()

		Pin23.high()
		time.sleep(5)
		Pin23.low()
		GP.cleanup()
			
		

#def cleanup():
#		Pin23.low()
#		GP.cleanup()


#viper_on()
#cleanup()
#GP.cleanup()
