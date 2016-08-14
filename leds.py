import json

import opc

import pygame


class LEDs:

    def __init__(self, settings):
        self.settings = settings

        self.server = opc.Client('localhost:7890')

        json_data = open('./opc/playfield.json')
        self.led_map = json.load(json_data)

        self.number_of_leds = len(self.led_map)

        self.center_x = int(self.settings['Screen']['X'] / 2)
        self.center_y = int(self.settings['Screen']['Y'] / 2)

        self.multiplier = self.settings['Screen']['Y'] / 5.5
        self.circle_diameter = int(self.settings['Screen']['Y'] / 60)
        self.circle_outline_width = int(self.circle_diameter / 2)


    def put_pixels(self, pixels):
        self.server.put_pixels(pixels)


    def reset_all_pixels(self):
        print('This is where the reset code will go!')


    def generate_led_graphic(self, screen, number, color):

        led_position_x = int(self.center_x - (self.multiplier * self.led_map[number]['point'][0]))
        led_position_y = int(self.center_y - (self.multiplier * self.led_map[number]['point'][2]))

        pygame.draw.circle(
            screen, color, (led_position_x, led_position_y),
            self.circle_diameter, self.circle_outline_width
        )
