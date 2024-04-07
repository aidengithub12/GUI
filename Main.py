import pyglet as pg
from pyglet.window import mouse
import RectangleCollision
import MouseHandler
import pyglet.gui as pgg
import random
# import glooey as golden
import MasterFIle
import Calculate


#TODO: fix screen bug
MOUSE = MouseHandler.MouseStateHandler()
resolution = [1920,1080]
window = pg.window.Window(width=int(resolution[0]),height=int(resolution[1]),resizable = True,)
image = pg.image.SolidColorImagePattern((255,255,255,255)).create_image(int(resolution[0]),int(resolution[1]))
window.push_handlers(MOUSE)


#All reading variables
GT = 0 #temp
WB = 0 #temp
AT = 0 #temp
IR = 0 #temp
BAR = 0 #float
RH = 0 #float
WD = 0 #int
WS = 0 #int
LAT = 0 #float
LONG = 0 #float
#map = 0
#gps = 0
compass = 0 #float
#All button declarations
GT_Image = pg.image.load('sensor_button.jpg')
WB_Image = pg.image.load('sensor_button.jpg')
AT_Image, IR_Image, Wd_Image, WS_Image = pg.image.load('sensor_button.jpg'), pg.image.load('sensor_button.jpg'), pg.image.load('sensor_button.jpg'), pg.image.load('sensor_button.jpg')
#All labels for buttons here
"""
(90, 34, 139);, 1 
"""
"""
GT.blit(123,733)
    WB.blit(351,733)
    AT.blit(841,733)
    IR.blit(1000,733)
    Wd.blit(550,733)
    WS.blit(1200,733)
    """

fps_display = pg.window.FPSDisplay(window=window)
fps_display.label._set_position((window.height/2, window.width/2,0))
labelGT = pg.text.Label(text="GT", color=(0,0,0,255),x=123,y=1035,font_size=36,bold=True,font_name='Times New Roman')
labelWB = pg.text.Label(text="WB", color=(0,0,0,255),x=351,y=1035,font_size=36,bold=True)
labelAT = pg.text.Label(text="AT", color=(0,0,0,255),x=791,y=1035,font_size=36,bold=True)
labelIR = pg.text.Label(text="IR", color=(0,0,0,255),x=1000,y=1035,font_size=36,bold=True)
labelWD = pg.text.Label(text="Wd", color=(0,0,0,255),x=550,y=1035,font_size=36,bold=True)
labelWS = pg.text.Label(text="WS", color=(0,0,0,255),x=1200,y=1035,font_size=36,bold=True)
blank = pg.text.Label('')
labelReadingGT = pg.text.Label(text=str(GT) + ' C', color = (0,0,0,255), x = 123, y = 893, font_size=36, bold = True)
labelReadingWB = pg.text.Label(text=str(WB) + ' C', color = (0,0,0,255), x = 351, y = 893, font_size=36, bold = True)
labelReadingAT = pg.text.Label(text=str(AT) + ' C', color = (0,0,0,255), x = 791, y = 893, font_size=36, bold = True)
labelReadingIR = pg.text.Label(text=str(IR) + ' C', color = (0,0,0,255), x = 1000, y = 893, font_size=36, bold = True)
labelReadingWD = pg.text.Label(text=str(WD) + ' degrees', color = (0,0,0,255), x = 550, y = 893, font_size=36, bold = True)
labelReadingWS = pg.text.Label(text=str(WS) + ' m/s', color = (0,0,0,255), x = 1200, y = 893, font_size=36, bold = True)
labelReadingLAT = pg.text.Label(text=str(LAT) + ' degrees', color = (0,0,0,255), x = 99, y = 465, font_size=36, bold = True)
labelReadingLONG = pg.text.Label(text=str(LONG) + ' degrees', color = (0,0,0,255), x = 99, y = 323, font_size=36, bold = True)
labelReadingBAR = pg.text.Label(text = str(BAR) + ' units', color = (0,0,0,255), x = 1100, y = 465, font_size=36, bold = True)
labelReadingRH = pg.text.Label(text = str(RH) + ' units', color = (0,0,0,255), x = 1100, y = 323, font_size=36, bold = True)
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
    labelGT.draw()
    labelAT.draw()
    labelIR.draw()
    labelWB.draw()
    labelWD.draw()
    labelWS.draw()
    GT_Image.blit(60,833)
    WB_Image.blit(288,833)
    AT_Image.blit(728,833)
    IR_Image.blit(937,833)
    Wd_Image.blit(487,833)
    WS_Image.blit(1137,833)
    labelReadingGT.draw()
    labelReadingAT.draw()
    labelReadingIR.draw()
    labelReadingWB.draw()
    labelReadingWS.draw()
    labelReadingWD.draw()
    labelReadingLAT.draw()
    labelReadingLONG.draw()
    labelReadingBAR.draw()
    labelReadingRH.draw()
    fps_display.draw()
