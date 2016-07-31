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

config_menu_items.append("LEFT_JOY_UP:" + pygame.key.name(c.LEFT_JOY_UP) +":"+ str(c.LEFT_JOY_UP))
config_menu_items.append("LEFT_JOY_DOWN:" + pygame.key.name(c.LEFT_JOY_DOWN) +":"+ str(c.LEFT_JOY_DOWN))
config_menu_items.append("RIGHT_JOY_UP:" + pygame.key.name(c.RIGHT_JOY_UP) +":"+ str(c.RIGHT_JOY_UP))
config_menu_items.append("RIGHT_JOY_DOWN:" + pygame.key.name(c.RIGHT_JOY_DOWN) +":"+ str(c.RIGHT_JOY_DOWN))
config_menu_items.append("LEFT_LIMIT_TOP:" + pygame.key.name(c.LEFT_LIMIT_TOP) +":"+ str(c.LEFT_LIMIT_TOP))
config_menu_items.append("LEFT_LIMIT_BOTTOM:" + pygame.key.name(c.LEFT_LIMIT_BOTTOM) +":"+ str(c.LEFT_LIMIT_BOTTOM))
config_menu_items.append("RIGHT_LIMIT_TOP:" + pygame.key.name(c.RIGHT_LIMIT_TOP) +":"+ str(c.RIGHT_LIMIT_TOP))
config_menu_items.append("RIGHT_LIMIT_BOTTOM:" + pygame.key.name(c.RIGHT_LIMIT_BOTTOM) +":"+ str(c.RIGHT_LIMIT_BOTTOM))
config_menu_items.append("START_BUTTON:" + pygame.key.name(c.START_BUTTON) +":"+ str(c.START_BUTTON))
config_menu_items.append("SERVICE_BUTTON:" + pygame.key.name(c.SERVICE_BUTTON) +":"+ str(c.SERVICE_BUTTON))
config_menu_items.append("TILT_SWITCH:" + pygame.key.name(c.TILT_SWITCH) +":"+ str(c.TILT_SWITCH))
config_menu_items.append("HOLE_1_SWITCH:" + pygame.key.name(c.HOLE_1_SWITCH) +":"+ str(c.HOLE_1_SWITCH))
config_menu_items.append("HOLE_2_SWITCH:" + pygame.key.name(c.HOLE_2_SWITCH) +":"+ str(c.HOLE_2_SWITCH))
config_menu_items.append("HOLE_3_SWITCH:" + pygame.key.name(c.HOLE_3_SWITCH) +":"+ str(c.HOLE_3_SWITCH))
config_menu_items.append("HOLE_4_SWITCH:" + pygame.key.name(c.HOLE_4_SWITCH) +":"+ str(c.HOLE_4_SWITCH))
config_menu_items.append("HOLE_5_SWITCH:" + pygame.key.name(c.HOLE_5_SWITCH) +":"+ str(c.HOLE_5_SWITCH))
config_menu_items.append("HOLE_6_SWITCH:" + pygame.key.name(c.HOLE_6_SWITCH) +":"+ str(c.HOLE_6_SWITCH))
config_menu_items.append("HOLE_7_SWITCH:" + pygame.key.name(c.HOLE_7_SWITCH) +":"+ str(c.HOLE_7_SWITCH))
config_menu_items.append("HOLE_8_SWITCH:" + pygame.key.name(c.HOLE_8_SWITCH) +":"+ str(c.HOLE_8_SWITCH))
config_menu_items.append("HOLE_9_SWITCH:" + pygame.key.name(c.HOLE_9_SWITCH) +":"+ str(c.HOLE_9_SWITCH))
config_menu_items.append("HOLE_10_SWITCH:" + pygame.key.name(c.HOLE_10_SWITCH) +":"+ str(c.HOLE_10_SWITCH))
config_menu_items.append("HOLE_FAILURE_SWITCH:" + pygame.key.name(c.HOLE_FAILURE_SWITCH) +":"+ str(c.HOLE_FAILURE_SWITCH))




global selected_menu
selected_menu = "main"

class ServiceMenuMode(tools.ModeBase):
    """Serves as the service menu for the game. Placeholder for now. """

    def ProcessInput(self, events, pressed_keys):
        """Process the filtered list of events. """
        global current_menu

        global current_menu_item
        global selected_menu
        global menu_item_total
        global config_menu_items

        global main_menu_items

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == c.SERVICE_BUTTON:
                    if selected_menu=="main":
                        # Exit service menu and start to attract mode when the user presses the Service button
                        self.SwitchToMode(c.ATTRACT_MODE)
                    else:
                        # Return to service main menu if on another menu
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
                            menu_item_total = len(config_menu_items)
                            
                    #elif selected_menu == main_menu_items[0]:
                        #code for selecting item in main menu (config)
                        
                
                


    def Render(self, screen):
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
            text = font.render("-Service button to exit to previous menu", 1, (255, 255, 0))
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

            #Loop through and display all config menu items
            for menu_item in config_menu_items:
                font = pygame.font.Font(None, 25)
                if current_menu_item == config_menu_items.index(menu_item)+1:
                    text = font.render("-" + menu_item, 1, (255, 255, 0))
                else:
                    text = font.render(menu_item, 1, (255, 255, 255))
                    
                textpos = text.get_rect()
                textpos.top = (prevpos.bottom+5)
                textpos.left  = 50
                background.blit(text, textpos)
                prevpos = textpos

            

        

        
        screen.blit(background, (0, 0))
        pygame.display.flip()
