import pyglet
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


Dad = Characters((0, 0), "Dad")


def gimme_string(chunk):
    return str(chr(chunk))


def generate_map(x, y):
    campfire_map = []

    for i in range(x*y):
        campfire_map.append(choice(surfaces))

    return campfire_map


# display_map function prints out the map to console
def display_map(mappy):
    graphy = ""
    for i in range(len(mappy)):
        if mappy[i] in surfaces:
            graphy += gimme_string(mappy[i][0])

    return graphy


constant_map = generate_map(100,50)
# print(constant_map);

window = pyglet.window.Window()

music = pyglet.resource.media('assets/music/temp-music.mp3')
music.play()


batch = pyglet.graphics.Batch()

label = pyglet.text.Label('Campfire Dad Sim',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

grass_image = pyglet.image.load('assets/sprites/environment/grass.gif')
grass = pyglet.sprite.Sprite(grass_image, x=64, y=64)



grass_sprites = []
for i in range(4):
    x, y = i+1 * 64, 64
    grass_sprites.append(pyglet.sprite.Sprite(grass_image, x, y, batch=batch))

@window.event
def on_draw():
    window.clear()
    label.draw()
    batch.draw()



pyglet.app.run()
