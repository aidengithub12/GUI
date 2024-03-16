import pyglet as pg
import MouseHandler
resolution = [1920,1080]
window = pg.window.Window(width = resolution[0], height = resolution[1])

MOUSE = MouseHandler.MouseStateHandler()
window.push_handlers(MOUSE)



@window.event
def update(dt):
    print('(' + str(window._mouse_x) + ', ' + str(window._mouse_y) + ')')

pg.clock.schedule_interval(update, 2)
pg.app.run()