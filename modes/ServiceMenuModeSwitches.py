import time

import math

import json

import configparser

import pygame
import tools

import config as c





class ConfigureSwitchesMode(tools.ModeBase):
    """
    Service Mode switch configuration menu
    """

    def __init__(self, assets):
        super(ConfigureSwitchesMode, self).__init__(assets)

        """ Dicts are inherently unsortable, but that doesn't help us for
        displaying their content in a user-friendly manner (alphabetically).
        So let's make a list and naturally sort it. """
        self.sorted_switches = sorted(self.settings['Controls'].keys(), key=self.natural_sort)

        # A dict to hold the new switch values
        self.new_switches = {}

        self.current_switch = 0
        self.reusing_switch = False

        # After amount while iterating over switches for display, move to next column
        self.max_items_per_column = 11

        # Set initial state
        self.state = 'switch tests'


    def process(self, events, pressed_keys):

        # Reach back to game.py to disable its Service Mode switch
        global override_service_button
        override_service_button = True

        self.pressed_keys = pressed_keys

        # If in 'switch tests' state, advance state when both joysticks are pushed Up
        if self.state == 'switch tests':
            if pressed_keys[int(self.settings['Controls']['JoyLeftUp'])] and pressed_keys[int(self.settings['Controls']['JoyRightUp'])]:
                self.state = 'initialize configuration'

        # If in 'initialize configuration' state, move the rod out of the way
        elif self.state == 'initialize configuration':
            # Advance state when Start button is pressed
            if pressed_keys[int(self.settings['Controls']['StartButton'])]:
                self.state = 'configuration in process'

            # If a limit switch is active, move the rod off of it
            elif pressed_keys[int(self.settings['Controls']['LimitLeftBottom'])]:
                self.rod.move(1, 0)
            elif pressed_keys[int(self.settings['Controls']['LimitLeftTop'])]:
                self.rod.move(-1, 0)
            elif pressed_keys[int(self.settings['Controls']['LimitRightBottom'])]:
                self.rod.move(0, 1)
            elif pressed_keys[int(self.settings['Controls']['LimitRightTop'])]:
                self.rod.move(0, -1)

        # If in 'configuration in process' state, advance state if out of switches
        elif self.state == 'configuration in process':
            if self.current_switch >= len(self.sorted_switches):
                self.state = 'confirm save'

        # If in 'confirm save' state, advance state if Start button is pressed
        elif self.state == 'confirm save':
            if pressed_keys[int(self.settings['Controls']['StartButton'])]:
                self.state = 'save settings'

        # If in 'save settings' state, rebuild updated settings.ini, save, reset
        elif self.state == 'save settings':
            self.settings['Controls'] = self.new_switches

            config = configparser.ConfigParser()
            config.optionxform = str

            for section in self.settings:
                config.add_section(section)
                for key in self.settings[section]:
                    config.set(section, key, str(self.settings[section].get(key)))

            config_file = open('settings.ini', 'w')
            config.write(config_file)
            config_file.close()


            # Reset
            self.new_switches = {}
            self.current_switch = 0
            self.state = 'switch tests'


        for event in events:
            allow_set_key = False

            if event.type == pygame.KEYDOWN:
                if self.state == 'configuration in process':
                    if self.sorted_switches[self.current_switch] == 'HoleSwitchFailure':
                        allow_set_key = True
                    else:
                        if event.key != self.settings['Controls']['HoleSwitchFailure']:
                            allow_set_key = True

                    if allow_set_key:
                        if self.check_if_already_used(event.key):
                            allow_set_key = False
                            self.reusing_switch = True
                        else:
                            allow_set_key = True

                if event.key == self.settings['Controls']['ServiceButton']:
                    if self.state == 'configuration in process' and self.sorted_switches[self.current_switch] == 'ServiceButton':
                        allow_set_key = True
                    else:
                        self.switch_to_mode(c.SERVICE_MENU_MODE)

                if allow_set_key:
                        self.reusing_switch = False

                        self.new_switches[self.sorted_switches[self.current_switch]] = event.key
                        self.current_switch += 1

        override_service_button = False


    def render(self, screen):
        # Set background color
        screen.fill((0, 0, 64))

        self.add_text(caption='Switch Configuration', size=48, color=(255, 255, 255), y=50)

        if self.state == 'switch tests':
            self.add_text(caption='Move both joysticks Up to reconfigure switches', y=90)

            original_legend_pos = legend_pos = 100
            ii = 0
            current_column = 1

            for switch in self.sorted_switches:
                legend_pos += 28

                x = (current_column - 1) * 180 + 180

                # Change the color of a switch that is activated
                color = (255, 255, 255)
                if self.pressed_keys[int(self.settings['Controls'][switch])]:
                    color = (255, 0, 255)

                # Add each switch description and selected key
                self.add_text(caption=str(switch) + ': ', size=24, color=(255, 255, 0), align='right', x=x, y=legend_pos)
                self.add_text(pygame.key.name(self.settings['Controls'][switch]), size=24, color=color, align='left', x=x+5, y=legend_pos)

                # Iterate switch counter, reset if too high and iterate column
                ii += 1
                if ii == self.max_items_per_column:
                    ii = 0
                    current_column += 1
                    legend_pos = original_legend_pos

        # Essentially just an instructions screen before the configuration loop
        elif self.state == 'initialize configuration':

            # Add title
            self.add_text(caption='Directions', y=90)

            # Add instructions
            instructions = [
                '• If any limit switches were active, the machine moved',
                '  the rod to deactivate them.',
                '• This process is easier with your playfield glass off.',
                '• You can exit at any time without saving changes by',
                '  pressing the Service button (currently set to: ' +
                pygame.key.name(self.settings['Controls']['ServiceButton']) + ')',
                '• You cannot set multiple keys to the same switch or',
                '  set multiple switches to the same key.',
                '• Your new configuration won\'t become active until',
                '  you confirm and save at the end.'
            ]
            previous_text_y = 100
            for instruction in instructions:
                previous_text_y += 28
                self.add_text(caption=instruction, color=(255, 255, 255), size=30, x=40, y=previous_text_y)

            # Add press Start notice
            self.add_text(caption='Press the Start button to begin', y=previous_text_y+40)
            self.add_text(caption='(currently set to: ' +
                pygame.key.name(self.settings['Controls']['StartButton']) + ')', size=30, y=previous_text_y+70)

        elif self.state == 'configuration in process':
            if self.current_switch < len(self.sorted_switches):
                self.add_text(caption='Activate the switch for:', y=190)
                self.add_text(caption=self.sorted_switches[self.current_switch], size=40, color=(255, 255, 255), y=225)

                if self.reusing_switch:
                    self.add_text(caption='ERROR: That switch has been used! Try again.', color=(255, 0, 0), y=260)

        elif self.state == 'confirm save':
            self.add_text(caption='Configuration complete.', y=90)
            self.add_text(caption='Press the Start button to save settings.', y=120)
            self.add_text(caption='Otherwise, press the Service button to exit.', y=150)


    def check_if_already_used(self, key):
        """ For each of the new switches set, check if used, return result """
        for switch in self.new_switches:
            if key == self.new_switches[switch]:
                return True
        return False


    def natural_sort(self, s):
        """
        Helper function to enhance sorted() with natural sorting
        Would normally sort HoleSwitch1, HoleSwitch10, HoleSwitch2, etc.
        """

        # Regular expressions library
        import re

        # Container for output
        new_s = []

        # For each chunk in the given string, split by the numbers...
        for c in re.split(r'([0-9]+)', s):

            # If the chunk is a number, add to the list reformatted as an int, else str
            if re.match(r'[0-9]+$', c):
                new_s.append(int(c))
            else:
                new_s.append(c)

        return new_s
