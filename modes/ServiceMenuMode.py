import time

import math

import json

import configparser

import pygame
import tools

import config as c

from .ServiceMenuModeSwitches import ConfigureSwitchesMode
from .ServiceMenuModeServos import ServoAdjustmentsMode
from .ServiceMenuModeLEDs import LEDAddressesMode
from .ServiceMenuModeDebugConsole import DebugConsoleMode
from .ServiceMenuSettings import SettingsMenuMode

configured = False

class ServiceMenuMode(tools.ModeBase):
    """
    Service Mode main menu
    """

    def __init__(self, assets):
        super(ServiceMenuMode, self).__init__(assets)

        global configured

        if not configured:
            configured = True

            self.main_menu = [
                {'item': 'Settings', 'class': SettingsMenuMode(assets)},
                {'item': 'Switch Configuration', 'class': ConfigureSwitchesMode(assets)},
                {'item': 'Servo Adjustments', 'class': ServoAdjustmentsMode(assets)},
                {'item': 'LED Addresses', 'class': LEDAddressesMode(assets)},
                {'item': 'Debug Console', 'class': DebugConsoleMode(assets)},
            ]

        self.selected_menu_item = 0


    def process(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                # If the Service button is pressed, go back to Attract Mode
                if event.key == self.settings['Controls']['ServiceButton']:
                    self.switch_to_mode(c.ATTRACT_MODE)

                # If Start button is pressed, switch mode to active menu item
                elif event.key == self.settings['Controls']['StartButton']:
                    self.switch_to_mode(self.main_menu[self.selected_menu_item]['class'])

                # If joystick(s) moved Up, go up one menu item or back to bottom
                elif event.key == self.settings['Controls']['JoyLeftUp'] or event.key == self.settings['Controls']['JoyRightUp']:
                    if self.selected_menu_item <= 0:
                        self.selected_menu_item = len(self.main_menu) - 1
                    else:
                        self.selected_menu_item -= 1

                # If joystick(s) moved Down, go down one menu item or back to top
                elif event.key == self.settings['Controls']['JoyLeftDown'] or event.key == self.settings['Controls']['JoyRightDown']:
                    if self.selected_menu_item >= len(self.main_menu) - 1:
                        self.selected_menu_item = 0
                    else:
                        self.selected_menu_item += 1


    def render(self, screen):
        # Set background color
        screen.fill((0, 0, 64))

        previous_text_y = 50

        # Add title
        self.add_text(caption='Service Menu', size=48, color=(255, 255, 255), y=previous_text_y)
        previous_text_y += 20

        # Add instructions
        instructions = [
            'Use either joystick to navigate',
            'Press Start button to submit',
            'Press Service button to exit current menu'
        ]
        for instruction in instructions:
            previous_text_y += 30
            self.add_text(caption='• ' + instruction, x=80, y=previous_text_y)

        previous_text_y += 40

        #Loop through and display all main menu items
        for option in self.main_menu:

            previous_text_y += 38

            text = option['item']
            if self.main_menu[self.selected_menu_item]['item'] == text:
                text = '> ' + text + ' <'
                color = (0, 255, 255)
            else:
                color = (255, 255, 255)
            self.add_text(caption=text, color=color, y=previous_text_y)
