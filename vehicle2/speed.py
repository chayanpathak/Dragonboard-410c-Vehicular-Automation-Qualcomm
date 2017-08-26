def speed():
	print "Enter the speed value:",
	present_speed = raw_input().strip()
	present_speed = int(present_speed)
	if present_speed > 60:
		return 1
	else:
		return 0

		
	