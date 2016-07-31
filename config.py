import pygame



# Switches

#opens controller config file, reads in values, and applies them to keys
control_config_file = open("control_config.txt", "r")

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



# Audio

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
