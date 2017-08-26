from GPIOlibrary import GPIOProcessor
import time


GP= GPIOProcessor()

#Pin23=GP.getPin23()
#Pin25=GP.getPin25()
Pin33=GP.getPin33()
Pin31=GP.getPin31()
Pin32=GP.getPin32()
Pin34=GP.getPin34()
Pin30=GP.getPin30()

#Pin23.out()
#Pin25.out()
Pin33.out()
Pin31.out()
Pin32.out()
Pin34.out()
Pin30.out()


#def car_start():
#		Pin23.high()
#		Pin25.high()
#		print 12
		#time.sleep(10)	
   	

	
#def car_stop():
#		Pin23.low()
#		Pin25.low()	
'''  	
def viper_on():
		for i in range(3):
			Pin23.low()
			Pin25.high()
			time.sleep(1)
			Pin23.high()
			Pin25.low()
			time.sleep(1)
		Pin23.low()
		Pin25.low()
'''
def left_wind_shield_up(left):
				if(left==0):
					Pin33.low()
					Pin31.high()
					time.sleep(5)
					Pin33.low()
					Pin31.low()
					return 1
				else:
					return 1

def left_wind_shield_down(left):
			if(left==1):
				Pin33.high()
				Pin31.low()
				time.sleep(5)
				Pin33.low()
				Pin31.low()			
				return 0
			else:
  				return 0
	
def right_wind_shield_up(right):
				if(right==0):
					Pin32.low()
					Pin34.high()
					time.sleep(1.5)
					Pin32.low()
					Pin34.low()
					return 1
				else:
					return 1

def right_wind_shield_down(right):
			if(right==1):
				Pin32.high()
				Pin34.low()
				time.sleep(1.5)
				Pin32.low()
				Pin34.low()			
				return 0
			else:
  				return 0
	
def head_light():
		Pin30.high()
		sleep(5)
		Pin30.low()
		
def cleanup():
			GP.cleanup()

