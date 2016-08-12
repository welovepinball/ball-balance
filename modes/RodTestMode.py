import pygame

import tools

import rod

import config as c



class RodTestMode(tools.ModeBase):
    
    def __init__(self, rod):
        

        self.rod = rod
        self.rod.allowed_to_move = True




    def process(self, events, pressed_keys):
        # ------------------------------------------------------------

        self.rod.activate_joysticks(pressed_keys)



    def render(self, screen):

        # Fill the screen with black to redraw the graphics
        screen.fill((0, 0, 0))

        # Generate the carriage and rod graphics
        self.rod.generate_graphics(screen)
