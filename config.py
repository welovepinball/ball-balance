import os

import sys

import pygame



#---------------------------------------------------------------------
# Graphics
#---------------------------------------------------------------------

SCREEN_WIDTH  = 640
SCREEN_HEIGHT = 480



#---------------------------------------------------------------------
# Servos
#---------------------------------------------------------------------

# Change pin number to change the corresponding GPIO for the left and right servos.
RPI_PIN_LEFT_SERVO  = 12
RPI_PIN_RIGHT_SERVO = 40

# Opens servo config file, reads in value and applies to speed variable
servo_config_path = sys.path[0] + "/servo_config.txt"
canonicalized_path = servo_config_path.replace('/', os.sep).replace('\\', os.sep)

servo_config_file = open(canonicalized_path, "r")

SERVO_SPEED = float(servo_config_file.readline())

#check speed
if SERVO_SPEED<.5:
    SERVO_SPEED=.5
elif SERVO_SPEED>2.5:
    SERVO_SPEED=2.5

servo_config_file.close()


#---------------------------------------------------------------------
# Switches
#---------------------------------------------------------------------

# Opens control config file, reads in values, and apply them to keys
control_config_path = sys.path[0] + "/control_config.txt"
canonicalized_path = control_config_path.replace('/', os.sep).replace('\\', os.sep)

control_config_file = open(canonicalized_path, "r")

keyinput = []
for line in control_config_file:
    line = line[line.find("=") + 1:]
    if '\n' in line:
        line = line[:len(line) - 1]
    #print(line)
    keyinput.append(int(line))

LEFT_JOY_UP    = keyinput[0]
LEFT_JOY_DOWN  = keyinput[1]
RIGHT_JOY_UP   = keyinput[2]
RIGHT_JOY_DOWN = keyinput[3]

LEFT_LIMIT_TOP     = keyinput[4]
LEFT_LIMIT_BOTTOM  = keyinput[5]
RIGHT_LIMIT_TOP    = keyinput[6]
RIGHT_LIMIT_BOTTOM = keyinput[7]

START_BUTTON   = keyinput[8]
SERVICE_BUTTON = keyinput[9]
TILT_SWITCH    = keyinput[10]

HOLES_SWITCHES = {
    1:  keyinput[11],
    2:  keyinput[12],
    3:  keyinput[13],
    4:  keyinput[14],
    5:  keyinput[15],
    6:  keyinput[16],
    7:  keyinput[17],
    8:  keyinput[18],
    9:  keyinput[19],
    10: keyinput[20]
}
HOLE_FAILURE_SWITCH=keyinput[21]

control_config_file.close()



#---------------------------------------------------------------------
# Audio
#---------------------------------------------------------------------

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



#---------------------------------------------------------------------
# Key Lookup
#---------------------------------------------------------------------

def key_name_lookup(key):
    legend = {
        8: 'K_BACKSPACE',
        9: 'K_TAB',
        12: 'K_CLEAR',
        13: 'K_RETURN',
        19: 'K_PAUSE',
        27: 'K_ESCAPE',
        32: 'K_SPACE',
        33: 'K_EXCLAIM',
        34: 'K_QUOTEDBL',
        35: 'K_HASH',
        36: 'K_DOLLAR',
        38: 'K_AMPERSAND',
        39: 'K_QUOTE',
        40: 'K_LEFTPAREN',
        41: 'K_RIGHTPAREN',
        42: 'K_ASTERISK',
        43: 'K_PLUS',
        44: 'K_COMMA',
        45: 'K_MINUS',
        46: 'K_PERIOD',
        47: 'K_SLASH',
        48: 'K_0',
        49: 'K_1',
        50: 'K_2',
        51: 'K_3',
        52: 'K_4',
        53: 'K_5',
        54: 'K_6',
        55: 'K_7',
        56: 'K_8',
        57: 'K_9',
        58: 'K_COLON',
        59: 'K_SEMICOLON',
        60: 'K_LESS',
        61: 'K_EQUALS',
        62: 'K_GREATER',
        63: 'K_QUESTION',
        64: 'K_AT',
        91: 'K_LEFTBRACKET',
        92: 'K_BACKSLASH',
        93: 'K_RIGHTBRACKET',
        94: 'K_CARET',
        95: 'K_UNDERSCORE',
        96: 'K_BACKQUOTE',
        97: 'K_a',
        98: 'K_b',
        99: 'K_c',
        100: 'K_d',
        101: 'K_e',
        102: 'K_f',
        103: 'K_g',
        104: 'K_h',
        105: 'K_i',
        106: 'K_j',
        107: 'K_k',
        108: 'K_l',
        109: 'K_m',
        110: 'K_n',
        111: 'K_o',
        112: 'K_p',
        113: 'K_q',
        114: 'K_r',
        115: 'K_s',
        116: 'K_t',
        117: 'K_u',
        118: 'K_v',
        119: 'K_w',
        120: 'K_x',
        121: 'K_y',
        122: 'K_z',
        127: 'K_DELETE',
        256: 'K_KP0',
        257: 'K_KP1',
        258: 'K_KP2',
        259: 'K_KP3',
        260: 'K_KP4',
        261: 'K_KP5',
        262: 'K_KP6',
        263: 'K_KP7',
        264: 'K_KP8',
        265: 'K_KP9',
        266: 'K_KP_PERIOD',
        267: 'K_KP_DIVIDE',
        268: '_KP_MULTIPLY',
        269: 'K_KP_MINUS',
        270: 'K_KP_PLUS',
        271: 'K_KP_ENTER',
        272: 'K_KP_EQUALS',
        273: 'K_UP',
        274: 'K_DOWN',
        275: 'K_RIGHT',
        276: 'K_LEFT',
        277: 'K_INSERT',
        278: 'K_HOME',
        279: 'K_END',
        280: 'K_PAGEUP',
        281: 'K_PAGEDOWN',
        282: 'K_F1',
        283: 'K_F2',
        284: 'K_F3',
        285: 'K_F4',
        286: 'K_F5',
        287: 'K_F6',
        288: 'K_F7',
        289: 'K_F8',
        290: 'K_F9',
        291: 'K_F10',
        292: 'K_F11',
        293: 'K_F12',
        294: 'K_F13',
        295: 'K_F14',
        296: 'K_F15',
        300: 'K_NUMLOCK',
        301: 'K_CAPSLOCK',
        302: 'K_SCROLLOCK',
        303: 'K_RSHIFT',
        304: 'K_LSHIFT',
        305: 'K_RCTRL',
        306: 'K_LCTRL',
        307: 'K_RALT',
        308: 'K_LALT',
        309: 'K_RMETA',
        310: 'K_LMETA',
        311: 'K_LSUPER',
        312: 'K_RSUPER',
        313: 'K_MODE',
        315: 'K_HELP',
        316: 'K_PRINT',
        317: 'K_SYSREQ',
        318: 'K_BREAK',
        319: 'K_MENU',
        320: 'K_POWER',
        321: 'K_EURO'
    }

    return legend[key]
