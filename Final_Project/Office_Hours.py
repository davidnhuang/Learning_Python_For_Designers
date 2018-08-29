## - All comments from Alex are prefaced with double-#
## David - this is fantastic- really enjoyed seeing the end result here!
## It's obvious a lot of effort went into making this
## I would love to play an adventure game like this!


# David Huang
# Alexander Seropian
# Computer Science for Designers and Artists
# Version 1.1 - Alpha
# Nov 22 2017

# Imports
import pygame
import random

# INITIATIONS - DO NOT CHANGE
pygame.init() # initiates pygame module
pygame.font.init() # initiates pygame font
pygame.display.set_caption('OFFICE HOURS.exe') # sets the title for the window

# ---------- CONSTANTS ----------
## Nice use of variables to store your program's data
## Including the lists data structure for the dialogue

# font family
GAME_FONT_FAMILY = '/Users/david/Documents/GitHub/Learning-Python-For-Designers/Final_Project/uni0553-webfont.ttf'
TITLE_FONT_SIZE = 40 # largest font size 40 px for titles
SUBTITLE_FONT_SIZE = 20 # 20px for subtitles
INTERFACE_FONT_SIZE = 12 # smallest font size for ingame computer

# typography display
TITLE_DISPLAY = pygame.font.Font(GAME_FONT_FAMILY, TITLE_FONT_SIZE) # renders uni0553 at 40px
SUBTITLE_DISPLAY = pygame.font.Font(GAME_FONT_FAMILY, SUBTITLE_FONT_SIZE) # renders uni0553 at 20px
COMPUTER_DISPLAY = pygame.font.Font(GAME_FONT_FAMILY, INTERFACE_FONT_SIZE) # renders uni0553 at 12px

# game surface
SCREEN_SIZE = 800 # sets max screen size at 800 px
GAME_DISPLAY = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE)) # defines GAME_DISPLAY as a surface
GAME_EXIT = False # did user exit the game? default at False

# game initial settings
GAME_START = False # did user start game? defaults at False, which spawns starting title screen
SCENE = 0 # which scene is user on? defaults at 0, which is outside of Jerry's office

# world initial settings
OFFICE_HOURS = True # when player needs to go into the office for work
YEARS_COUNT = 0 # counts how many years Jerry has been working at company
INDOOR = False # tests if user has entered a building or not; defaults at no
OPEN_COMPUTER = False # is user using a computer right now? defaults at no
JERRY_RESPONSE = 0 # did user respond to angry customers?
INDOOR_LOCATION = [None, 'OFFICE', 'BAR', 'APARTMENT', 'CAVE'] # which building interior is the player on?
INTERIOR_BG_RENDER = INDOOR_LOCATION[0] # which interior bg is rendered
SLEEP = False # did player sleep? can only occur if OFFICE_OURS == False
TREASURE_ENDING = False # did player find the hidden treasure?
TREASURE_REQUIREMENT = False # did player meet requirements to enter the treasure cave?
BACKGROUND_NIGHT_DAY = 0 # this number determines which background URL to render; defaults at 0, which is day time
STARTING_SCREEN = True
INTRO_SCREEN = True
NOTE = False
END_OF_DAY_MESSAGE = False
HOMELESS_GUY = False

CUSTOMER_NUMBER = random.randint(0,4)

SLEEP_WINDOW = False

FIRST_CLUE_FOUND = False
SECOND_CLUE_FOUND = False
# game prompt positions
BG_POSITION = (0,0) # background render position
PROMPT_POSITION = (500, SCREEN_SIZE * 0.9) # actions prompt position
EXIT_COMPUTER_POSITION = (100, SCREEN_SIZE * 0.7) # exit out of computer
RETURN_COMPUTER_POSITION = (350, SCREEN_SIZE * 0.7)
CLOSE_ITEM_POSITION = (500, SCREEN_SIZE * 0.05)

# ingame collectables
FLASHLIGHT = False # did player find the flashlight for the cave?
KEY = False # did player find the key to open the treasure chest?

# dialogues
CUSTOMER_NAME = ['JOE:', 'MARRY:', 'KATIE:', 'JOHN:', 'MAX:'] # name of all angry customers
UI_STARTING_MESSAGE = '1 CUSTOMER CONNECTED ON THE LINE - 20 IN QUEUE' # starting message for ingame computer
# all the dialogues from the angry customers
CUSTOMER_DIALOGUE_START = ["HI, MY INSURANCE RATE HAS SKY ROCKETED, WHAT'S GOING ON?",
                           "YO, WTF IS GOING ON WITH MY INSURANCE RATE, IT DOUBLED?!?!?!",
                           "HEY CROOKS, WHAT ARE YOU DOING WITH MY INSURANCE RATE?",
                           "HELLO, I WAS AT HOSPITAL AND THEY SAY IT'S FAKE??",
                           "WHY IS MY DOCTOR SAYING NO TO THIS INSURANCE?",
                           "MY RATE IS GOING CRAZY, WHAT'S GOING ON?"]
# all the ending dialogues from angry customers before they disconnect
CUSTOMER_END = ["I'M CALLING MY LAWYER", "I'M SUING YOU GUYS", "HOW DO YOU GUYS SLEEP AT NIGHT?", "**** YOU ALL", "YOU'RE NOT HELP AT ALL"]

# Jerry's response
JERRY_CHAT_RESPONSES = ["I'm very sorry to hear that.",
                        "Unfortunately, I cannot do anything about that right now,",
                        "but I can forward this complaint to my manage, is that ok?"]

# Jerry's RETURN key changing as the conversation continues
RETURN_PROMPT = ['press RETURN to connect', 'press RETURN to respond','press RETURN to continue', 'press RETURN for next customer']
# colors default
BLACK = (0,0,0)
WHITE = (255,255,255)
SKY_BLUE = (135,206,235)
NIGHT_BLACK = (19,24,98)
GREEN = (0,255,0)

# character settings
# prompted messages
# action prompts
# E actions = ENTER / EXIT
enter_prompt = SUBTITLE_DISPLAY.render('press E to enter', False, (WHITE))
exit_prompt = SUBTITLE_DISPLAY.render('press E to exit', False, (WHITE))

# space actions - USE / INTERACT
pickup_prompt = SUBTITLE_DISPLAY.render('press SPACE to use', False, (WHITE))
sleep_prompt = SUBTITLE_DISPLAY.render('press SPACE to sleep', False, (WHITE))
note_prompt = SUBTITLE_DISPLAY.render('press SPACE to read', False, (WHITE))
talk_prompt = SUBTITLE_DISPLAY.render('press SPACE to talk', False, (WHITE))

