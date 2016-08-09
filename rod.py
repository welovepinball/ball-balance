try:
    import RPi.GPIO as GPIO
except:
    print ("Could not import RPi.GPIO")

import pygame

import tools

import config as c


class Rod:

    allowed_to_move = False

    limit_left_up    = False
    limit_left_down  = False
    limit_right_up   = False
    limit_right_down = False

    # If servo code were reimplemented completely,
    # this should be set to True
    servos_operational = False

    left_bar_position  = 260
    right_bar_position = 260


    def init(self):
        # Sets up GPIO pins and motors - DO NOT MODIFY
        try:
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(c.RPI_PIN_LEFT_SERVO, GPIO.OUT)
            GPIO.setup(c.RPI_PIN_RIGHT_SERVO, GPIO.OUT)

            self.left_servo  = GPIO.PWM(c.RPI_PIN_LEFT_SERVO, 50)
            self.right_servo = GPIO.PWM(c.RPI_PIN_RIGHT_SERVO, 50)
        except:
            print ("Could not set up servos.")
            servos_operational = False


    def activate_joysticks(self, pressed_keys):
        if pressed_keys[c.LEFT_JOY_UP] and pressed_keys[c.RIGHT_JOY_UP]:
            self.player_move(1, 1)
        elif pressed_keys[c.LEFT_JOY_UP] and pressed_keys[c.RIGHT_JOY_DOWN]:
            self.player_move(1, -1)
        elif pressed_keys[c.LEFT_JOY_DOWN] and pressed_keys[c.RIGHT_JOY_UP]:
            self.player_move(-1, 1)
        elif pressed_keys[c.LEFT_JOY_DOWN] and pressed_keys[c.RIGHT_JOY_DOWN]:
            self.player_move(-1, -1)
        elif pressed_keys[c.LEFT_JOY_UP]:
            self.player_move(1, 0)
        elif pressed_keys[c.LEFT_JOY_DOWN]:
            self.player_move(-1, 0)
        elif pressed_keys[c.RIGHT_JOY_UP]:
            self.player_move(0, 1)
        elif pressed_keys[c.RIGHT_JOY_DOWN]:
            self.player_move(0, -1)


    """
    Formula to drive servos
    ----------------------------------
    * The midpoint (stopping point) for the continuous servo is 7.5
    * While the stopping point should be the midpoint, the servo must be calibrated properly, so alternatively setting the pulse to 0 will stop movement
    * Full speed one direction is 5 (min)
    * Full speed the other direction is 10 (max)
    * Slower speeds are achievable at values between midpoint and min/max.
    """
    def move(self, left, right, add_sound = False):
        if left > 0:
            if self.limit_left_up:
                print('LEFT UP PREVENTED!')
            else:
                #print('Moving left up!')
                if add_sound: tools.play_sound(c.AUDIO_ROD_LEFT_UP)

                if self.servos_operational:
                    try:
                        self.left_servo.start(7.5+c.SERVO_SPEED)
                    except:
                        print('ERROR: Could not move left servo up.')

                # This is superficial, for testing purposes. Will be removed.
                self.left_bar_position -= 3

        elif left < 0:
            if self.limit_left_down:
                print('LEFT DOWN PREVENTED!')
            else:
                #print('Moving left down!')
                if add_sound: tools.play_sound(c.AUDIO_ROD_LEFT_DOWN)

                if self.servos_operational:
                    try:
                        self.left_servo.start(7.5-c.SERVO_SPEED)
                    except:
                        print('ERROR: Could not move left servo down.')

                # This is superficial, for testing purposes. Will be removed.
                self.left_bar_position += 3

        else:
            if self.servos_operational:
                try:
                    #setting pulse to 0 to kill motor rather than 7.5 to stall it
                    self.left_servo.start(0)
                except:
                    print('ERROR: Could not stop left servo.')


        if right > 0:
            if self.limit_right_up:
                print('RIGHT UP PREVENTED!')
            else:
                #print('Moving right up!')
                if add_sound: tools.play_sound(c.AUDIO_ROD_RIGHT_UP)

                if self.servos_operational:
                    try:
                        self.left_servo.start(7.5+c.SERVO_SPEED)
                    except:
                        print('ERROR: Could not move right servo up.')

                # This is superficial, for testing purposes. Will be removed.
                self.right_bar_position -= 3

        elif right < 0:
            if self.limit_right_down:
                print('RIGHT DOWN PREVENTED!')
            else:
                #print('Moving right down!')
                if add_sound: tools.play_sound(c.AUDIO_ROD_RIGHT_DOWN)

                if self.servos_operational:
                    try:
                        self.left_servo.start(7.5-c.SERVO_SPEED)
                    except:
                        print('ERROR: Could not move right servo down.')

                # This is superficial, for testing purposes. Will be removed.
                self.right_bar_position += 3

        else:
            if self.servos_operational:
                try:
                    #setting pulse to 0 to kill motor rather than 7.5 to stall it
                    self.left_servo.start(0)
                except:
                    print('ERROR: Could not stop right servo.')


    def player_move(self, left, right):
        if self.allowed_to_move:
            self.move(left, right, True)
        else:
            print('NOT ALLOWED TO MOVE RIGHT NOW!')


    def generate_graphics(self, screen):
        """ This is superficial, for testing purposes. Will be removed. """

        # Set the left and right carriages to blue
        left_block_color  = (0, 128, 255)
        right_block_color = (0, 128, 255)

        # If a limit switch is active on either side, change its carriage to orange
        if self.limit_left_up  or self.limit_left_down or not self.allowed_to_move:  left_block_color  = (255, 100, 0)
        if self.limit_right_up or self.limit_right_down or not self.allowed_to_move: right_block_color = (255, 100, 0)

        # Draw the carriages to the screen
        pygame.draw.rect(screen, left_block_color,  pygame.Rect(30,  self.left_bar_position,  60, 60))
        pygame.draw.rect(screen, right_block_color, pygame.Rect(300, self.right_bar_position, 60, 60))

        # Add a line for the bar between the carriage blocks
        pygame.draw.line(screen, (200, 200, 200), (90, self.left_bar_position + 30), (300, self.right_bar_position + 30), 10)