def update(dt):
    global processedonce
    data = Calculate.getSensorData()
    if RectangleCollision.collision.rectangle(MOUSE["x"],MOUSE["y"],60,833,1,1,255,136):
        if MOUSE[mouse.LEFT] and processedonce == False:
            MasterFIle.getGraph(xvalues=data[1],yvalues=data[2],var="GT")
            processedonce = True
        if not MOUSE[mouse.LEFT] and processedonce == True:
            processedonce = False
    if RectangleCollision.collision.rectangle(MOUSE["x"],MOUSE["y"],288,833,1,1,255,136):
        if MOUSE[mouse.LEFT] and processedonce == False:
            MasterFIle.getGraph(xvalues=data[1],yvalues=data[2],var="WB")
            processedonce = True
        if not MOUSE[mouse.LEFT] and processedonce == True:
            processedonce = False
    if RectangleCollision.collision.rectangle(MOUSE["x"],MOUSE["y"],728,833,1,1,255,136):
        if MOUSE[mouse.LEFT] and processedonce == False:
            MasterFIle.getGraph(xvalues=data[1],yvalues=data[2],var="AT")
            processedonce = True
        if not MOUSE[mouse.LEFT] and processedonce == True:
            processedonce = False
    if RectangleCollision.collision.rectangle(MOUSE["x"],MOUSE["y"],937,833,1,1,255,136):
        if MOUSE[mouse.LEFT] and processedonce == False:
            MasterFIle.getGraph(xvalues=data[1],yvalues=data[2],var="IR")
            processedonce = True
        if not MOUSE[mouse.LEFT] and processedonce == True:
            processedonce = False
    if RectangleCollision.collision.rectangle(MOUSE["x"],MOUSE["y"],487,833,1,1,255,136):
        if MOUSE[mouse.LEFT] and processedonce == False:
            MasterFIle.getGraph(xvalues=data[1],yvalues=data[2],var="WD")
            processedonce = True
        if not MOUSE[mouse.LEFT] and processedonce == True:
            processedonce = False
    if RectangleCollision.collision.rectangle(MOUSE["x"],MOUSE["y"],1137,833,1,1,255,136):
        if MOUSE[mouse.LEFT] and processedonce == False:
            MasterFIle.getGraph(xvalues=data[1],yvalues=data[2],var="WS")
            processedonce = True
        if not MOUSE[mouse.LEFT] and processedonce == True:
            processedonce = False
#makes click sound everytime a window is opened
@window.event
def on_activate():
    # music = pg.media.load("C:\\Users\\aiden\\Downloads\\click.mp3")
    # music.play()
    blank.draw()
    pass
@window.event
def on_hide():
    on_draw()
@window.event
def on_show():
    on_draw()
def updateValues(dt):
    global data
    data = Calculate.getSensorData()
    """
    data.GT,data.WB,data.AT,data.IRT,data.P,data.RH,data.WS,data.WD,data.LAT,
    data.LON,data.COMP
    """
    labelReadingGT.text = str(data[2][len(data[2]) - 1]) + 'C'
    labelReadingWB.text = str(data[3][0]) #+ 'C'
    labelReadingAT.text = str(data[4][0]) #+ 'C'
    labelReadingIR.text = str(data[5][0]) #+ 'units'
    labelReadingRH.text = str(data[7][0]) #+ 'units'
    labelReadingWS.text = str(data[8][0]) #+ 'm/s'
    labelReadingWD.text = str(data[9][0]) #+ 'units'
    labelReadingLAT.text = str(data[10][0]) #+ 'degrees'
    labelReadingLONG.text = str(data[11][0]) #+ 'degrees'
#runs code above
pg.clock.schedule_interval(update,1/10)
pg.clock.schedule_interval(updateValues,1/10)
pg.app.run()