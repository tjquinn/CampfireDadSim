import sys # imported for output method at bottom
from termcolor import colored
from random import choice

#TO DO: import better dictionary or object
surfaces = [[9608, 'green'], [9608, 'white'], [9608, 'blue']]

def decode_map_chunk(chunk):

    return str(chr(chunk))


#generate_map will return a list of x*y length
def generate_map(x, y):

    campfire_map = []

    for i in range(x * y):

        if i % x != 0:
            campfire_map.append(choice(surfaces))
        else:
            campfire_map.append('<br>')

    return campfire_map

#display_map
def display_map(mappy):
    graphy = ""
    for i in range(len(mappy)):
        if mappy[i] not in surfaces:
            graphy += "\n\r"
        else:
            # graphy += mappy[i][:1]
            graphy += colored(decode_map_chunk(mappy[i][0]), mappy[i][1])

    return graphy

constant_map = display_map(generate_map(100, 100))
modified_map = constant_map


#TO DO: Get this working
def start_game(modified_map):
    sys.stdout.write(modified_map)
    # sys.stdout.flush()
    

def update_map(modified_map):
    sys.stdout.write(modified_map)
    # sys.stdout.flush()

def end_game(modified_map):
    sys.stdout.write(modified_map)
    # sys.stdout.flush()

start_game(modified_map)