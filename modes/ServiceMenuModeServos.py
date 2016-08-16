import time

import math

import json

import configparser

import pygame
import tools

import config as c



TAP_TIMER = pygame.USEREVENT + 1
TAP_BOUNCE_MICROSECONDS = 300

class ServoAdjustmentsMode(tools.ModeBase):
    """
    Service Mode servo adjustments menu
    """

    def __init__(self, assets):
        super(ServoAdjustmentsMode, self).__init__(assets)
        self.tap_active = False
        self.movement_mode = False


    def process(self, events, pressed_keys):

        if self.movement_mode:
            self.rod.allowed_to_move = True
        else:
            self.rod.allowed_to_move = False

        for event in events:

            # If a button is pressed down...
            if event.type == pygame.KEYDOWN:
                if event.key == self.settings['Controls']['StartButton']:
                    if self.tap_active:
                        self.movement_mode = not self.movement_mode
                        pygame.time.set_timer(TAP_TIMER, 0)
                        self.tap_active = False
                    else:
                        pygame.time.set_timer(TAP_TIMER, TAP_BOUNCE_MICROSECONDS)
                        self.tap_active = True

            elif event.type == TAP_TIMER:
                pygame.time.set_timer(TAP_TIMER, 0)
                self.tap_active = False

        self.rod.activate_joysticks(pressed_keys)


    def render(self, screen):
        # Set background color
        screen.fill((0, 0, 64))

        if self.movement_mode:
            screen.fill((255, 127, 127))

        # Add title
        self.add_text(caption='Servo Adjustments', size=48, color=(255, 255, 255), y=50)
        self.add_text(caption='Double-tap the Start button to switch', y=90)
        self.add_text(caption='between adjustment and movement modes', y=120)

        if c.LeftServoStatus == "Setup Failed!":
            fontcolor = (255,0,0)
        else:
            fontcolor = (0,255,0)

        self.add_text(caption="Left Motor Status: " + c.LeftServoStatus, y=160, size=20, color=fontcolor)
        
        if c.RightServoStatus == "Setup Failed!":
            fontcolor = (255,0,0)
        else:
            fontcolor = (0,255,0)
            
        self.add_text(caption="Right Motor Status: " + c.RightServoStatus, y=175, size = 20, color=fontcolor)

        if self.movement_mode:
            # Generate the carriage and rod graphics
            self.rod.generate_graphics(screen)
            
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

