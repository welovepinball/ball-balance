
try:
    import RPi.GPIO as GPIO
except:
    print ("Could not import RPi.GPIO")
    
import config as c


# Sets up GPIO pins and motors - DO NOT MODIFY
try:
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(c.l_motor_rpi_pin, GPIO.OUT)
    GPIO.setup(c.r_motor_rpi_pin, GPIO.OUT)
    left_servo=GPIO.PWM(c.l_motor_rpi_pin,50)
    right_servo=GPIO.PWM(c.r_motor_rpi_pin,50)
except:
    print ("Could not set up motors.")

#DO NOT MODIFY
#Formula to drive motors - input "right" or "left" and direction/speed
#The midpoint (stoping point) for the continuous motor is 7.5
#Full speed one direction is 5 (min) and full speed the other direction is 10 (max)
#Slower speeds are acheivable at values between midpoint and min/max.
#direction_speed equals 7.5 plus or minus the speed set in motor_speed variable.

def move_motor(left_right, direction_speed):
    if left_right == "right":
        try:
            right_servo.start(direction_speed)
        except:
            print ("Could not move/stop right motor.")
    elif left_right == "left":
        try:
            left_servo.start(direction_speed)
        except:
            print ("Could not move/stop left motor.")
    else:
        print (left_right + " is not a valid entry for left_right in the move_motor function.  Only left and right can be entered.")
        
