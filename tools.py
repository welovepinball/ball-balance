import os

import pygame

import config as c



#---------------------------------------------------------------------



class ModeBase:
    """Modes will inherit from this class. """

    def __init__(self, rod):
        self.rod = rod
        self.refresh(rod)


    def refresh(self, rod):
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



#---------------------------------------------------------------------
# Sound and music handling (won't crash PyGame if file not found!)
#---------------------------------------------------------------------

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
