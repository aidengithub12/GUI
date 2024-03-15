import pyglet as pg
import MouseHandler
resolution = [1920,1080]
window = pg.window.Window(width = resolution[0], height = resolution[1])

MOUSE = MouseHandler.MouseStateHandler()
window.push_handlers(MOUSE)
label = pg.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center',color=(255,255,255,255)).draw()


@window.event
def update(dt):
    print('(' + str(window._mouse_x) + ', ' + str(window._mouse_y) + ')')
def on_draw():
    window.clear()
    # label.draw()
pg.clock.schedule_interval(update, 2)
pg.app.run()