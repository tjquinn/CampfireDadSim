import pyglet
import copy
import pprint
import keyboard
from termcolor import colored
from random import choice
from sys import stdout
from assets import surfaces


class CampGrounds:
    def __init__(self, x_size, y_size, features):
        self.x_size = x_size
        self.y_size = y_size
        self.features = features


class Characters:
    def __init__(self, loc, profession):
        self.loc = loc
        self.profession = profession

    def draw_character(self, x, y, player):
        self.x = x
        self.y = y
        self.player = player
        player.set_position(x, y)


player = pyglet.sprite.Sprite(pyglet.image.load('assets/sprites/characters/dad.gif'), 0, 0)
Dad = Characters((0, 0), "Dad")


def gimme_string(chunk):
    return str(chr(chunk))


def generate_map(width, height, size):
    campfire_map = []

    for x in range(10):

        row = x % 10 * 64

        for y in range(10):
            col = y % 10 * 64
            surface = copy.deepcopy(choice(surfaces))
            surface['pos'] = {'x': row, 'y': col}
            campfire_map.append(surface)

    return campfire_map


window = pyglet.window.Window(640, 640)
batch = pyglet.graphics.Batch()
constant_map = generate_map(640, 640, 64)

# Going to write my own 8bit song on FL Studio taking this down because it was copyrighted
# music = pyglet.resource.media('assets/music/temp-music.mp3')
# music.play()

label = pyglet.text.Label('Campfire Dad Sim',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width // 2, y=window.height // 2,
                          anchor_x='center', anchor_y='center')


def character_controller(key):
    # Looping boundaries
    min = 0
    max = 640
    dad_x = Dad.loc[0]
    dad_y = Dad.loc[1]

    # Move dad up
    if (key.name in ['w', 'up']):
        if (dad_y + 64 <= max):
            Dad.loc = (dad_x, (dad_y + 64))
            Dad.draw_character(dad_x, (dad_y + 64), player)
        else:
            Dad.loc = (dad_x, min)
            Dad.draw_character(dad_x, min, player)

    # Move dad right
    if (key.name in ['d', 'right']):
        if (dad_x + 64 <= max):
            Dad.loc = ((dad_x + 64), dad_y)
            Dad.draw_character((dad_x + 64), dad_y, player)
        else:
            Dad.loc = (min, dad_y)
            Dad.draw_character(min, dad_y, player)

    # Move dad down
    if (key.name in ['s', 'down']):
        if (dad_y - 64 > min):
            Dad.loc = (dad_x, (dad_y - 64))
            Dad.draw_character(dad_x, (dad_y - 64), player)
        else:
            Dad.loc = (dad_x, max)
            Dad.draw_character(dad_x, max, player)

    # Move dad left
    if (key.name in ['a', 'left']):
        if (dad_x - 64 > min):
            Dad.loc = ((dad_x - 64), dad_y)
            Dad.draw_character((dad_x - 64), dad_y, player)
        else:
            Dad.loc = (max, dad_y)
            Dad.draw_character(max, dad_y, player)

    # Dad Attack
    # if (key.name in ['space']):
    #     print('ATTACK!')


def make_grid(batch, height, width, size):
    for i in range(size):
        x = (i + 1) * size
        y = (i + 1) * size
        batch.add(2, pyglet.gl.GL_LINES, None,
                  ('v2i', (x, 0, x, width)),
                  ('c3B', (0, 0, 255, 0, 255, 0)))

        batch.add(2, pyglet.gl.GL_LINES, None,
                  ('v2i', (0, y, height, y)),
                  ('c3B', (0, 0, 255, 0, 255, 0)))

    return batch


ground_sprites = []
for i in range(len(constant_map)):
    pos_x = constant_map[i]['pos']['x']
    pos_y = constant_map[i]['pos']['y']
    ground_image = pyglet.image.load(constant_map[i]['image'])
    ground_sprites.append(pyglet.sprite.Sprite(ground_image, pos_x, pos_y, batch=batch))

# make_grid(batch, 640, 640, 64)

keyboard.on_press(character_controller)


@window.event
def on_draw():
    window.clear()
    batch.draw()
    player.draw()
    # label.draw()

pyglet.app.run()