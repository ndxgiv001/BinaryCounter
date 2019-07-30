#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: Given Ndou
Student Number: ndxgiv001
Prac: 1
Date: 28/07/2019
"""

# import Relevant Librares
import RPi.GPIO as GPIO




def main():
GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(8,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(12,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(10,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    #GPIO.add_event_detect(16,GPIO.RISING,callback=button_callback)
    GPIO.add_event_detect(16, GPIO.FALLING, callback=button_callback,bouncetime=300)
    
    GPIO.add_event_detect(18,GPIO.RISING,callback=button_callback2,bouncetime=300)
    


# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        #while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except Exception as e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
