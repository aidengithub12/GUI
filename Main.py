
import pyglet as pg
from pyglet.window import mouse
import RectangleCollision
import MouseHandler
import pyglet.gui as pgg
import random
# import glooey as golden
import matplotlib.pyplot as plot

MOUSE = MouseHandler.MouseStateHandler()
resolution = [1920,1080]
window = pg.window.Window(width=int(resolution[0]),height=int(resolution[1]))
image = pg.image.SolidColorImagePattern((255,255,255,255)).create_image(int(resolution[0]),int(resolution[1]))
window.push_handlers(MOUSE)

#All button declarations
GT = pg.image.load('sensor_button.jpg')
WB = pg.image.load('sensor_button.jpg')
AT, IR, Wd, WS = pg.image.load('sensor_button.jpg'), pg.image.load('sensor_button.jpg'), pg.image.load('sensor_button.jpg'), pg.image.load('sensor_button.jpg')
#All labels for buttons here
"""
(90, 34, 139);, 1 
"""
label = pg.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center',color=(90,34,139,1))
labelGT = pg.text.Label(text="GT", color=(0,0,0,0),x=128,y=1035,font_size=36,bold=True,font_name='Times New Roman',anchor_x='center',anchor_y='center').draw()
labelWB = pg.text.Label(text="WB", color=(0,0,0,0),x=351,y=1035,font_size=36,bold=True)
labelAT = pg.text.Label(text="AT", color=(0,0,0,0),x=841,y=1035,font_size=36,bold=True)
labelIR = pg.text.Label(text="IR", color=(0,0,0,0),x=1311,y=1035,font_size=36,bold=True)
labelWD = pg.text.Label(text="Wd", color=(0,0,0,0),x=550,y=1035,font_size=36,bold=True)
labelWS = pg.text.Label(text="WS", color=(0,0,0,0),x=1500,y=1035,font_size=36,bold=True)


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
    labelAT.draw()
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
def on_key_press(symbol, modifiers = 0):
    if symbol == pg.window.key.G:
        getGraph()
    
#makes click sound everytime a window is opened
@window.event
def on_activate():
    # music = pg.media.load("C:\\Users\\aiden\\Downloads\\click.mp3")
    # music.play()
    pass

#runs code above
pg.clock.schedule_interval(update,1/120)
pg.app.run()