# esc option at the bottom left hand side of Jerry's computer
exit_computer_prompt = SUBTITLE_DISPLAY.render('press ESC to exit', False, (GREEN))

# cycles through the respond options at the bottom right of the computer screen in Jerry's computer
respond_computer_prompt_1 = SUBTITLE_DISPLAY.render(RETURN_PROMPT[0], False, (GREEN))
respond_computer_prompt_2 = SUBTITLE_DISPLAY.render(RETURN_PROMPT[1], False, (GREEN))
respond_computer_prompt_3 = SUBTITLE_DISPLAY.render(RETURN_PROMPT[2], False, (GREEN))
respond_computer_prompt_4 = SUBTITLE_DISPLAY.render(RETURN_PROMPT[3], False, (GREEN))

# C option to continue the story
continue_prompt = SUBTITLE_DISPLAY.render('press C to continue', False, (WHITE))

# X key to close end of day screens
x_prompt = SUBTITLE_DISPLAY.render('press X to close', False, (WHITE))

# day end messages
end_of_day_display = SUBTITLE_DISPLAY.render('6 Hours of that later...', False, (WHITE))
# year end messages
end_of_year_display = SUBTITLE_DISPLAY.render('beep beep beep ... 8:30AM', False, (WHITE))

# computer messages
# lines that appear on the computer screen when Jerry is in his computer
computer_ui_display = COMPUTER_DISPLAY.render('connecting to customer...', False, (GREEN))
# computer login id
random_chat_id = COMPUTER_DISPLAY.render('LOGIN: 2918.2891', False, (GREEN))
# Jerry's opening lines (constant)
jerry_chat_name = COMPUTER_DISPLAY.render('Jerry', False, (GREEN))
jerry_auto_message_1 = COMPUTER_DISPLAY.render('Hi! This is Jerry From Great Credit Insurance', False, (GREEN))
jerry_auto_message_2 = COMPUTER_DISPLAY.render('How may I help you today?', False, (GREEN))
jerry_respond_message_1 = COMPUTER_DISPLAY.render(JERRY_CHAT_RESPONSES[0], False, (GREEN))
jerry_respond_message_2 = COMPUTER_DISPLAY.render(JERRY_CHAT_RESPONSES[1], False, (GREEN))
jerry_respond_message_3 = COMPUTER_DISPLAY.render(JERRY_CHAT_RESPONSES[2], False, (GREEN))

# customer
customer_chat_name = COMPUTER_DISPLAY.render(CUSTOMER_NAME[0], False, (GREEN))
customer_chat_messages = COMPUTER_DISPLAY.render(CUSTOMER_DIALOGUE_START[0], False, (GREEN))
customer_end_messages = COMPUTER_DISPLAY.render(CUSTOMER_END[0], False, (GREEN))
customer_disconnected_message = COMPUTER_DISPLAY.render('Customer has left the chatroom.', False, (GREEN))

# text locations
# ingame computer screen positions
USER_CONNECTED_POSITION = (350, SCREEN_SIZE * 0.12) # position for text 'user connected'
END_OF_DAY_POSITION = (100, SCREEN_SIZE*0.45) # position for text after user finished a day's work ingame

# x for the start of each chat bubble
CUSTOMER_CHAT_BUBBLE = 100
JERRY_CHAT_BUBBLE = 100

# line coordinates on ingame computer screen
COMPUTER_LINE_0 = (JERRY_CHAT_BUBBLE, SCREEN_SIZE * 0.13)
COMPUTER_LINE_1 = (JERRY_CHAT_BUBBLE, SCREEN_SIZE * 0.2) # line 1 on computer screen
COMPUTER_LINE_2 = (JERRY_CHAT_BUBBLE, SCREEN_SIZE * 0.22) # line 2 on computer screen
COMPUTER_LINE_3 = (CUSTOMER_CHAT_BUBBLE, SCREEN_SIZE * 0.26) # line 3 on computer screen
COMPUTER_LINE_4 = (CUSTOMER_CHAT_BUBBLE, SCREEN_SIZE * 0.28) # line 4 on computer screen
COMPUTER_LINE_5 = (JERRY_CHAT_BUBBLE, SCREEN_SIZE * 0.32) # line 5 on computer screen
COMPUTER_LINE_6 = (JERRY_CHAT_BUBBLE, SCREEN_SIZE * 0.34) # line 6 on computer screen
COMPUTER_LINE_7 = (JERRY_CHAT_BUBBLE, SCREEN_SIZE * 0.36) # line 7 on computer screen
COMPUTER_LINE_8 = (JERRY_CHAT_BUBBLE, SCREEN_SIZE * 0.38) # line 8 on computer screen
COMPUTER_LINE_9 = (CUSTOMER_CHAT_BUBBLE, SCREEN_SIZE * 0.42) # line 9 on computer screen
COMPUTER_LINE_10 = (CUSTOMER_CHAT_BUBBLE, SCREEN_SIZE * 0.44) # line 10 on computer screen
COMPUTER_LINE_11 = (CUSTOMER_CHAT_BUBBLE, SCREEN_SIZE * 0.60)

# backgrounds (EX = exterior, IN = interior, FO = foreground)
# outdoor background (office hours)
#----- 6.0 PNGs -----#
# TODO - RENDERING LOCATION (CHANGE THIS PATH TO WHERE YOU SAVED THE GAME DIRECTORY)
GAME_DIRECTORY = '/Users/david/Documents/GitHub/Learning-Python-For-Designers/Final_Project'

# 6.1 player Character
# Jerry Sprite facing right
JERRY_R = GAME_DIRECTORY + '/assets/character/jerry_right-01.png'
# Jerry Sprite facing left
JERRY_L = GAME_DIRECTORY + '/assets/character/jerry_left-01.png'

# 6.2 world character
HOMELESS_GUY_PNG = GAME_DIRECTORY + '/assets/character/homeless_guy-01.png'

