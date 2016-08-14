import time

import math

import json

import configparser

import pygame
import tools

import config as c





class LEDAddressesMode(tools.ModeBase):
    """
    Service Mode LED addresses menu
    """

    def __init__(self, assets):
        super(LEDAddressesMode, self).__init__(assets)

        self.led_fps = 60

        self.r_speed = 7
        self.g_speed = -13
        self.b_speed = 19

        self.r_frequency = 0.13
        self.g_frequency = 0.23
        self.b_frequency = 0.37

        self.start_time = time.time()

        self.current_led = 0


    def process(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                # Return to Service Mode main menu when Service button is pressed
                if event.key == self.settings['Controls']['ServiceButton']:
                    self.switch_to_mode(c.SERVICE_MENU_MODE)

                # If joystick(s) moved Down, move to next LED or back to top
                elif event.key == self.settings['Controls']['JoyLeftDown'] or event.key == self.settings['Controls']['JoyRightDown']:
                    self.current_led += 1
                    if self.current_led >= self.leds.number_of_leds:
                        self.current_led = 0

                # If joystick(s) moved Up, move to next LED or back to bottom
                elif event.key == self.settings['Controls']['JoyLeftUp'] or event.key == self.settings['Controls']['JoyRightUp']:
                    self.current_led -= 1
                    if self.current_led < 0:
                        self.current_led = self.leds.number_of_leds - 1


    def render(self, screen):
        # Set background color
        screen.fill((0, 0, 64))

        # Add title
        self.add_text(caption='LED Index: ' + str(self.current_led), size=48, color=(255, 255, 255), y=50)

        # Set phase to t
        t = (time.time() - self.start_time) * 22

        # Make a container list for the updated LED pixels
        pixels = []

        # For each LED pixel...
        for ii in range(self.leds.number_of_leds):

            # If current LED is selected, display a bright color, else dim white
            if ii == self.current_led:

                # Set RGB values with dissonant sine waves, increment on each pixel
                r = math.sin(t / self.r_speed + self.r_frequency * ii + 0) * 127 + 128
                g = math.sin(t / self.g_speed + self.g_frequency * ii + 2) * 127 + 128
                b = math.sin(t / self.b_speed + self.b_frequency * ii + 4) * 127 + 128

                # Invert channel when dark so that selected pixel is always bright
                if r < 128: r = 255 - r
                if g < 128: g = 255 - g
                if b < 128: b = 255 - b

            else:
                r = 64
                g = 64
                b = 64

            # Add the new RGB color to the LED pixels container
            pixels.append((r, g, b))
            # Generate the superficial on-screen pixel representation
            self.leds.generate_led_graphic(screen, ii, (r, g, b))

        # Send the new pixels to the actual LEDs
        self.leds.put_pixels(pixels)
