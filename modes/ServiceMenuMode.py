import pygame
import tools

import config as c


global menu_item_total
menu_item_total = 3
global current_menu_item
current_menu_item = 1

global main_menu_items
main_menu_items = []

main_menu_items.append("Control Configuration")
main_menu_items.append("Menu Item 2")
main_menu_items.append("Menu Item 3")


global config_menu_total_items
global config_menu_items
config_menu_items = []
global config_menu_current_switch


config_menu_items.append("LEFT_JOY_UP" + '\n' + "Current Key: " + c.key_name_lookup(c.LEFT_JOY_UP) + '\n' + "Current Value: "+ str(c.LEFT_JOY_UP))
config_menu_items.append("LEFT_JOY_DOWN" + '\n' + "Current Key: " + c.key_name_lookup(c.LEFT_JOY_DOWN) + '\n' + "Current Value: "+ str(c.LEFT_JOY_DOWN))
config_menu_items.append("RIGHT_JOY_UP" + '\n' + "Current Key: " + c.key_name_lookup(c.RIGHT_JOY_UP) + '\n' + "Current Value: "+ str(c.RIGHT_JOY_UP))
config_menu_items.append("RIGHT_JOY_DOWN" + '\n' + "Current Key: " + c.key_name_lookup(c.RIGHT_JOY_DOWN) + '\n' + "Current Value: "+ str(c.RIGHT_JOY_DOWN))
config_menu_items.append("LEFT_LIMIT_TOP" + '\n' + "Current Key: " + c.key_name_lookup(c.LEFT_LIMIT_TOP) + '\n' + "Current Value: "+ str(c.LEFT_LIMIT_TOP))
config_menu_items.append("LEFT_LIMIT_BOTTOM" + '\n' + "Current Key: " + c.key_name_lookup(c.LEFT_LIMIT_BOTTOM) + '\n' + "Current Value: "+ str(c.LEFT_LIMIT_BOTTOM))
config_menu_items.append("RIGHT_LIMIT_TOP" + '\n' + "Current Key: " + c.key_name_lookup(c.RIGHT_LIMIT_TOP) + '\n' + "Current Value: "+ str(c.RIGHT_LIMIT_TOP))
config_menu_items.append("RIGHT_LIMIT_BOTTOM" + '\n' + "Current Key: " + c.key_name_lookup(c.RIGHT_LIMIT_BOTTOM) + '\n' + "Current Value: "+ str(c.RIGHT_LIMIT_BOTTOM))
config_menu_items.append("START_BUTTON" + '\n' + "Current Key: " + c.key_name_lookup(c.START_BUTTON) + '\n' + "Current Value: "+ str(c.START_BUTTON))
config_menu_items.append("SERVICE_BUTTON" + '\n' + "Current Key: " + c.key_name_lookup(c.SERVICE_BUTTON) + '\n' + "Current Value: "+ str(c.SERVICE_BUTTON))
config_menu_items.append("TILT_SWITCH" + '\n' + "Current Key: " + c.key_name_lookup(c.TILT_SWITCH) + '\n' + "Current Value: "+ str(c.TILT_SWITCH))
config_menu_items.append("HOLE_1_SWITCH" + '\n' + "Current Key: " + c.key_name_lookup(c.HOLES_SWITCHES[1]) + '\n' + "Current Value: "+ str(c.HOLES_SWITCHES[1]))
config_menu_items.append("HOLE_2_SWITCH" + '\n' + "Current Key: " + c.key_name_lookup(c.HOLES_SWITCHES[2]) + '\n' + "Current Value: "+ str(c.HOLES_SWITCHES[2]))
config_menu_items.append("HOLE_3_SWITCH" + '\n' + "Current Key: " + c.key_name_lookup(c.HOLES_SWITCHES[3]) + '\n' + "Current Value: "+ str(c.HOLES_SWITCHES[3]))
config_menu_items.append("HOLE_4_SWITCH" + '\n' + "Current Key: " + c.key_name_lookup(c.HOLES_SWITCHES[4]) + '\n' + "Current Value: "+ str(c.HOLES_SWITCHES[4]))
config_menu_items.append("HOLE_5_SWITCH" + '\n' + "Current Key: " + c.key_name_lookup(c.HOLES_SWITCHES[5]) + '\n' + "Current Value: "+ str(c.HOLES_SWITCHES[5]))
config_menu_items.append("HOLE_6_SWITCH" + '\n' + "Current Key: " + c.key_name_lookup(c.HOLES_SWITCHES[6]) + '\n' + "Current Value: "+ str(c.HOLES_SWITCHES[6]))
config_menu_items.append("HOLE_7_SWITCH" + '\n' + "Current Key: " + c.key_name_lookup(c.HOLES_SWITCHES[7]) + '\n' + "Current Value: "+ str(c.HOLES_SWITCHES[7]))
config_menu_items.append("HOLE_8_SWITCH" + '\n' + "Current Key: " + c.key_name_lookup(c.HOLES_SWITCHES[8]) + '\n' + "Current Value: "+ str(c.HOLES_SWITCHES[8]))
config_menu_items.append("HOLE_9_SWITCH" + '\n' + "Current Key: " + c.key_name_lookup(c.HOLES_SWITCHES[9]) + '\n' + "Current Value: "+ str(c.HOLES_SWITCHES[9]))
config_menu_items.append("HOLE_10_SWITCH" + '\n' + "Current Key: " + c.key_name_lookup(c.HOLES_SWITCHES[10]) + '\n' + "Current Value: "+ str(c.HOLES_SWITCHES[10]))
config_menu_items.append("HOLE_FAILURE_SWITCH" + '\n' + "Current Key: " + c.key_name_lookup(c.HOLE_FAILURE_SWITCH) + '\n' + "Current Value: "+ str(c.HOLE_FAILURE_SWITCH))