# 6.2 background PNG
# 6.2.1 outdoor environment
OFFICE_EX_BG = GAME_DIRECTORY + '/assets/BG/Office_exterior.png'
BAR_EX_BG = GAME_DIRECTORY + '/assets/BG/Bar_exterior.png'
APARTMENT_EX_BG = GAME_DIRECTORY + '/assets/BG/Apartment_exterior.png'
FOREST_1 = GAME_DIRECTORY + '/assets/BG/Forest_1.png'
FOREST_2 = GAME_DIRECTORY + '/assets/BG/Forest_2.png'
FOREST_3 = GAME_DIRECTORY + '/assets/BG/Forest_3.png'
CAVE = GAME_DIRECTORY + '/assets/BG/Cave.png'
TREASURE_END = GAME_DIRECTORY + '/assets/BG/Cave_3.png'
CITY_END = GAME_DIRECTORY + '/assets/BG/End_of_city.png'
HIGHWAY_END = GAME_DIRECTORY + '/assets/BG/Highway_end.png'
BUS_STOP_BG = [GAME_DIRECTORY + '/assets/BG/Bus_stop.png',
               GAME_DIRECTORY + '/assets/BG/Bus_stop_a.png']
HIGHWAY_1 = [GAME_DIRECTORY + '/assets/BG/Highway_1.png',
             GAME_DIRECTORY + '/assets/BG/Highway_1_a.png']
HIGHWAY_2 = [GAME_DIRECTORY + '/assets/BG/Highway_2.png',
             GAME_DIRECTORY + '/assets/BG/Highway_2_a.png']

# 6.2.2 indoor environment
OFFICE_INTERIOR_1 = GAME_DIRECTORY + '/assets/BG/Inside_Office_1_A.png'
OFFICE_INTERIOR_2 = [GAME_DIRECTORY + '/assets/BG/Inside_Office_2.png',
                     GAME_DIRECTORY + '/assets/BG/Inside_Office_2_A.png']
OFFICE_INTERIOR_3 = [GAME_DIRECTORY + '/assets/BG/Inside_Office_3.png',
                     GAME_DIRECTORY + '/assets/BG/Inside_Office_3_A.png']
OFFICE_END = [GAME_DIRECTORY + '/assets/BG/Office_End.png',
              GAME_DIRECTORY + '/assets/BG/Office_End_a.png']
BAR_INTERIOR = [GAME_DIRECTORY + '/assets/BG/Bar_interior.png',
                GAME_DIRECTORY + '/assets/BG/Bar_interior_afterwork.png']
APARTMENT_INTERIOR = [GAME_DIRECTORY + '/assets/BG/Apartment_Interior.png',
                       GAME_DIRECTORY + '/assets/BG/Apartment_Interior_a.png']
COMPUTER_SCREEN = GAME_DIRECTORY + '/assets/BG/Screen.png'

# 6.2.3 foreground
FO_LAMPS = GAME_DIRECTORY + '/assets/BG/foreground_lamp-01.png'
FO_BUS_STOP = GAME_DIRECTORY + '/assets/BG/Bus_stop_FO.png'
FO_CITY_END = GAME_DIRECTORY + '/assets/BG/City_end_FO.png'
FO_ROAD_END = GAME_DIRECTORY + '/assets/BG/Road_End_FO.png'
FO_FOREST_1 = GAME_DIRECTORY + '/assets/BG/Forest_1_FO.png'
FO_FOREST_2 = GAME_DIRECTORY + '/assets/BG/Forest_2_FO.png'
FO_FOREST_3 = GAME_DIRECTORY + '/assets/BG/Forest_3_FO.png'
FO_CAVE = GAME_DIRECTORY + '/assets/BG/Cave_FO.png'

# 6.2.4 in-game Obj
WATER_COOLER_NOTE = GAME_DIRECTORY + '/assets/Obj/water_cooler_note.png'
GET_OUT_NOTE = GAME_DIRECTORY + '/assets/Obj/homeless_note.png'
FIRST_CLUE = GAME_DIRECTORY + '/assets/Obj/first_clue.png'
SECOND_CLUE = GAME_DIRECTORY + '/assets/Obj/second_clue.png'
FLASHLIGHT_PNG = GAME_DIRECTORY + '/assets/Obj/flashlight.png'
KEY_PNG = GAME_DIRECTORY + '/assets/Obj/key.png'
MOMS_NOTE = GAME_DIRECTORY + '/assets/Obj/mom_note.png'
BAR_MENU = GAME_DIRECTORY + '/assets/Obj/bar_menu.png'

# 6.2.5 game screens
STARTING_SCREEN_PNG = GAME_DIRECTORY + '/assets/BG/starting.png'
INTRO_SCREEN_PNG = GAME_DIRECTORY + '/assets/BG/intro.png'

GOOD_ENDING_SCREEN = GAME_DIRECTORY + '/assets/BG/Good_Ending.png'
POOR_ENDING_SCREEN = GAME_DIRECTORY + '/assets/BG/Poor_Ending.png'


# character positioning
JERRY_X = SCREEN_SIZE * 0.3 # initial position of Jerry
JERRY_Y = SCREEN_SIZE * 0.5 # initial position of Jerry

JERRY_X_IN = 50 # initial position of Jerry Indoor
JERRY_Y_IN = SCREEN_SIZE * 0.4 # initial position of Jerry Indoor

CHARACTER_DIR = True # character facing right by default; True = right, False = left

HOMELESS_X = SCREEN_SIZE * 0.2
HOMELESS_Y = SCREEN_SIZE * 0.49

# screen limits to trigger scene change
# outdoor
SCREEN_MAX = SCREEN_SIZE - 40 # right bound that would trigger scene change
SCREEN_MIN = 10 # left bound that would trigger scene change

# indoor
SCREEN_MAX_IN = SCREEN_SIZE - 100 # right bound that would trigger scene change
SCREEN_MIN_IN = 10 # left bound that would trigger scene change

# movement
dx = 0
dy = 0

STOP = 0 # stops player movement when he / she is near the boundary

# box range that would trigger prompts or interactions
door_range_min = 280 # right side of the office door
door_range_max = 380 # left side of the office door

bar_door_range_min = 280 # right side of the bar door
bar_door_range_max = 380 # left side of the bar door

apartment_door_min = 250 # right side of the apartment door
apartment_door_max = 550 # left side of the apartment door

forest_entry_min = 0 # right side of the forest entry
forest_entry_max = 500 # left side of the forest entry

flash_light_min = 600
flash_light_max = 700
# indoor
office_exit_min = 0 # right side of the office exit
office_exit_max = 150 # left side of the office exit

bar_exit_min = 0 # right side of the bar exit
bar_exit_max = 150 # left side of the bar exit

