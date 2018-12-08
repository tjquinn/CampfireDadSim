from termcolor import colored
from random import choice
from sys import stdout


class CampGrounds:
    def __init__(self, x_size, y_size, features):
        self.x_size = x_size
        self.y_size = y_size
        self.features = features


class Characters:
    def __init__(self, loc, profession):
        self.loc = loc
        self.profession = profession


Dad = Characters((0,0), "Dad")


# TO DO: import better dictionary or object
surfaces = [[9608, 'green'], [9608, 'white'], [9608, 'blue']]


def gimme_string(chunk):
    return str(chr(chunk))


def generate_map(x, y):
    campfire_map = []

    for i in range(x * y):

        if i % x != 0:
            campfire_map.append(choice(surfaces))
        else:
            campfire_map.append('<br>')

    return campfire_map


# display_map function prints out the map to console
def display_map(mappy):
    graphy = ""
    for i in range(len(mappy)):
        if mappy[i] not in surfaces:
            graphy += "\n\r"
        else:
            # graphy += mappy[i][:1]
            graphy += colored(gimme_string(mappy[i][0]), mappy[i][1])

    return graphy


constant_map = display_map(generate_map(100, 100))
modified_map = constant_map


#TO DO: Get this working
def start_game(modified_map):
    stdout.write(modified_map)
    # sys.stdout.flush()
    

def update_map(modified_map):
    stdout.write(modified_map)
    # sys.stdout.flush()

def end_game(modified_map):
    stdout.write(modified_map)
    # sys.stdout.flush()

start_game(modified_map)