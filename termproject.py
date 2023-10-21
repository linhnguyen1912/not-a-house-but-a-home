#Name: Linh Nguyen
#Andrew id: ltn2

from cmu_112_graphics import *
from colorsys import rgb_to_hls, hls_to_rgb
from shape import *
from furniture import *
import math 

#make color wheel in the corner
def drawColorWheel(app, canvas):
    canvas.create_image(app.colorWheelX, app.colorWheelY, 
    image=ImageTk.PhotoImage(app.colorWheel))
    canvas.create_rectangle(app.colorWheelX-app.height/8,
    app.colorWheelY- app.height/8,
    app.colorWheelX- app.height/8+app.height/20, 
    app.colorWheelY- app.height/8-app.height/20, 
    fill =app.colorPicked, outline="orange3")

#check if a point is within colorwheel
def inColorWheel(app,x,y):
    return (x-app.colorWheelX)**2 + (y-app.colorWheelY)**2 <= (app.height/8)**2

def getPixelColor(app, x, y):
    app.temp = app.colorWheel.convert('RGB')
    x=x-(app.colorWheelX-app.temp.width/2)
    y=y-(app.colorWheelY-app.temp.height/2)
    return app.temp.getpixel((x,y))

#make trash can in the corner
def drawTrashCan(app,canvas):
    canvas.create_image(app.trashCanX, app.trashCanY, 
    image=ImageTk.PhotoImage(app.trashCan))
    
def appStarted(app):
    app.margin = 10
    app.color = "#f7f7b2"
    #scale for the selected furniture
    app.selectedFurniture=None
    app.selectedShape=None
    app.selectedShapeIndex=-1
    #angle for the pov of the furniture 
    app.angle=0
    app.scale = 0
    app.furniture=[]
    app.timePassed=0

    app.colorWheel = app.loadImage('colorwheel.png')
    app.colorWheel = app.scaleImage(app.colorWheel, app.height/(4*app.colorWheel.height))
    app.colorWheelX = app.width/8
    app.colorWheelY = app.height-(app.width*1/8)
    app.colorPicked = None

    app.trashCan = app.loadImage('trashcan.png')
    app.trashCan = app.scaleImage(app.trashCan, app.height/(8*app.trashCan.height))
    app.trashCanX = app.margin*5 + app.height/16
    app.trashCanY = app.margin*5 + app.height/16

    #list of model furniture on the right side of the screen
    app.scrollY = 0
    app.modelFurniture = []
    app.modelBed = Bed([app.width*7/8,app.height/5],25,math.pi*4/3)
    app.modelFurniture.append(app.modelBed)
    app.modelDrawer = Drawer([app.width*7/8,app.height*2/5],30,math.pi/3)
    app.modelFurniture.append(app.modelDrawer)
    app.modelCouch = Couch([app.width*6.75/8,app.height*3.15/5],20,math.pi*5.5/3)
    app.modelFurniture.append(app.modelCouch)
    app.modelCoffeeTable = coffeeTable([app.width*7/8,app.height*4/5], 30, math.pi/3)
    app.modelFurniture.append(app.modelCoffeeTable)
    app.modelChair=Chair([app.width*7/8,app.height], 20, math.pi/3)
    app.modelFurniture.append(app.modelChair)
    app.modelSingleSofa = singleSofa([app.width*7/8,app.height*6/5], 20, math.pi/3)
    app.modelFurniture.append(app.modelSingleSofa)

#function that check if event.key is near the model furniture and if legal, init that furniture
def checkForLegalInit(app,x,y):
    for furniture in app.modelFurniture:
        if distance(x,y, furniture.getPosition()[0], furniture.getPosition()[1])<=10:
            if type(furniture)==str:
                #init the furniture based on its type
                #update app.selectedFurniture to this object
                #append the object to the existing app.furniture list
                pass

def keyPressed(app,event):
    if app.selectedFurniture!=None:
        if event.key == 'Up': 
            app.angle+=0.1
            app.selectedFurniture.setAngle(app.angle)
        if event.key == 'Down':
            app.angle-=0.1
            app.selectedFurniture.setAngle(app.angle)
        if event.key == 'Right':
            app.scale+=5
            app.selectedFurniture.setScale(app.scale)
        if event.key == 'Left':
            app.scale-=5
            app.selectedFurniture.setScale(app.scale)
    if event.key =='p':
        print(app.angle)
        print()
    if event.key =='w':
        app.scrollY =-10
        for furniture in app.modelFurniture:
            furniture.setPosition([furniture.getPosition()[0], furniture.getPosition()[1]+app.scrollY])
    if event.key =='s' and app.modelFurniture[0].getPosition()[1]<app.height/5:
        app.scrollY =+10
        for furniture in app.modelFurniture:
            furniture.setPosition([furniture.getPosition()[0], furniture.getPosition()[1]+app.scrollY])
    if event.key == 'Space':
        app.scrollY=0
    if event.key =='d':
        if app.selectedShapeIndex<len(app.selectedFurniture.getShapes())-1:
            app.selectedShapeIndex+=1
            app.selectedShape = app.selectedFurniture.getShapes()[app.selectedShapeIndex]
        if app.selectedShape!=None:
            app.colorPicked = app.selectedShape.getColor()
    elif event.key =='a':
        if app.selectedShapeIndex>0:
            app.selectedShapeIndex-=1
            app.selectedShape = app.selectedFurniture.getShapes()[app.selectedShapeIndex]
        if app.selectedShape!=None:
            app.colorPicked = app.selectedShape.getColor()
    #Press enter to finish updating shape color
    if event.key =='Return':
        app.selectedShape=None
        app.selectedShapeIndex=-1


