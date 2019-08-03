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
myList = [0]
#increment if the operand is plus, else decrement
def operator(oprtr):
    if(oprtr=="plus"):
        myList[0]=(myList[0]+1)%8
    else:
        if((myList[0]-1)<0):
            myList[0] = 7
        else:
            myList[0]=myList[0]-1
#this method is for blinking the leds
def blinkLeds():
    bitss = bin(myList[0]).zfill(4) # get 3 bit for every value
    bits=bitss.replace('b', '')
	
	#access all the bits generated
    firstBit =int(bits[-1])
    secBit=int(bits[-2])
    thirdBit=int(bits[-3])
    
    
    GPIO.output(8,firstBit)
    GPIO.output(10,secBit)
    GPIO.output(12,thirdBit)
#this method is a call back for decrementing
def button_callback2(channel):
    
    operator("minus")
    blinkLeds()	
#this method is a call back for incrementing
def button_callback(channel):
    blinkLeds()
    operator("plus")
#main method where execution starts
def main():
GPIO.setwarnings(False)

	#setup the pins to output/input
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(8,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(12,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(10,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    #GPIO.add_event_detect(16,GPIO.RISING,callback=button_callback)
	
	#set interrupts to detect when a button is clicked
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