apartment_exit_min = 0 # right side of the apartment exit
apartment_exit_max = 150 # left side of the apartment exit

moms_note_min = 150
moms_note_max = 250

computer_min = 220 # right side of the computer
computer_max = 350 # left side of the computer

homeless_box_min = SCREEN_SIZE * 0.15 # right side of the homeless man
homeless_box_max = SCREEN_SIZE * 0.25 # left side of the homeless man

menu_min = 250
menu_max = 350

first_clue_min = 250
first_clue_max = 350

second_clue_min = 400
second_clue_max = 500

key_min = 250
key_max = 350
# Game Boundaries
# indoor
# stopping point in the office
office_exit_stop = 60
water_cooler_stop = 550
# stopping point in the bar
bar_exit_stop = 60
bar_bartender_stop = 450
# stopping point in the apartment
apartment_exit_stop = 40
bed_stop = 500
# outdoor
# stopping point on the city street
highway_stop = 510
city_stop = 600
cave_entrance = 100
treasure_chest = 100
no_turning_back = SCREEN_SIZE - 100


# ---------- FUNCTIONS ----------
# Background Functions
def skybox(): # fills the screen with sky blue, simulating sky
    if OFFICE_HOURS == True: # if it is during the day
        GAME_DISPLAY.fill(SKY_BLUE) # render a blue skye
    else: # if it is at night
        GAME_DISPLAY.fill(NIGHT_BLACK) # render a night sky

def bg_render(BG_NAME): # this function renders backgrounds based on PNG names
    png_img = pygame.image.load(BG_NAME) # load the background image
    GAME_DISPLAY.blit(png_img, BG_POSITION) # display the image as a background

## one improvement might be to store your images in list and use the scene ID as an index into the list to draw it
## then you wouldn't need to have this really long if-elif chain
def backdrop_change(): # this function changes the background based on which scene the player is in
    if INDOOR == False: # if the player is outdoors
        # within the city
        if SCENE == 0: # starting position of the game
            bg_render(OFFICE_EX_BG)
        elif SCENE == 1: # outside the bar
            bg_render(BAR_EX_BG)
        elif SCENE == 2: # outside Jerry's apartment
            bg_render(APARTMENT_EX_BG)
        elif SCENE == 3: # at the end of the city street
            bg_render(CITY_END)
        # outside the city
        elif SCENE == -1: # bus stop
            bg_render(BUS_STOP_BG[BACKGROUND_NIGHT_DAY])
        elif SCENE == -2: # first segment of the highway
            bg_render(HIGHWAY_1[BACKGROUND_NIGHT_DAY])
        elif SCENE == -3: # second segment of the highway
            bg_render(HIGHWAY_2[BACKGROUND_NIGHT_DAY])
        elif SCENE == -4: # end of the road
            bg_render(HIGHWAY_END)
        elif SCENE == -5: # start of the forest
            bg_render(FOREST_1)
        elif SCENE == -6: # second part of the forest
            bg_render(FOREST_2)
        elif SCENE == -7: # outside the cave
            bg_render(FOREST_3)
        elif SCENE == -8: # the treasure
            bg_render(CAVE)
    else: # if the player is indoor
        if INTERIOR_BG_RENDER == 'OFFICE':
            if SCENE == 0:
                bg_render(OFFICE_INTERIOR_1)
            elif SCENE == 1:
                bg_render(OFFICE_INTERIOR_2[BACKGROUND_NIGHT_DAY])
            elif SCENE == 2:
                bg_render(OFFICE_INTERIOR_3[BACKGROUND_NIGHT_DAY])
            elif SCENE == 3:
                bg_render(OFFICE_END[BACKGROUND_NIGHT_DAY])
        elif INTERIOR_BG_RENDER == 'BAR':
            if SCENE == 1:
                bg_render(BAR_INTERIOR[BACKGROUND_NIGHT_DAY])
        elif INTERIOR_BG_RENDER == 'APARTMENT':
            if SCENE == 2:
                bg_render(APARTMENT_INTERIOR[BACKGROUND_NIGHT_DAY])

def homeless_blit(): # renders the homeless man
    if INDOOR == False and SCENE == 2: # near Jerry's apartment
            GAME_DISPLAY.blit(pygame.image.load(HOMELESS_GUY_PNG), (HOMELESS_X, HOMELESS_Y)) # this is what he looks like

def foreground(): # renders foreground elements
    if INDOOR == False: # if player is outdoor
        if SCENE == 0 or SCENE == 1 or SCENE == 2: # renders lamps on the street
            bg_render(FO_LAMPS)
        elif SCENE == 3:  # renders the stop sign
            bg_render(FO_CITY_END)
        elif SCENE == -1: # renders the bus bench
            bg_render(FO_BUS_STOP)
            bg_render(FO_LAMPS)
        elif SCENE == -4: # renders the road end sign
            bg_render(FO_ROAD_END)
        elif SCENE == -5:
            bg_render(FO_FOREST_1)
        elif SCENE == -6:
            bg_render(FO_FOREST_2)
        elif SCENE == -7:
            bg_render(FO_FOREST_3)
        elif SCENE == -8:
            bg_render(FO_CAVE)

def char_render(x, y, in_x, in_y):  # renders character sprite
    if INDOOR == False:  # if player is outdoors
        if CHARACTER_DIR == True:  # if player is facing the right
            char_png = pygame.image.load(JERRY_R)  # render Jerry facing right
            GAME_DISPLAY.blit(char_png, (x, y))  # blit at x,y
        else:  # if player is facing the left
            char_png = pygame.image.load(JERRY_L)  # render Jerry facing left
            GAME_DISPLAY.blit(char_png, (x, y))  # blit at x,y
    elif INDOOR == True:  # if player is indoor
        if CHARACTER_DIR == True:  # if player is facing the right
            char_png = pygame.image.load(JERRY_R)  # load Jerry facing right
            enlarge_char_png = pygame.transform.scale(char_png, (250, 250))  # enlarge png model
            GAME_DISPLAY.blit(enlarge_char_png, (in_x, in_y))  # blit enlarged png to x,y
        else:  # if player is facing the left
            char_png = pygame.image.load(JERRY_L)  # load Jerry facing left
            enlarge_char_png = pygame.transform.scale(char_png, (250, 250))  # enlarge png model
            GAME_DISPLAY.blit(enlarge_char_png, (in_x, in_y))  # blit enlarge png to x,y


