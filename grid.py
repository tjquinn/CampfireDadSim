import pyglet

window = pyglet.window.Window(400, 400)
batch = pyglet.graphics.Batch()

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

make_grid(batch, 400, 400, 40)

@window.event
def on_draw():
    window.clear()
    batch.draw()
   
pyglet.app.run()
