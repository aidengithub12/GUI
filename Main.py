
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
labelGT = pyglet.text.Label(text="GT", color=(0,0,0,0),x=128,y=1035,font_size=36,bold=True,font_name='Times New Roman',anchor_x='center',anchor_y='center').draw()
labelWB = pyglet.text.Label(text="WB", color=(0,0,0,0),x=351,y=1035,font_size=36,bold=True).draw()
labelAT = pyglet.text.Label(text="AT", color=(0,0,0,0),x=841,y=1035,font_size=36,bold=True).draw()
labelIR = pyglet.text.Label(text="IR", color=(0,0,0,0),x=1311,y=1035,font_size=36,bold=True).draw()
labelWD = pyglet.text.Label(text="Wd", color=(0,0,0,0),x=550,y=1035,font_size=36,bold=True).draw()
labelWS = pyglet.text.Label(text="WS", color=(0,0,0,0),x=1500,y=1035,font_size=36,bold=True).draw()


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

#sets window everytime something is added
processedonce = False
@window.event
def on_draw():
    window.clear()
    image.blit(0,0)
    GT.blit(123,733)
    WB.blit(351,733)
    AT.blit(841,733)
    IR.blit(1000,733)
    Wd.blit(550,733)
    WS.blit(1200,733)
    
def update(dt):
    global processedonce
    #button logic for GT
    if RectangleCollision.collision.rectangle(MOUSE["x"],MOUSE["y"],123,733,1,1,255,136):
        if MOUSE[mouse.LEFT] and processedonce == False:
            print("Works")
            processedonce = True
        if not MOUSE[mouse.LEFT] and processedonce == True:
            processedonce = False
    if RectangleCollision.collision.rectangle(MOUSE["x"],MOUSE["y"],351,733,1,1,255,136):
        if MOUSE[mouse.LEFT] and processedonce == False:
            print("Works")
            processedonce = True
        if not MOUSE[mouse.LEFT] and processedonce == True:
            processedonce = False
    if RectangleCollision.collision.rectangle(MOUSE["x"],MOUSE["y"],841,733,1,1,255,136):
        if MOUSE[mouse.LEFT] and processedonce == False:
            print("Works")
            processedonce = True
        if not MOUSE[mouse.LEFT] and processedonce == True:
            processedonce = False
    if RectangleCollision.collision.rectangle(MOUSE["x"],MOUSE["y"],1000,733,1,1,255,136):
        if MOUSE[mouse.LEFT] and processedonce == False:
            print("Works")
            processedonce = True
        if not MOUSE[mouse.LEFT] and processedonce == True:
            processedonce = False
    if RectangleCollision.collision.rectangle(MOUSE["x"],MOUSE["y"],550,733,1,1,255,136):
        if MOUSE[mouse.LEFT] and processedonce == False:
            print("Works")
            processedonce = True
        if not MOUSE[mouse.LEFT] and processedonce == True:
            processedonce = False
    if RectangleCollision.collision.rectangle(MOUSE["x"],MOUSE["y"],1200,733,1,1,255,136):
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