global new_keys
new_keys = []
global new_key_check
new_key_check = 0
global selected_menu
selected_menu = "main"

class ServiceMenuMode(tools.ModeBase):
    """Serves as the service menu for the game. Placeholder for now. """

    def process(self, events, pressed_keys):
        """Process the filtered list of events. """
        global current_menu

        global current_menu_item
        global selected_menu
        global menu_item_total
        global config_menu_items
        global config_menu_current_switch

        global main_menu_items
        global new_keys
        global new_key_check


        for event in events:
            if event.type == pygame.KEYDOWN:
                if selected_menu == main_menu_items[0]:
                    #print (event.key)
                    new_key_check = 1
                    if config_menu_current_switch > 0:
                        for key in new_keys:
                            if key == event.key:
                                new_key_check = 0

                    if new_key_check == 1:
                        new_keys.append(event.key)
                        config_menu_current_switch += 1

                    if config_menu_current_switch > len(config_menu_items)-1:
                        #save out changes to control config file
                        #opens controller config file, reads in values, and applies them to keys
                        control_config_file = open("control_config.txt", "w")

                        i=0
                        formatted_text = ""
                        

                        #loop through and write each line in the config file
                        while i <= len(config_menu_items)-1:
                            formatted_text = config_menu_items[i]
                            formatted_text = formatted_text[:formatted_text.find('\n')]
                            formatted_text = formatted_text +"=" + str(new_keys[i])
                            if i<len(config_menu_items)-1:
                                formatted_text = formatted_text + "=" + '\n'
                            control_config_file.write(formatted_text)
                            i+=1

                        control_config_file.close

                        #re-assign keys in the open instance of the game to match new configuration
                        c.LEFT_JOY_UP=new_keys[0]
                        c.LEFT_JOY_DOWN=new_keys[1]
                        c.RIGHT_JOY_UP=new_keys[2]
                        c.RIGHT_JOY_DOWN=new_keys[3]
                        c.LEFT_LIMIT_TOP=new_keys[4]
                        c.LEFT_LIMIT_BOTTOM=new_keys[5]
                        c.RIGHT_LIMIT_TOP=new_keys[6]
                        c.RIGHT_LIMIT_BOTTOM=new_keys[7]
                        c.START_BUTTON=new_keys[8]
                        c.SERVICE_BUTTON=new_keys[9]
                        c.TILT_SWITCH=new_keys[10]
                        c.HOLES_SWITCHES[1]=new_keys[11]
                        c.HOLES_SWITCHES[2]=new_keys[12]
                        c.HOLES_SWITCHES[3]=new_keys[13]
                        c.HOLES_SWITCHES[4]=new_keys[14]
                        c.HOLES_SWITCHES[5]=new_keys[15]
                        c.HOLES_SWITCHES[6]=new_keys[16]
                        c.HOLES_SWITCHES[7]=new_keys[17]
                        c.HOLES_SWITCHES[8]=new_keys[18]
                        c.HOLES_SWITCHES[9]=new_keys[19]
                        c.HOLES_SWITCHES[10]=new_keys[20]
                        c.HOLE_FAILURE_SWITCH=new_keys[21]
                        
                        #initialize new_keys array so that the controls can be assigned again by entering the config menu
                        new_keys = []

                        config_menu_current_switch = len(config_menu_items)-1
                        selected_menu = "main"


                if event.key == c.SERVICE_BUTTON:
                    if selected_menu=="main":
                        # Exit service menu and start to attract mode when the user presses the Service button
                        self.switch_to_mode(c.ATTRACT_MODE)
                    elif selected_menu != main_menu_items[0]:
                        # Return to service main menu if on another menu besides config
                        selected_menu = "main"
                        menu_item_total = len(main_menu_items)
                        current_menu_item = 1

                elif event.key == c.LEFT_JOY_UP:
                    # Move up in menu
                    current_menu_item -= 1
                    if current_menu_item < 1:
                        current_menu_item = menu_item_total
                elif event.key == c.LEFT_JOY_DOWN:
                    # Move down in menu
                    current_menu_item += 1
                    if current_menu_item > menu_item_total:
                        current_menu_item = 1
                elif event.key == c.START_BUTTON:
                    # Enter Selected item
                    if selected_menu == "main":
                        selected_menu = main_menu_items[current_menu_item-1]
                        if selected_menu == main_menu_items[0]:
                            #menu_item_total = len(config_menu_items)

                            ########################################
                            #######################################
                            ######### ENTER CODE HERE TO MOVE CARRIAGES
                            ######### OFF OF LIMIT SWITCHES AND LOAD BALL
                            ######### FROM TROUGH TO ROD
                            ########################################
                            #######################################

                            config_menu_current_switch = 0


                    #elif selected_menu == main_menu_items[0]:
                        #code for selecting item in main menu (config)






    def render(self, screen):
        """Render output. """

        # Fill background with blue
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((0, 0, 255))

        # MAIN MENU
        if selected_menu=="main":

            # Display menu name at top center
            font = pygame.font.Font(None, 36)
            text = font.render("Service Menu", 1, (255, 255, 255))
            textpos = text.get_rect()
            textpos.centerx = background.get_rect().centerx
            background.blit(text, textpos)
            prevpos = textpos

            # Display instructional text under previous entry - edit font size and color in the next 2 lines
            font = pygame.font.Font(None, 19)
            text = font.render("-Left Joystick to navigate", 1, (255, 255, 0))
            textpos = text.get_rect()
            textpos.top = (prevpos.bottom+2)
            textpos.left  = 50
            background.blit(text, textpos)
            prevpos = textpos

            # Display instructional text under previous entry - edit font size and color in the next 2 lines
            font = pygame.font.Font(None, 19)
            text = font.render("-Start button to enter", 1, (255, 255, 0))
            textpos = text.get_rect()
            textpos.top = (prevpos.bottom+2)
            textpos.left  = 50
            background.blit(text, textpos)
            prevpos = textpos

            # Display instructional text under previous entry - edit font size and color in the next 2 lines
            font = pygame.font.Font(None, 19)
            text = font.render("-Service button to exit", 1, (255, 255, 0))
            textpos = text.get_rect()
            textpos.top = (prevpos.bottom+2)
            textpos.left  = 50
            background.blit(text, textpos)
            prevpos = textpos

            font = pygame.font.Font(None, 19)
            text = font.render("", 1, (255, 255, 0))
            textpos = text.get_rect()
            textpos.top = (prevpos.bottom+20)
            textpos.left  = 50
            background.blit(text, textpos)
            prevpos = textpos

            #Loop through and display all main menu items
            for menu_item in main_menu_items:
                font = pygame.font.Font(None, 25)
                if current_menu_item == main_menu_items.index(menu_item)+1:
                    text = font.render("-" + menu_item, 1, (255, 255, 0))
                else:
                    text = font.render(menu_item, 1, (255, 255, 255))

                textpos = text.get_rect()
                textpos.top = (prevpos.bottom+5)
                textpos.left  = 50
                background.blit(text, textpos)
                prevpos = textpos

        #Control Config Menu
        elif selected_menu== main_menu_items[0]:
            # Display menu name at top center
            font = pygame.font.Font(None, 36)
            text = font.render("Control Config Menu", 1, (255, 255, 255))
            textpos = text.get_rect()
            textpos.centerx = background.get_rect().centerx
            background.blit(text, textpos)
            prevpos = textpos

            font = pygame.font.Font(None, 19)
            text = font.render("", 1, (255, 255, 0))
            textpos = text.get_rect()
            textpos.top = (prevpos.bottom+20)
            textpos.left  = 50
            background.blit(text, textpos)
            prevpos = textpos



            # Display instructional text under previous entry - edit font size and color in the next 2 lines
            font = pygame.font.Font(None, 25)
            text = font.render("Activate the switch for:", 1, (255, 255, 0))
            textpos = text.get_rect()
            textpos.top = (prevpos.bottom+3)
            textpos.left  = 50
            background.blit(text, textpos)
            prevpos = textpos



            #Loop through and display all config menu items

            #parse out separate strings from config_menu_items
            str_part1 = config_menu_items[config_menu_current_switch]
            str_part2 = str_part1[str_part1.find('\n'):]
            str_part1 = str_part1[:str_part1.find('\n')]
            str_part2 = str_part2[str_part2.find('\n')+1:]
            str_part3 = str_part2[str_part2.find('\n')+1:]
            str_part2 = str_part2[:str_part2.find('\n')]

            print ("string 1: " + str_part1)
            print ("string 2: " +str_part2)
            print ("string 3: " +str_part3)

            #display separate strings in meaningful way
            font = pygame.font.Font(None, 25)
            text = font.render(str_part1, 1, (255, 255, 0))
            textpos = text.get_rect()
            textpos.top = (prevpos.bottom+5)
            textpos.left  = 50
            background.blit(text, textpos)
            prevpos = textpos

            text = font.render(str_part2, 1, (0, 255, 0))
            textpos = text.get_rect()
            textpos.top = (prevpos.bottom+5)
            textpos.left  = 50
            background.blit(text, textpos)
            prevpos = textpos

            text = font.render(str_part3, 1, (0, 255, 0))
            textpos = text.get_rect()
            textpos.top = (prevpos.bottom+5)
            textpos.left  = 50
            background.blit(text, textpos)
            prevpos = textpos





            font = pygame.font.Font(None, 20)
            if new_key_check == 0 and config_menu_current_switch > 0:
                text = font.render("That switch has been used!  Try again.", 1, (255, 0, 0))
            else:
                text = font.render("", 1, (255, 0, 0))

            textpos = text.get_rect()
            textpos.top = (prevpos.bottom+5)
            textpos.left  = 50
            background.blit(text, textpos)
            prevpos = textpos







        screen.blit(background, (0, 0))
        pygame.display.flip()
