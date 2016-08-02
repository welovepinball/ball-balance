import pygame

try:
    import RPi.GPIO as GPIO
except:
    print ("Could not import RPi.GPIO")


#########################################################################
# Switches
#########################################################################

#opens controller config file, reads in values, and applies them to keys
try:
    control_config_file = open(sys.path[0] + "\\" +"control_config.txt", "r")
except:
    control_config_file = open(sys.path[0] + "/" +"control_config.txt", "r")



keyinput = []
for line in control_config_file:
    line = line[line.find("=")+1:]
    line = line[:len(line)-1]
    #print (line)
    keyinput.append(int(line))

LEFT_JOY_UP=keyinput[0]
LEFT_JOY_DOWN=keyinput[1]
RIGHT_JOY_UP=keyinput[2]
RIGHT_JOY_DOWN=keyinput[3]
LEFT_LIMIT_TOP=keyinput[4]
LEFT_LIMIT_BOTTOM=keyinput[5]
RIGHT_LIMIT_TOP=keyinput[6]
RIGHT_LIMIT_BOTTOM=keyinput[7]
START_BUTTON=keyinput[8]
SERVICE_BUTTON=keyinput[9]
TILT_SWITCH=keyinput[10]
HOLE_1_SWITCH=keyinput[11]
HOLE_2_SWITCH=keyinput[12]
HOLE_3_SWITCH=keyinput[13]
HOLE_4_SWITCH=keyinput[14]
HOLE_5_SWITCH=keyinput[15]
HOLE_6_SWITCH=keyinput[16]
HOLE_7_SWITCH=keyinput[17]
HOLE_8_SWITCH=keyinput[18]
HOLE_9_SWITCH=keyinput[19]
HOLE_10_SWITCH=keyinput[20]
HOLE_FAILURE_SWITCH=keyinput[21]
    
control_config_file.close()

##LEFT_JOY_UP    = pygame.K_w
##LEFT_JOY_DOWN  = pygame.K_s
##RIGHT_JOY_UP   = pygame.K_UP
##RIGHT_JOY_DOWN = pygame.K_DOWN
##
##LEFT_LIMIT_TOP     = pygame.K_LEFTBRACKET
##LEFT_LIMIT_BOTTOM  = pygame.K_SEMICOLON
##RIGHT_LIMIT_TOP    = pygame.K_RIGHTBRACKET
##RIGHT_LIMIT_BOTTOM = pygame.K_QUOTE
##
##START_BUTTON = pygame.K_RETURN
##
##SERVICE_BUTTON = pygame.K_F1
##
##TILT_SWITCH = pygame.K_BACKSPACE
##
##HOLE_1_SWITCH  = pygame.K_1
##HOLE_2_SWITCH  = pygame.K_2
##HOLE_3_SWITCH  = pygame.K_3
##HOLE_4_SWITCH  = pygame.K_4
##HOLE_5_SWITCH  = pygame.K_5
##HOLE_6_SWITCH  = pygame.K_6
##HOLE_7_SWITCH  = pygame.K_7
##HOLE_8_SWITCH  = pygame.K_8
##HOLE_9_SWITCH  = pygame.K_9
##HOLE_10_SWITCH = pygame.K_0
##HOLE_FAILURE_SWITCH = pygame.K_x



#########################################################################
# Audio
#########################################################################

AUDIO_BONUS          = '../audio/bonus.wav'
AUDIO_EXTRA_BALL     = '../audio/extra-ball.wav'
AUDIO_FAILURE        = '../audio/failure.wav'
AUDIO_GAMEOVER       = '../audio/gameover.wav'
AUDIO_ROD_LEFT_DOWN  = '../audio/rod-left-down.wav'
AUDIO_ROD_LEFT_UP    = '../audio/rod-left-up.wav'
AUDIO_ROD_RIGHT_DOWN = '../audio/rod-right-down.wav'
AUDIO_ROD_RIGHT_UP   = '../audio/rod-right-up.wav'
AUDIO_SUCCESS        = '../audio/success.wav'
AUDIO_THEME          = '../audio/theme.wav'
AUDIO_TICK           = '../audio/tick.wav'
AUDIO_TILT           = '../audio/tilt.wav'
AUDIO_WIN            = '../audio/win.wav'


#########################################################################
# Motors
#########################################################################
# Change pin number to change the corresponding GPIO for the left and right motors.
l_motor_rpi_pin = 12
r_motor_rpi_pin = 40

# Set speed of motor between 0 (no motion) and 2.5 (max speed).
motor_speed = 2.5

# Sets up GPIO pins and motors - DO NOT MODIFY
try:
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(l_motor_rpi_pin, GPIO.OUT)
    GPIO.setup(r_motor_rpi_pin, GPIO.OUT)
    left_servo=GPIO.PWM(l_motor_rpi_pin,50)
    right_servo=GPIO.PWM(r_motor_rpi_pin,50)
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
        
