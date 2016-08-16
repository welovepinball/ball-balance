import os

import pygame

import config as c



#---------------------------------------------------------------------


class ModeBase:
    """Modes will inherit from this class. """

    def __init__(self, assets):
        self.rod = assets['rod']
        self.leds = assets['leds']
        self.settings = assets['settings']
        self.screen = assets['screen']

        self.refresh(assets)


    def refresh(self, assets):
        """Set the mode's next property to self.

        If the program has already been in this mode before and switched to a
        different one, self.next will still be set to that last location, so
        run_game() will switch the mode back to that one if not for calling this
        method before that happens.

        """
        self.next = self


    def process(self, events, pressed_keys):
        """Process the filtered list of events.

        Subclasses should override this method or else they get a warning.

        """
        print("You need to override process() in the child class!")


    def render(self, screen):
        """Render output, to screen and otherwise.

        Subclasses should override this method or else they get a warning.

        """
        print("You need to override render() in the child class!")


    def switch_to_mode(self, next_mode):
        """Set mode's next property to the given mode."""

        self.next = next_mode


    def add_text(self, caption = "", size = 36, align = 'left', color = (255, 255, 0), x = 'center', y = 240):
        """ Helper function to add text without all the boilerplate """

        font = pygame.font.Font(None, size)
        text = font.render(caption, 1, color)

        position = text.get_rect()
        if x == 'center':
            position.centerx = self.settings['Screen']['X'] / 2
        else:
            if align == 'right':
                position.right = x
            else:
                position.left = x

        position.centery = y
        self.screen.blit(text, position)





#-----------------------------------------------------------------
# Sound and music handling (won't crash PyGame if file not found!)
#-----------------------------------------------------------------

sounds = {}

def play_sound(path):

    sound = sounds.get(path)
    if sound == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)

        if os.path.isfile(canonicalized_path):
            sound = pygame.mixer.Sound(canonicalized_path)
            sounds[path] = sound
        else:
            sound = None

    if sound:
        sound.play()



def play_song(path, loop = 0):

    canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)

    if os.path.isfile(canonicalized_path):
        pygame.mixer.music.load(canonicalized_path)
        pygame.mixer.music.play(loop)

#-----------------------------------------------------------------
# Debug Print Buffer
#-----------------------------------------------------------------

DEBUG_PRINT_BUFFER=[]

def Debug_Print(line):
    #if less than 10 items in buffer, then add new line to end
    if len(DEBUG_PRINT_BUFFER)<10:
        DEBUG_PRINT_BUFFER.append(line)
    #if 10 items in buffer, shift items up and add new line to end
    else:
        i=0
        while i < 9:
            DEBUG_PRINT_BUFFER[i]=DEBUG_PRINT_BUFFER[i+1]
            i+=1
        DEBUG_PRINT_BUFFER[i]=line

DEBUG_TOGGLE = True
