import time

import math

import json

import configparser

import pygame
import tools

import config as c


class DebugConsoleMode(tools.ModeBase):
    """
    Service Mode servo adjustments menu
    """

    def __init__(self, assets):
        super(DebugConsoleMode, self).__init__(assets)
        #tools.Debug_Print("Set up debug menu!")

    def process(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                # Return to Service Mode main menu when Service button is pressed
                if event.key == self.settings['Controls']['ServiceButton']:
                    self.switch_to_mode(c.SERVICE_MENU_MODE)


    def render(self, screen):
        # Set background color
        screen.fill((0, 0, 64))

        # Add title
        self.add_text(caption='Debug Console', size=48, color=(255, 255, 255), y=50)
        i=90
        
        # Prints Debug Buffer
        for line in tools.DEBUG_PRINT_BUFFER:
            i+=10
            self.add_text(caption="-"+line, size=20, color=(255, 255, 255), y=i, x=10)