# PROMPTED MESSAGE FUNCTIONS
## I like that you have a message system/function

def prompt(msg): # blits action prompt on the lower half of the screen
    GAME_DISPLAY.blit(msg, PROMPT_POSITION) # render the prompted message at the lower right hand side

def blit_prompt(msg, position): # more flexible prompt function where user can define what message and where it is rendered
    GAME_DISPLAY.blit(msg, position) # render the message at a specific position

def prompt_display(): # blits a display at a specific location on the screen
    if INDOOR == False: # if player is outdoor
        if SCENE == 0 or SCENE == 1: # if he is outside the office or outside the bar
            door_prompt = collision(JERRY_X, door_range_min, door_range_max) # is Jerry about to enter the bar or the office?
            if door_prompt == True: # if Jerry is inside that box
                prompt(enter_prompt) # print the prompt to enter on the lower right hand side
        elif SCENE == 2: # if he is outside his apartment
            apartment_prompt = collision(JERRY_X, apartment_door_min, apartment_door_max) # is Jerry about to enter the apartment?
            homeless_man_box = collision(JERRY_X, homeless_box_min, homeless_box_max)
            if apartment_prompt == True: # if Jerry is inside that box
                prompt(enter_prompt) # print the prompt to enter on the lower right hand side
            elif homeless_man_box == True and HOMELESS_GUY == False: # if Jerry passes by the homeless man
                prompt(talk_prompt) # show talk prompt
        elif SCENE == -2:
            first_clue_prompt = collision(JERRY_X,first_clue_min, first_clue_max)
            if first_clue_prompt == True and HOMELESS_GUY == True:
                prompt(note_prompt)
        elif SCENE == -3:
            second_clue_prompt = collision(JERRY_X,second_clue_min,second_clue_max)
            if second_clue_prompt == True and HOMELESS_GUY == True:
                prompt(note_prompt)
        elif SCENE == -4: # if Jerry is right outside the forest
            forest_entry_prompt = collision(JERRY_X, forest_entry_min, forest_entry_max) # is Jerry about to enter the forest?
            flash_light_found = collision(JERRY_X, flash_light_min, flash_light_max)
            if forest_entry_prompt == True and HOMELESS_GUY == True: # if Jerry is inside that box
                prompt(enter_prompt) # print the prompt to enter the lower right hand side
            elif flash_light_found == True and HOMELESS_GUY == True and FLASHLIGHT == False:
                prompt(pickup_prompt)
        elif SCENE == -6:
            key_found = collision(JERRY_X, key_min, key_max)
            if key_found == True and HOMELESS_GUY == True and KEY == False:
                prompt(pickup_prompt)
        elif SCENE == -7:
            cave_entry_found = collision(JERRY_X, 0,cave_entrance)
            if KEY == True and FLASHLIGHT == True and cave_entry_found == True:
                prompt(enter_prompt)
        elif SCENE == -8:
            near_treasure = collision(JERRY_X, 0, treasure_chest)
            if KEY == True and FLASHLIGHT == True and near_treasure == True:
                prompt(pickup_prompt)
    else: # if player is indoor
        if INTERIOR_BG_RENDER == 'OFFICE': # if player is in the first office scene
            if SCENE == 0: # if Jerry is at the first segment of the office
                # if he is right in front of his computer and it is during office hours
                if computer_min <= JERRY_X_IN <= computer_max and OFFICE_HOURS == True:
                    prompt(pickup_prompt) # print the prompt at the lower right hand side
                elif office_exit_min <= JERRY_X_IN <= office_exit_max: # else if he is near the exit
                    prompt(exit_prompt) # print exit prompt
            elif SCENE == 3: # if he is near the water cooler
                if SCREEN_SIZE > JERRY_X_IN > water_cooler_stop: # is he near the note on the water cooler?
                    prompt(note_prompt) # print the prompt on the lower right hand side
        elif SCENE == 1 and INTERIOR_BG_RENDER == 'BAR': # if player is in the bar interior
            if bar_exit_min <= JERRY_X_IN <= bar_exit_max: # if player is within exit range
                prompt(exit_prompt) # print exit prompt
            if menu_min <= JERRY_X_IN <= menu_max:
                prompt(note_prompt)
        elif SCENE == 2 and INTERIOR_BG_RENDER == 'APARTMENT': # if Jerry is in the apartment
            if apartment_exit_min <= JERRY_X_IN <= apartment_exit_max: # if he is within exit range
                prompt(exit_prompt) # print exit prompt
            # is Jerry near his bed and he is done with work?
            elif SCREEN_SIZE > JERRY_X_IN > bed_stop and OFFICE_HOURS == False:
                prompt(sleep_prompt) # print prompt at the lower right hand side
            elif moms_note_max > JERRY_X_IN > moms_note_min:
                prompt(note_prompt)

def collision(char_x, target_box_min, target_box_max):  # detects collision between player and object
    if target_box_min <= char_x <= target_box_max:  # if player enters the hit box of target object
        return True  # collision has happened
    else:
        return False  # no collision detected

# COMPUTER INTERFACE FUNCTIONS IN JERRY'S OFFICE
def open_computer_interface(): # opens the computer terminal
    if OPEN_COMPUTER == True and OFFICE_HOURS == True: # when Jerry is on his computer
        bg_render(COMPUTER_SCREEN) # display computer UI
        blit_prompt(random_chat_id, COMPUTER_LINE_0) # print LOGIN information of Jerry
        blit_prompt(exit_computer_prompt, EXIT_COMPUTER_POSITION)# render computer screen UI
def chat_bubble_auto(): # renders chat bubbles when Jerry is on his computer
    if OPEN_COMPUTER == True: # if Jerry is on his computer
        if JERRY_RESPONSE >= 0: # auto message that Jerry sends out to customers
            blit_prompt(jerry_auto_message_1, COMPUTER_LINE_1) # Jerry name
            blit_prompt(jerry_auto_message_2, COMPUTER_LINE_2) # Jerry's automated hello message
            CUSTOMER_NUMBER = YEARS_COUNT
            return CUSTOMER_NUMBER
def chat_bubble_2(YEARS_COUNT):
    if JERRY_RESPONSE >= 1: # once User presses CONTINUE
        blit_prompt(COMPUTER_DISPLAY.render(CUSTOMER_NAME[YEARS_COUNT], False, (GREEN)), COMPUTER_LINE_3) # customer name
        blit_prompt(COMPUTER_DISPLAY.render(CUSTOMER_DIALOGUE_START[YEARS_COUNT], False, (GREEN)), COMPUTER_LINE_4) # customer angry concern
