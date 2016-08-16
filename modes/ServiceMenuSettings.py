import time

import math

import json

import configparser

import pygame
import tools

import config as c




class SettingsMenuMode(tools.ModeBase):
    """
    Service Mode servo adjustments menu
    """

    def __init__(self, assets):
        super(SettingsMenuMode, self).__init__(assets)
        self.menu_items = [
            {'item': "Debug Mode: " + str(tools.DEBUG_TOGGLE)},
            {'item': "Item 2: " },
            {'item': "Item 3: " },
        ]

        self.selected_menu_item = 0


    def process(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                # Return to Service Mode main menu when Service button is pressed
                if event.key == self.settings['Controls']['ServiceButton']:
                    self.switch_to_mode(c.SERVICE_MENU_MODE)
                elif event.key == self.settings['Controls']['JoyLeftDown'] or event.key == self.settings['Controls']['JoyRightDown'] :
                    if self.selected_menu_item < len(self.menu_items)-1:
                        self.selected_menu_item +=1
                    else:
                        self.selected_menu_item=0
                elif event.key == self.settings['Controls']['JoyLeftUp'] or event.key == self.settings['Controls']['JoyRightUp']:
                    if self.selected_menu_item > 0:
                        self.selected_menu_item -=1
                    else:
                        self.selected_menu_item=len(self.menu_items)-1
                elif event.key == self.settings['Controls']['StartButton']:
                    if self.selected_menu_item == 0:
                        if tools.DEBUG_TOGGLE == False:
                            tools.DEBUG_TOGGLE=True
                        else:
                            tools.DEBUG_TOGGLE=False
                        self.menu_items[self.selected_menu_item]['item']= "Debug Mode: " + str(tools.DEBUG_TOGGLE)


    def render(self, screen):
        
        # Set background color
        screen.fill((0, 0, 64))
        previous_text_y = 50

        # Add title
        self.add_text(caption='Settings Menu', size=48, color=(255, 255, 255), y=previous_text_y)
        previous_text_y += 20

        # Add instructions
        instructions = [
            'Use either joystick to navigate',
            'Press Start button to change value',
            'Press Service button to exit current menu'
        ]
        for instruction in instructions:
            previous_text_y += 30
            self.add_text(caption='• ' + instruction, x=80, y=previous_text_y)

        previous_text_y += 40

        for option in self.menu_items:
            text = option['item']
            previous_text_y += 40
            if self.menu_items[self.selected_menu_item]['item'] == text:
                text = ">" + text + "<"
                color=(0, 255, 255)
            else:
                color=(255, 255, 255)
            self.add_text(caption=text, color=color, y=previous_text_y,x=20)
        
##        # Prints Debug Buffer
##        for line in tools.DEBUG_PRINT_BUFFER:
##            i+=10
##            self.add_text(caption="-"+line, size=20, color=(255, 255, 255), y=i, x=10)
