import pygame
import sys

#########################################################################
# Motors
#########################################################################
# Change pin number to change the corresponding GPIO for the left and right motors.
l_motor_rpi_pin = 12
r_motor_rpi_pin = 40

# Set speed of motor between 0 (no motion) and 2.5 (max speed).
motor_speed = 2.5



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
#### KEY LOOKUP
#########################################################################

def key_name_lookup(index_val):
    if index_val == 8:
        return "K_BACKSPACE"
    elif index_val == 9:
        return "K_TAB"
    elif index_val == 12:
        return "K_CLEAR"
    elif index_val == 13:
        return "K_RETURN"
    elif index_val == 19:
        return "K_PAUSE"
    elif index_val == 27:
        return "K_ESCAPE"
    elif index_val == 32:
        return "K_SPACE"
    elif index_val == 33:
        return "K_EXCLAIM"
    elif index_val == 34:
        return "K_QUOTEDBL"
    elif index_val == 35:
        return "K_HASH"
    elif index_val == 36:
        return "K_DOLLAR"
    elif index_val == 38:
        return "K_AMPERSAND"
    elif index_val == 39:
        return "K_QUOTE"
    elif index_val == 40:
        return "K_LEFTPAREN"
    elif index_val == 41:
        return "K_RIGHTPAREN"
    elif index_val == 42:
        return "K_ASTERISK"
    elif index_val == 43:
        return "K_PLUS"
    elif index_val == 44:
        return "K_COMMA"
    elif index_val == 45:
        return "K_MINUS"
    elif index_val == 46:
        return "K_PERIOD"
    elif index_val == 47:
        return "K_SLASH"
    elif index_val == 48:
        return "K_0"
    elif index_val == 49:
        return "K_1"
    elif index_val == 50:
        return "K_2"
    elif index_val == 51:
        return "K_3"
    elif index_val == 52:
        return "K_4"
    elif index_val == 53:
        return "K_5"
    elif index_val == 54:
        return "K_6"
    elif index_val == 55:
        return "K_7"
    elif index_val == 56:
        return "K_8"
    elif index_val == 57:
        return "K_9"
    elif index_val == 58:
        return "K_COLON"
    elif index_val == 59:
        return "K_SEMICOLON"
    elif index_val == 60:
        return "K_LESS"
    elif index_val == 61:
        return "K_EQUALS"
    elif index_val == 62:
        return "K_GREATER"
    elif index_val == 63:
        return "K_QUESTION"
    elif index_val == 64:
        return "K_AT"
    elif index_val == 91:
        return "K_LEFTBRACKET"
    elif index_val == 92:
        return "K_BACKSLASH"
    elif index_val == 93:
        return "K_RIGHTBRACKET"
    elif index_val == 94:
        return "K_CARET"
    elif index_val == 95:
        return "K_UNDERSCORE"
    elif index_val == 96:
        return "K_BACKQUOTE"
    elif index_val == 97:
        return "K_a"
    elif index_val == 98:
        return "K_b"
    elif index_val == 99:
        return "K_c"
    elif index_val == 100:
        return "K_d"
    elif index_val == 101:
        return "K_e"
    elif index_val == 102:
        return "K_f"
    elif index_val == 103:
        return "K_g"
    elif index_val == 104:
        return "K_h"
    elif index_val == 105:
        return "K_i"
    elif index_val == 106:
        return "K_j"
    elif index_val == 107:
        return "K_k"
    elif index_val == 108:
        return "K_l"
    elif index_val == 109:
        return "K_m"
    elif index_val == 110:
        return "K_n"
    elif index_val == 111:
        return "K_o"
    elif index_val == 112:
        return "K_p"
    elif index_val == 113:
        return "K_q"
    elif index_val == 114:
        return "K_r"
    elif index_val == 115:
        return "K_s"
    elif index_val == 116:
        return "K_t"
    elif index_val == 117:
        return "K_u"
    elif index_val == 118:
        return "K_v"
    elif index_val == 119:
        return "K_w"
    elif index_val == 120:
        return "K_x"
    elif index_val == 121:
        return "K_y"
    elif index_val == 122:
        return "K_z"
    elif index_val == 127:
        return "K_DELETE"
    elif index_val == 256:
        return "K_KP0"
    elif index_val == 257:
        return "K_KP1"
    elif index_val == 258:
        return "K_KP2"
    elif index_val == 259:
        return "K_KP3"
    elif index_val == 260:
        return "K_KP4"
    elif index_val == 261:
        return "K_KP5"
    elif index_val == 262:
        return "K_KP6"
    elif index_val == 263:
        return "K_KP7"
    elif index_val == 264:
        return "K_KP8"
    elif index_val == 265:
        return "K_KP9"
    elif index_val == 266:
        return "K_KP_PERIOD"
    elif index_val == 267:
        return "K_KP_DIVIDE"
    elif index_val == 268:
        return "K_KP_MULTIPLY"
    elif index_val == 269:
        return "K_KP_MINUS"
    elif index_val == 270:
        return "K_KP_PLUS"
    elif index_val == 271:
        return "K_KP_ENTER"
    elif index_val == 272:
        return "K_KP_EQUALS"
    elif index_val == 273:
        return "K_UP"
    elif index_val == 274:
        return "K_DOWN"
    elif index_val == 275:
        return "K_RIGHT"
    elif index_val == 276:
        return "K_LEFT"
    elif index_val == 277:
        return "K_INSERT"
    elif index_val == 278:
        return "K_HOME"
    elif index_val == 279:
        return "K_END"
    elif index_val == 280:
        return "K_PAGEUP"
    elif index_val == 281:
        return "K_PAGEDOWN"
    elif index_val == 282:
        return "K_F1"
    elif index_val == 283:
        return "K_F2"
    elif index_val == 284:
        return "K_F3"
    elif index_val == 285:
        return "K_F4"
    elif index_val == 286:
        return "K_F5"
    elif index_val == 287:
        return "K_F6"
    elif index_val == 288:
        return "K_F7"
    elif index_val == 289:
        return "K_F8"
    elif index_val == 290:
        return "K_F9"
    elif index_val == 291:
        return "K_F10"
    elif index_val == 292:
        return "K_F11"
    elif index_val == 293:
        return "K_F12"
    elif index_val == 294:
        return "K_F13"
    elif index_val == 295:
        return "K_F14"
    elif index_val == 296:
        return "K_F15"
    elif index_val == 300:
        return "K_NUMLOCK"
    elif index_val == 301:
        return "K_CAPSLOCK"
    elif index_val == 302:
        return "K_SCROLLOCK"
    elif index_val == 303:
        return "K_RSHIFT"
    elif index_val == 304:
        return "K_LSHIFT"
    elif index_val == 305:
        return "K_RCTRL"
    elif index_val == 306:
        return "K_LCTRL"
    elif index_val == 307:
        return "K_RALT"
    elif index_val == 308:
        return "K_LALT"
    elif index_val == 309:
        return "K_RMETA"
    elif index_val == 310:
        return "K_LMETA"
    elif index_val == 311:
        return "K_LSUPER"
    elif index_val == 312:
        return "K_RSUPER"
    elif index_val == 313:
        return "K_MODE"
    elif index_val == 315:
        return "K_HELP"
    elif index_val == 316:
        return "K_PRINT"
    elif index_val == 317:
        return "K_SYSREQ"
    elif index_val == 318:
        return "K_BREAK"
    elif index_val == 319:
        return "K_MENU"
    elif index_val == 320:
        return "K_POWER"
    elif index_val == 321:
        return "K_EURO"