def chat_bubble_3():
    if JERRY_RESPONSE >= 2: # once User responds to the concern
        blit_prompt(jerry_chat_name, COMPUTER_LINE_5) # Jerry name
        blit_prompt(jerry_respond_message_1, COMPUTER_LINE_6) # Jerry's response
        blit_prompt(jerry_respond_message_2, COMPUTER_LINE_7)
        blit_prompt(jerry_respond_message_3, COMPUTER_LINE_8)
def chat_bubble_4(YEARS_COUNT):
    if JERRY_RESPONSE >= 3: # once Jerry responds
        blit_prompt(COMPUTER_DISPLAY.render(CUSTOMER_NAME[YEARS_COUNT], False, (GREEN)), COMPUTER_LINE_9) # customer name
        blit_prompt(COMPUTER_DISPLAY.render(CUSTOMER_END[YEARS_COUNT], False, (GREEN)), COMPUTER_LINE_10) # customer's angry remark to Jerry's lack of helpfulness
        blit_prompt(customer_disconnected_message, COMPUTER_LINE_11) # shows that customer disconnected
def change_respond_prompt(): # this function changes the RETURN prompt when Jerry is using his computer
    if JERRY_RESPONSE == 0: # if Jerry just started his computer
        blit_prompt(respond_computer_prompt_1, RETURN_COMPUTER_POSITION) # display this prompt
    elif JERRY_RESPONSE == 1: # if customer responded
        blit_prompt(respond_computer_prompt_2, RETURN_COMPUTER_POSITION) # display this prompt
    elif JERRY_RESPONSE == 2: # if Jerry responds again
        blit_prompt(respond_computer_prompt_3, RETURN_COMPUTER_POSITION) #
    elif JERRY_RESPONSE == 3:
        blit_prompt(respond_computer_prompt_4, RETURN_COMPUTER_POSITION)
def chat_dialogues(YEARS_COUNT): # displays all the dialogue between Jerry and Customer on the computer screen
    if OPEN_COMPUTER == True and OFFICE_HOURS == True and INDOOR == True and INTERIOR_BG_RENDER == 'OFFICE':
        chat_bubble_auto() # display the automated message Jerry puts out everytime
        chat_bubble_2(YEARS_COUNT) # changes user's name based on the year Jerry has been working
        chat_bubble_3() # display Jerry's automatic message
        chat_bubble_4(YEARS_COUNT) # changes user's name base on the year Jerry has been working
        change_respond_prompt()

# Obj found / notes
def world_Obj():
    if INDOOR == True:
        water_cooler_note = collision(JERRY_X_IN, water_cooler_stop, SCREEN_SIZE)
        moms_note = collision(JERRY_X_IN, moms_note_min, moms_note_max)
        menu_note = collision(JERRY_X_IN, menu_min, menu_max)
        if SCENE == 3 and INTERIOR_BG_RENDER == 'OFFICE':
            if water_cooler_note == True and NOTE == True:
                bg_render(WATER_COOLER_NOTE)
                blit_prompt(x_prompt,CLOSE_ITEM_POSITION)
        elif SCENE == 2 and INTERIOR_BG_RENDER == 'APARTMENT':
            if moms_note == True and NOTE == True:
                bg_render(MOMS_NOTE)
                blit_prompt(x_prompt,CLOSE_ITEM_POSITION)
        elif SCENE == 1 and INTERIOR_BG_RENDER == 'BAR':
            if menu_note == True and NOTE == True:
                bg_render(BAR_MENU)
                blit_prompt(x_prompt,CLOSE_ITEM_POSITION)
    else:
        homeless_man_note = collision(JERRY_X, homeless_box_min, homeless_box_max)
        first_clue_note = collision(JERRY_X, first_clue_min, first_clue_max)
        second_clue_note = collision(JERRY_X, second_clue_min, second_clue_max)
        key_found = collision(JERRY_X, key_min, key_max)
        treasure_found = collision(JERRY_X,0,treasure_chest)
        if homeless_man_note == True and NOTE == True:
            bg_render(GET_OUT_NOTE)
            blit_prompt(x_prompt,CLOSE_ITEM_POSITION)
        elif first_clue_note == True and NOTE == True and SCENE == -2:
            bg_render(FIRST_CLUE)
            blit_prompt(x_prompt,CLOSE_ITEM_POSITION)
        elif second_clue_note == True and NOTE == True and SCENE == -3:
            bg_render(SECOND_CLUE)
            blit_prompt(x_prompt,CLOSE_ITEM_POSITION)
        elif SCENE == -4 and NOTE == True:
            bg_render(FLASHLIGHT_PNG)
            blit_prompt(x_prompt,CLOSE_ITEM_POSITION)
        elif key_found == True and SCENE == -6 and NOTE == True:
            bg_render(KEY_PNG)
            blit_prompt(x_prompt,CLOSE_ITEM_POSITION)

def cave_entry():
    if KEY == True and FLASHLIGHT == True:
        TREASURE_REQUIREMENT = True
        return TREASURE_REQUIREMENT

# Text screens at the end of the year and the end of the day
def end_of_day_message():
    GAME_DISPLAY.fill(BLACK)
    blit_prompt(end_of_day_display, END_OF_DAY_POSITION)
    prompt(x_prompt)

def new_day():
    if SLEEP == True: # when Jerry is asleep
        GAME_DISPLAY.fill(BLACK)
        blit_prompt(end_of_year_display, END_OF_DAY_POSITION)
        prompt(x_prompt)

def starting_screen():
    if STARTING_SCREEN == True:
        bg_render(STARTING_SCREEN_PNG)

def intro_screen():
    if STARTING_SCREEN == False and INTRO_SCREEN == True:
        bg_render(INTRO_SCREEN_PNG)

def ending(): # determines the ending of the game
    if YEARS_COUNT == 4:
        bg_render(POOR_ENDING_SCREEN)
    elif TREASURE_ENDING == True:
        GAME_DISPLAY.fill(WHITE)
        bg_render(GOOD_ENDING_SCREEN)

