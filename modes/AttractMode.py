import pygame

import tools

import config as c



class AttractMode(tools.ModeBase):

    def __init__(self, rod):
        self.rod = rod


    def process(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == c.START_BUTTON:
                    # Move to the next mode when the user presses the Start button
                    self.switch_to_mode(c.GAME_MODE)


    def render(self, screen):
        # Just fill the screen with all red
        screen.fill((255, 0, 0))
