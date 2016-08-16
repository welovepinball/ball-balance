import time

import math

import json

import pygame

import tools

import config as c



class AttractMode(tools.ModeBase):

    def __init__(self, assets):
        super(AttractMode, self).__init__(assets)

        self.led_fps = 60

        self.r_speed = 7
        self.g_speed = -13
        self.b_speed = 19

        self.r_frequency = 0.13
        self.g_frequency = 0.23
        self.b_frequency = 0.37

        self.start_time = time.time()


    def process(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == self.settings['Controls']['StartButton']:
                    # Move to the next mode when the user presses the Start button
                    self.switch_to_mode(c.GAME_MODE)


    def render(self, screen):
        # Just fill the screen with all red
        screen.fill((64, 64, 64))

        t = (time.time() - self.start_time) * 22

        pixels = []

        

        for ii in range(self.leds.number_of_leds):

            r = math.sin(t / self.r_speed + self.r_frequency * ii + 0) * 127 + 128
            g = math.sin(t / self.g_speed + self.g_frequency * ii + 2) * 127 + 128
            b = math.sin(t / self.b_speed + self.b_frequency * ii + 4) * 127 + 128

            if ii % 2:
                r = 255 - r
                g = 255 - g
                b = 255 - b

            pixels.append((r, g, b))

            self.leds.generate_led_graphic(screen, ii, (r, g, b))

        self.leds.put_pixels(pixels)

        #Checks if Debugging is on
        if tools.DEBUG_TOGGLE:

            #increments debug timer and adds blank to print buffer
            #this would eventually clear the buffer if no other print commands are sent
            tools.DEBUG_TIMER+=1
            if tools.DEBUG_TIMER > tools.DEBUG_TIMER_MAX:
                tools.DEBUG_TIMER = 0
                tools.Debug_Print("")
            debug_y=350
            # Prints Debug Buffer
            for line in tools.DEBUG_PRINT_BUFFER:
                debug_y+=10
                debug_caption = ""
                if line:
                    debug_caption = "-" + line
                self.add_text(caption=debug_caption, size=20, color=(255, 255, 255), y=debug_y, x=14)
            
