import sys
import termios
import tty
import os
import time
from random import randint
import shutil
import numpy as np
from colorama import Fore, Back, Style

 # import local files
import create_scenery
import config

char = '' 

while True:
    char=config.get_key(config.get_input())
    
    create_scenery.create_floor(config.m)
    create_scenery.create_Wall()
    create_scenery.create_Enemy()

    if (char == config.QUIT):
        # shut down all [q]
        print(Style.RESET_ALL)
        os.system('cls' if os.name == 'nt' else 'clear')
        exit(0)

    if (char == config.START):
        # create a Person [a]
        create_scenery.create_Mario()

    elif (char == config.BREAK):
        # break the loop [s]
        os.system('cls' if os.name == 'nt' else 'clear')
        break
        # time.sleep(button_delay)

    elif (char == config.RIGHT):
        # Person moving right[d]
        a = config.m.x+1
        b = config.m.y
        config.m.move(a, b)
        for i in config.w_list:
            ret = i.move(i.x-1)
            if (ret == 1):
                config.w_list.remove(i)

        # time.sleep(button_delay)

    elif (char == config.JUMP):
        # Person  [w]
        config.m.jump()
        # time.sleep(button_delay)

    elif (char == "1"):
        print("Number 1 pressed")
        # pppptime.sleep(button_delay)