def initFurniture(type, position, scale, angle):
    if type=="Bed":
        result = Bed(position,scale, angle)
    elif type =="Drawer":
        result = Drawer(position, scale, angle)
    elif type =="Couch":
        result = Couch(position, scale, angle)
    elif type =="coffeeTable":
        result = coffeeTable(position,  scale, angle)
    elif type =="Chair":
        result = Chair(position, scale, angle)
    elif type =="singleSofa":
        result = singleSofa(position,  scale, angle)
    return result

def mousePressed(app,event):
    if inColorWheel(app,event.x,event.y):
        color = getPixelColor(app,event.x,event.y) 
        app.colorPicked = rgbToHex(color)
    for furniture in app.furniture:
        if distance(event.x,event.y, furniture.getPosition()[0], furniture.getPosition()[1])<=10:
            app.selectedFurniture = furniture
            app.scale = furniture.getScale()
            app.angle = furniture.getAngle()
    for furniture in app.modelFurniture:
        if distance(event.x,event.y, furniture.getPosition()[0], furniture.getPosition()[1])<=10:
            newFurniture = initFurniture(furniture.getType(), [app.width/2, app.height/2], furniture.getScale(), furniture.getAngle())
            app.furniture.append(newFurniture)
            app.selectedFurniture = newFurniture

def mouseDragged(app,event):
    if inColorWheel(app,event.x,event.y):
        color = getPixelColor(app,event.x,event.y)
        app.colorPicked = rgbToHex(color)
    elif app.selectedFurniture!=None:
        app.selectedFurniture.setPosition((event.x,event.y))

def timerFired(app):
    app.timePassed+=app.timerDelay
    if app.selectedFurniture!=None:
        tempPos = app.selectedFurniture.getPosition()
        if distance(tempPos[0],tempPos[1], app.trashCanX, app.trashCanY)<=10:
            app.furniture.remove(app.selectedFurniture)
            app.selectedFurniture = None
            app.selectedShape = None
            app.selectedShapeIndex=-1
    if app.selectedShapeIndex!=-1 and app.selectedFurniture!=None:
        app.selectedShape = app.selectedFurniture.getShapes()[app.selectedShapeIndex]
        

def drawRoom(app,canvas, color):
    points = [[-1,-1,1],[1,-1,1],[1,1,1],[-1,1,1],[-1,-1,-1],[1,-1,-1],\
    [1,1,-1],[-1,1,-1]]
    points2D=[]
    for point in points:
            #get the coordinated of the 2d projection
            reshaped = reshape(point,3,1)
            rotated2d = matMulti(rotationZ(math.pi/4), reshaped)
            rotated2d = matMulti(rotationX(math.pi/3), rotated2d)
            rotated2d = matMulti(rotationY(0), rotated2d)
            projected2d = matMulti(projMat, rotated2d)
            x= int(projected2d[0][0] *  180) + app.width/2
            y= int(projected2d[1][0]  * 180) + app.height/2
            points2D.append([x,y]) 
    rect1 = [0,3,7,4]
    rect2 = [0,1,5,4]
    rect3 = [7,4,5,6]
    colorRgb = hexToRgb(color)
    lightColor = lightenColor(colorRgb,0.1)
    lightColor = rgbToHex(lightColor)
    darkColor = darkenColor(colorRgb,0.1)
    darkColor = rgbToHex(darkColor)
    Cuboid.polygon(canvas, rect1[0], rect1[1], rect1[2], rect1[3], points2D, color)
    Cuboid.polygon(canvas, rect2[0], rect2[1], rect2[2], rect2[3], points2D, lightColor)
    Cuboid.polygon(canvas, rect3[0], rect3[1], rect3[2], rect3[3], points2D, darkColor)

def redrawAll(app,canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill=app.color)
    drawRoom(app,canvas, "#c8bfe3")
    drawColorWheel(app, canvas)
    drawTrashCan(app,canvas)

    for furniture in app.modelFurniture:
        furniture.draw(canvas)
        canvas.create_oval(furniture.getPosition()[0]-2, furniture.getPosition()[1]-2,\
        furniture.getPosition()[0]+2, furniture.getPosition()[1]+2, fill = app.color, outline = app.color)
    
    if app.furniture!=[]:
        for furniture in app.furniture:
            furniture.draw(canvas)
            canvas.create_oval(furniture.getPosition()[0]-2, furniture.getPosition()[1]-2,\
            furniture.getPosition()[0]+2, furniture.getPosition()[1]+2, fill = app.color, outline = app.color)
    
    if app.selectedShape!=None:
        app.selectedShape.setColor(app.colorPicked)

    if app.selectedShapeIndex!=-1 and app.selectedShape!=None:
        app.selectedShape.outline(canvas)

    drawColorWheel(app, canvas)
    drawTrashCan(app,canvas)

runApp(width=900, height=600)

'''
Source: 
https://favpng.com/png_view/actions-color-picker-hand-finger-orange-png/ynkGGG0E
https://favpng.com/png_view/%D0%BA%D1%80%D1%83%D0%B3%D0%B8-color-wheel-rgb-color-model-color-gradient-complementary-colors-png/xw5btGdN
pictures

https://www.educative.io/answers/how-to-convert-hex-to-rgb-and-rgb-to-hex-in-python
https://www.pluralsight.com/blog/tutorials/understanding-hexadecimal-colors-simple#:~:text=Hex%20color%20codes%20start%20with,0%20to%20255%20in%20RGB). 
converting rgb to hex

https://www.youtube.com/watch?v=qw0oY6Ld-L0
isometric graphics tutorial

https://news.ycombinator.com/item?id=3583564
lightencolor
'''