# ============================================== MAIN LOOP ==============================================
while not GAME_EXIT:
    for event in pygame.event.get(): # check all the user inputs on the key pad
        # ======== KEYBOARD COMMANDS ========
        # WINDOW CLOSE
        if event.type == pygame.QUIT:
            GAME_EXIT = True # quit out the game
        # KEY PRESS
        if event.type == pygame.KEYDOWN: # detects whether there has been a key press input
            # left arrow - MOVING
            if event.key == pygame.K_LEFT: # if it is the left arrow key
                CHARACTER_DIR = False # turn the character to the left
                dx = -10
            # right arrow - MOVING
            elif event.key == pygame.K_RIGHT: # if it is the right arrow key
                CHARACTER_DIR = True # turn the character to the right
                dx = 10  # move x to the right by 10 pixels per input
            # e key - ENTER OR EXIT BUILDINGS
            elif event.key == pygame.K_e:
                ## would be nice to put the enter and use code in their own functions to clean up this main loop a bit
                # detections outdoor
                # detects whether Jerry is near the office entrance in order to open it and go in
                office_entrance_door = collision(JERRY_X, door_range_min, door_range_max)
                bar_entrance_door = collision(JERRY_X, bar_door_range_min, bar_door_range_max)
                apartment_entrance_door = collision(JERRY_X, apartment_door_min, apartment_door_max)
                forest_entry_way = collision(JERRY_X, forest_entry_min, forest_entry_max)
                cave_entry_found = collision(JERRY_X, 0, cave_entrance)
                # detections indoor
                # detects whether Jerry is near the office exit to leave the building
                office_exit_door = collision(JERRY_X_IN, office_exit_min, office_exit_max)
                bar_exit_door = collision(JERRY_X_IN, bar_exit_min, bar_exit_max)
                apartment_exit_door = collision(JERRY_X_IN, apartment_exit_min, apartment_exit_max)
                if INDOOR == False: # if Jerry is outside
                    if SCENE == 0: # if Jerry is right outside the office
                        if office_entrance_door == True: # if he is near the office entrance
                            INDOOR = True # upon keypress, Jerry enters the building
                            INTERIOR_BG_RENDER = INDOOR_LOCATION[1] # Jerry is indoor in the first segment of the office
                    elif SCENE == 1 and bar_entrance_door == True: # if Jerry is right outside the local bar
                        INDOOR = True # upon keypress, Jerry enters the building
                        INTERIOR_BG_RENDER = INDOOR_LOCATION[2] # Jerry is indoor in the bar
                    elif SCENE == 2: # if Jerry is right outside his apartment
                        if apartment_entrance_door == True:
                            INDOOR = True # upon keypress, Jerry enters the building
                            INTERIOR_BG_RENDER = INDOOR_LOCATION[3] # Jerry is inside his apartment room
                    elif SCENE == -4 and forest_entry_way == True: # if Jerry is near the entry way of the forest
                        SCENE = -5 # upon keypress, he journeys into the woods
                        JERRY_X += 100
                    elif SCENE == -7 and cave_entry_found == True:
                        if KEY == True and FLASHLIGHT == True:
                            SCENE = -8
                            JERRY_X = SCREEN_SIZE - 100
                else: # if Jerry is inside already
                    if SCENE == 0 and INTERIOR_BG_RENDER == 'OFFICE': # if he is in the first segment of the office
                        if office_exit_door == True: # if he is near the office exit
                            INDOOR = False # upon keypress, Jerry leaves the building
                            INTERIOR_BG_RENDER = INDOOR_LOCATION[0] # reset the indoor background
                    elif SCENE == 1 and INTERIOR_BG_RENDER == 'BAR': # if he is in the bar
                        if bar_exit_door == True: # if he is near the bar exit
                            INDOOR = False # upon keypress Jerry leaves the building
                            INTERIOR_BG_RENDER = INDOOR_LOCATION[0] # reset the indoor background
                    elif SCENE == 2 and INTERIOR_BG_RENDER == 'APARTMENT': # if he is inside his room
                        if apartment_exit_door == True: # if he is near the door of his room
                            INDOOR = False # upon keypress, Jerry leaves the building
                            INTERIOR_BG_RENDER = INDOOR_LOCATION[0] # reset the indoor background
            # SPACE KEY - USE / READ Obj / INTERACTING WITH THE WORLD
            elif event.key == pygame.K_SPACE:
                # indoor
                computer_open = collision(JERRY_X_IN, computer_min, computer_max)
                near_bed = collision(JERRY_X_IN, bed_stop, SCREEN_SIZE)
                water_cooler_read = collision(JERRY_X_IN, water_cooler_stop, SCREEN_SIZE)
                homeless_box = collision(JERRY_X, homeless_box_min, homeless_box_max)
                moms_note = collision(JERRY_X_IN,moms_note_min, moms_note_max)
                menu_note = collision(JERRY_X_IN, menu_min, menu_max)
                # outdoor
                first_clue_box = collision(JERRY_X,first_clue_min,first_clue_max)
                second_clue_box = collision(JERRY_X,second_clue_min,second_clue_max)
                flashlight_box = collision(JERRY_X, flash_light_min, flash_light_max)
                key_box = collision(JERRY_X, key_min, key_max)
                treasure_box = collision(JERRY_X, 0, treasure_chest)
                if INDOOR == True: # if Jerry is inside
                    # if Jerry is in his office, during work hours and near his computer
                    if INTERIOR_BG_RENDER == 'OFFICE' and SCENE == 0 and computer_open == True and OFFICE_HOURS == True:
                        OPEN_COMPUTER = True # upon keypress Jerry opens his computer
                    elif SCENE == 2 and OFFICE_HOURS == False and near_bed == True:
                        SLEEP = True
                    elif SCENE == 3 and INTERIOR_BG_RENDER == 'OFFICE':
                        if water_cooler_read == True:
                            NOTE = True
                    elif SCENE == 1 and INTERIOR_BG_RENDER == 'BAR':
                        if menu_note == True:
                            NOTE = True
                    elif SCENE == 2 and INTERIOR_BG_RENDER == 'APARTMENT':
                        if moms_note == True:
                            NOTE = True
                else:
                    if SCENE == 2 and homeless_box == True:
                        HOMELESS_GUY = True
                        NOTE = True
                    elif SCENE == -2 and first_clue_box == True:
                        FIRST_CLUE_FOUND = True
                        NOTE = True
                    elif SCENE == -3 and second_clue_box == True:
                        SECOND_CLUE_FOUND = True
                        NOTE = True
                    elif SCENE == -4 and flashlight_box == True:
                        FLASHLIGHT = True
                        NOTE = True
                    elif SCENE == -6 and key_box == True:
                        KEY = True
                        NOTE = True
                    elif SCENE == -8 and treasure_box == True:
                        TREASURE_ENDING = True
            # RETURN KEY - ONLY USED WHEN JERRY IS USING HIS COMPUTER TO SEND RESPONSES
            elif event.key == pygame.K_RETURN:
                if OPEN_COMPUTER == True: # when Jerry is in front of his computer
                    JERRY_RESPONSE += 1 # upon keypress, he types and responds to customers
            # ESC KEY - ONLY USED WHEN JERRY IS USING HIS COMPUTER
            elif event.key == pygame.K_ESCAPE:
                if OPEN_COMPUTER == True: # if Jerry is in front of his computer
                    OPEN_COMPUTER = False # upon keypress, he exits his computer screen
            # X KEY - CLOSE WINDOWS / TITLE CARDS
            elif event.key == pygame.K_x: # this resets the day
                if SLEEP == True: # if Jerry is asleep and is waken by his alarm clock
                    SLEEP = False # upon keypress, he wakes up and starts a new day
                    YEARS_COUNT += 1
                    BACKGROUND_NIGHT_DAY = 0
                    OFFICE_HOURS = True
                elif NOTE == True:
                    NOTE = False
                elif END_OF_DAY_MESSAGE == True:
                    END_OF_DAY_MESSAGE = False
                    JERRY_RESPONSE = 0
            # S KEY - STARTING SCREENS
            elif event.key == pygame.K_s:
                if STARTING_SCREEN == True:
                    STARTING_SCREEN = False
                elif STARTING_SCREEN == False and INTRO_SCREEN == True:
                    INTRO_SCREEN = False
        # KEY RELEASES
        if event.type == pygame.KEYUP: # detects if the user has released a keypress
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: # whenever an arrow key is released
                dx = 0 # stop the x changes of the character; prevent the character from moving indefinitely
                dy = 0 # stop the y changes in the character; prevent the character from moving indefinitely

    # ======== JERRY MOVEMENT ========
    if INDOOR == False: # if Jerry is outdoor
        JERRY_X += dx # add movement to Jerry's position
    else: # if Jerry is indoor
        JERRY_X_IN += (dx*2) # add movement at a quicker pace

    # ======== SCENE CHANGERS ========
    if INDOOR == False: # if the player is outdoor
        if JERRY_X >= SCREEN_MAX: # if Jerry comes to 40px from the right side of the screen
            JERRY_X = 15 # reset Jerry to the left at 10px
            SCENE += 1 # change scene background
        elif JERRY_X < SCREEN_MIN:  # if Jerry comes to 10px from the left side of the screen
            JERRY_X = SCREEN_SIZE * 0.95 # reset Jerry to the right of the screen
            SCENE -= 1 # change scene background
    else: # if the player is indoor
        if JERRY_X_IN >= SCREEN_MAX_IN: # when Jerry hits the right most of the screen
            JERRY_X_IN = 20 # reset Jerry to the left
            SCENE += 1 # change the scene
        elif JERRY_X_IN < SCREEN_MIN_IN: # when Jerry hits the left most of the screen
            JERRY_X_IN = SCREEN_SIZE * 0.7 # reset Jerry to the right
            SCENE -= 1 # change the scene

    # ======================== GAME SURFACE ========================
    # BACKGROUND LAYERS#
    cave_entry()
    skybox()
    backdrop_change()
    # Layer 5 (characters)
    homeless_blit() # renders the homeless man
    char_render(JERRY_X,JERRY_Y,JERRY_X_IN,JERRY_Y_IN) # render's Jerry
    # Layer 4
    foreground() # renders foreground decorations
    # Layer 3
    prompt_display()
    # Layer 2
    if JERRY_RESPONSE <= 3: # if Jerry hasn't finished dealing with an angry customer
        open_computer_interface() # allow Jerry to open the computer
        chat_dialogues(YEARS_COUNT) # allow Jerry to chat
    elif JERRY_RESPONSE == 4: # after Jerry finished dealing with an angry customer
        OFFICE_HOURS = False # office hours are over
        END_OF_DAY_MESSAGE = True
        BACKGROUND_NIGHT_DAY = 1 # set the day to night
        OPEN_COMPUTER = False
    # Layer 1
    world_Obj()
    # SLEEP FUNCTION
    if END_OF_DAY_MESSAGE == True:
        end_of_day_message()
    if SLEEP == True:
        new_day()
    ending()
    intro_screen()
    starting_screen()
    # game update function
    pygame.display.flip()

    # GAME BOUNDARIES
    ## there's a bug in this code that let's me walk off the edge of the screens into the wild blue yonder!
    if INDOOR == True: # if player is indoor
        if INTERIOR_BG_RENDER == 'OFFICE': # if player is in office
            if SCENE == 0: # if player is in the first segment of the office
                if office_exit_stop > JERRY_X_IN > 0:
                    dx = STOP
            elif SCENE == 3: # if player is at the last segment of the office
                if SCREEN_SIZE > JERRY_X_IN > water_cooler_stop:
                    dx = STOP
        elif INTERIOR_BG_RENDER == 'BAR' and SCENE == 1: # if player is in the bar
            if bar_exit_stop > JERRY_X_IN > 0:
                dx = STOP
            elif SCREEN_SIZE > JERRY_X_IN > bar_bartender_stop:
                dx = STOP
        elif INTERIOR_BG_RENDER == 'APARTMENT' and SCENE == 2: # if player is inside his apartment
            if apartment_exit_stop > JERRY_X_IN > 0:
                dx = STOP
            elif SCREEN_SIZE > JERRY_X_IN > bed_stop:
                dx = STOP
    else: # if player is outdoor
        if SCENE == 3: # if player reached end of city street
            if SCREEN_SIZE > JERRY_X > city_stop:
                dx = STOP
        elif SCENE == -4: # if player reached end of highway
            if highway_stop > JERRY_X > 0:
                dx = STOP
        elif SCENE == -5:
            if SCREEN_SIZE > JERRY_X > no_turning_back:
                dx = STOP
        elif SCENE == -7 and TREASURE_REQUIREMENT == False:
            if cave_entrance > JERRY_X > 0:
                dx = STOP
        elif SCENE == -8:  # if player reached end of highway
            if treasure_chest > JERRY_X > 0:
                dx = STOP
    # ======================== GAME SURFACE ========================
