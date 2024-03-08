
import pyglet
from pyglet.window import mouse
import RectangleCollision
import MouseHandler
import pyglet.gui
import random
# import glooey as golden
import matplotlib.pyplot as plot

MOUSE = MouseHandler.MouseStateHandler()
resolution = [1920,1080]
window = pyglet.window.Window(width=int(resolution[0]),height=int(resolution[1]))
image = pyglet.image.SolidColorImagePattern((255,255,255,255)).create_image(int(resolution[0]),int(resolution[1]))
window.push_handlers(MOUSE)

#All button declarations
GT = pyglet.image.load('sensor_button.jpg')
WB = pyglet.image.load('sensor_button.jpg')
AT, IR, Wd, WS = pyglet.image.load('sensor_button.jpg'), pyglet.image.load('sensor_button.jpg'), pyglet.image.load('sensor_button.jpg'), pyglet.image.load('sensor_button.jpg')
#All labels for buttons here
label = pyglet.text.Label(text="sensor data here", color=(0,0,0,0),x=300,y=1000,font_size=36,bold=True)

#returns window
def getWindow():
    return window
#sets background of window to white
def setBackground():
    data = image.get_image_data().get_data('RGB', window.width * 3)
    new_image = b''
    for i in range(0,len(data), 3):
        pixel = bytes([random.randint(0,255)]) + bytes([random.randint(0,255)]) + bytes([random.randint(0,255)])
        new_image += pixel 
    image.set_data('RGB', window.width * 3, new_image)
#collection of functions to set window up
def initializeWindow():
    # setButtons()
    pass
#sets window everytime something is added
processedonce = False
@window.event
def on_draw():
    window.clear()
    image.blit(0,0)
    GT.blit(300,300)
    WB.blit(300,300)
    AT.blit(300,300)
    IR.blit(300,300)
    Wd.blit(300,300)
    WS.blit(300,300)
    label.draw()
def update(dt):
    global processedonce
    if RectangleCollision.collision.rectangle(MOUSE["x"],MOUSE["y"],300,300,1,1,255,136):
        if MOUSE[mouse.LEFT] and processedonce == False:
            print("Works")
            processedonce = True
        if not MOUSE[mouse.LEFT] and processedonce == True:
            processedonce = False
#opens graph window
def getGraph(x=[1,2,3],y=[2,4,1]):
    plot.plot(x,y)
    plot.xlabel('Xaxis')
    plot.ylabel('Yaxis')
    plot.table('sensor data')
    plot.show()
#gets graph everytime 'c' is pressed
@window.event
def on_key_press(symbol = pyglet.window.key.C, modifiers = 0):
    getGraph()
#makes click sound everytime a window is opened
@window.event
def on_activate():
    # music = pyglet.media.load("C:\\Users\\aiden\\Downloads\\click.mp3")
    # music.play()
    pass

#runs code above
pyglet.clock.schedule_interval(update,1/120)
pyglet.app.run()