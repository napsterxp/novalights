from time import sleep
from definitions import *
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

state = "startup"
count = 0

try:
	while True:
		#state = "off"
				
		##Silence Detector
		if GPIO.input(21) == GPIO.LOW:
                    redflash()
                    state = "silence"
                    count = 0
                    sleep(15)
                    
                ##Off Combos
		elif GPIO.input(23) == GPIO.LOW and GPIO.input(24) == GPIO.LOW:()
		elif GPIO.input(23) == GPIO.LOW and GPIO.input(20) == GPIO.LOW:()
		elif GPIO.input(23) == GPIO.LOW and GPIO.input(16) == GPIO.LOW:()
		
		##Mic and Door
		elif GPIO.input(24) == GPIO.LOW and GPIO.input(20) == GPIO.LOW and (state) != 'doorbell':
                    yellow()
                    state = "doorbell"
                    count = 0
		elif GPIO.input(24) == GPIO.LOW and GPIO.input(20) == GPIO.LOW and (state) == 'doorbell':()
		
		##Mic and Phone
		elif GPIO.input(24) == GPIO.LOW and GPIO.input(16) == GPIO.LOW and (state) != 'phone':
                    greenflash()
                    state = "phone"
                    count = 0
                    sleep (15)
		elif GPIO.input(24) == GPIO.LOW and GPIO.input(16) == GPIO.LOW and (state) == 'phone':()		
	

                ##Mic
		elif GPIO.input(24) == GPIO.LOW and (state) != 'mic live':
                    red()
                    state = "mic live"
		    print("Mic Live")
                    count = 0
                
                ##Door
		elif GPIO.input(20) == GPIO.LOW and (state) != 'doorbell':
                    yellow()
                    state = "doorbell"
                    count = 0

                ##Phone
		elif GPIO.input(16) == GPIO.LOW and (state) != 'phone':
                    greenflash()
                    state = "phone"
                    count = 0
                    sleep(15)

                ##Cleaner
		#elif GPIO.input(25) == GPIO.LOW and (parse) != 'cleaner':
                    #white()
                    #state.seek(0)
                    #state.truncate()
                    #state.write("cleaner")
                    #print ("CLEANER")

                ##OFF
		#elif GPIO.input(23) == GPIO.LOW and (state) != 'off':
                    #off()
                    #state = "off"
                    #count = 0

		elif GPIO.input(23) == GPIO.LOW and (state) == 'off':()
		elif GPIO.input(25) == GPIO.LOW and (state) == 'cleaner':()
		elif GPIO.input(16) == GPIO.LOW and (state) == 'phone':()
		elif GPIO.input(20) == GPIO.LOW and (state) == 'doorbell':()
		elif GPIO.input(24) == GPIO.LOW and (state) == 'mic live':()
		

				
		elif (state) != 'off':
                    blue()
		    print("blue")
                    state = "off"
                    count = 0
		
		##AutoSleep
		elif count > 7200 and count < 7202:
		    off()

                #Auto Sleep
		count = count +1
		sleep(0.5)
		






finally:
    print ("got to the end now")
