from time import sleep
from leddefinitions import *
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)



try:
	while True:
		state = open("status.txt", "r+")
		parse = state.read()
		
		##Silence Detector
		if GPIO.input(21) == GPIO.LOW:
                    redflash()
                    state.seek(0)
                    state.truncate()
                    state.write("silence")
                    print ("SILENCE DETECTED")
                    
                ##Off Combos
		elif GPIO.input(23) == GPIO.LOW and GPIO.input(24) == GPIO.LOW:()
		elif GPIO.input(23) == GPIO.LOW and GPIO.input(20) == GPIO.LOW:()
		elif GPIO.input(23) == GPIO.LOW and GPIO.input(16) == GPIO.LOW:()
		
		##Mic and Door
		elif GPIO.input(24) == GPIO.LOW and GPIO.input(20) == GPIO.LOW and (parse) != 'doorbell':
                    yellow()
                    state.seek(0)
                    state.truncate()
                    state.write("doorbell")
                    print ("staying on bell")
		elif GPIO.input(24) == GPIO.LOW and GPIO.input(20) == GPIO.LOW and (parse) == 'doorbell':()
		
		##Mic and Phone
		elif GPIO.input(24) == GPIO.LOW and GPIO.input(16) == GPIO.LOW and (parse) != 'phone':
                    greenflash()
                    state.seek(0)
                    state.truncate()
                    state.write("phone")
                    print ("staying on phone")
		elif GPIO.input(24) == GPIO.LOW and GPIO.input(16) == GPIO.LOW and (parse) == 'phone':()		
	

                ##Mic
		elif GPIO.input(24) == GPIO.LOW and (parse) != 'mic live':
                    red()
                    state.seek(0)
                    state.truncate()
                    state.write("mic live")
                    print ("GOING RED")
                
                ##Door
		elif GPIO.input(20) == GPIO.LOW and (parse) != 'doorbell':
                    yellow()
                    state.seek(0)
                    state.truncate()
                    state.write("doorbell")
                    print ("DOOR")

                ##Phone
		elif GPIO.input(16) == GPIO.LOW and (parse) != 'phone':
                    greenflash()
                    state.seek(0)
                    state.truncate()
                    state.write("phone")
                    print ("PHONE")

                ##Cleaner
		elif GPIO.input(25) == GPIO.LOW and (parse) != 'cleaner':
                    white()
                    state.seek(0)
                    state.truncate()
                    state.write("cleaner")
                    print ("CLEANER")

                ##OFF
		elif GPIO.input(23) == GPIO.LOW and (parse) != 'off':
                    dbo()
                    state.seek(0)
                    state.truncate()
                    state.write("off")
                    print ("off")

		elif GPIO.input(23) == GPIO.LOW and (parse) == 'off':()
		elif GPIO.input(25) == GPIO.LOW and (parse) == 'cleaner':()
		elif GPIO.input(16) == GPIO.LOW and (parse) == 'phone':()
		elif GPIO.input(20) == GPIO.LOW and (parse) == 'doorbell':()
		elif GPIO.input(24) == GPIO.LOW and (parse) == 'mic live':()
		

				
		elif (parse) != 'rest':
                    blue()
                    state.seek(0)
                    state.truncate()
                    state.write("rest")
                    print ("Returning to blue")
		state.close()
		sleep(0.5)






finally:
    print ("got to the end now")
