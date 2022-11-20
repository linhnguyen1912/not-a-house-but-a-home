#Name: Linh Nguyen
#Andrew id: ltn2

from cmu_112_graphics import *
import math 

#take in 2 1D lists and return the dot product
def dotProduct(L1,L2):
    result=0
    for i in range(len(L1)):
        result+=L1[i]*L2[i]
    return result

#take in a 2D list and return the ith col
def getCol(L, i):
    result =[]
    for r in range(len(L)):
        result.append(L[r][i])
    return result

#take in 2 2D list and return the matrix multiplication
def matMulti(L1,L2):
    if len(L1[0])!=len(L2):
        print("Invalid num rows and cols")
    result =[([0]*len(L2[0])) for i in range(len(L1))]
    for r in range(len(L1)):
        for c in range(len(L2[0])):
            result[r][c]=dotProduct(L1[r], getCol(L2,c))
    return result

#projection matrix
projMat = [[1,0,0],[0,1,0]]

#rotaiton matrices around the z axis
def rotationZ(angle):
    return [[math.cos(angle),-math.sin(angle),0],
    [math.sin(angle),math.cos(angle),0],
    [0,0,1]]

def rotationY(angle):
    return [[math.cos(angle),0, math.sin(angle)],
    [0,1,0],
    [-math.sin(angle),0, math.cos(angle)]]

def rotationX(angle):
    return [[1,0,0],
    [0, math.cos(angle),-math.sin(angle)],
    [0, math.sin(angle), math.cos(angle)]]

#take in a 1D list and output a 2D list of r c dim
def reshape(L, r, c):
    result = [([0]*c) for i in range(r)]
    i = 0
    for row in range(r):
        for col in range(c):
            result[row][col]=L[i]
            i+=1
    return result

class Cube:
    def __init__(self, points, angle, position, scale):
        self.points = points
        self.angle = angle
        self.position = position
        self.scale = scale
    
    @staticmethod
    def connectPoints(canvas,point1, point2, L):
        canvas.create_line(L[point1][0], L[point1][1],
        L[point2][0], L[point2][1], fill = 'black',
        )
    
    @staticmethod
    def polygon(canvas, p1, p2, p3, p4, L, color):
        canvas.create_polygon(L[p1][0],L[p1][1], L[p2][0], L[p2][1], L[p3][0],
        L[p3][1], L[p4][0], L[p4][1], fill = color)

    #later: take in rgb for shading based on rotation
    def draw(self, canvas):
        projectedPoints = []
        for point in self.points:
            #get the coordinated of the 2d projection
            reshaped = reshape(point,3,1)
            rotated2d = matMulti(rotationZ(self.angle), reshaped)
            rotated2d = matMulti(rotationX(math.pi/3.5), rotated2d)
            rotated2d = matMulti(rotationY(0), rotated2d)
            projected2d = matMulti(projMat, rotated2d)
            x= int(projected2d[0][0] * self.scale) + self.position[0]
            y= int(projected2d[1][0] * self.scale) + self.position[1]
            projectedPoints.append([x,y]) 
        # Cube.connectPoints(canvas,0,1,projectedPoints)
        # Cube.connectPoints(canvas,1,2,projectedPoints)
        # Cube.connectPoints(canvas,2,3,projectedPoints)
        # Cube.connectPoints(canvas,3,0,projectedPoints)

        # Cube.connectPoints(canvas,4,5,projectedPoints)
        # Cube.connectPoints(canvas,5,6,projectedPoints)
        # Cube.connectPoints(canvas,6,7,projectedPoints)
        # Cube.connectPoints(canvas,7,4,projectedPoints)
        Cube.polygon(canvas, 4,5,6,7, projectedPoints, "#e0a6a2" )

        # Cube.connectPoints(canvas,0,4,projectedPoints)
        # Cube.connectPoints(canvas,1,5,projectedPoints)
        # Cube.connectPoints(canvas,2,6,projectedPoints)
        # Cube.connectPoints(canvas,3,7,projectedPoints)
        Cube.polygon(canvas, 2,3,7,6, projectedPoints, "#d9716a")
        Cube.polygon(canvas, 2,1,5,6, projectedPoints, "#d17d77")
        Cube.polygon(canvas, 3,0,4,7, projectedPoints, "#ad5650")
        Cube.polygon(canvas, 3,2,6,7, projectedPoints, "#d68883")
        Cube.polygon(canvas, 3,0,1,2, projectedPoints, "#e6a7a3")
        Cube.polygon(canvas, 1,0,4,5, projectedPoints, "#e89797")
        Cube.polygon(canvas,0,1,2,3,projectedPoints, "#f7baba")
        for point in projectedPoints:
            canvas.create_text(point[0],point[1],
            text=f"{projectedPoints.index(point)}", font = "Arial 20 bold" ,
            fill='black')

#furniture class
class Furniture: 
    def __init__(self, shapes, color):
        self.shapes = shapes
        self.color = color

#make color wheel in the corner
def drawColorWheel(app, canvas):
    canvas.create_image(app.colorWheelX, app.colorWheelY, 
    image=ImageTk.PhotoImage(app.colorWheel))

#make trash can in the corner
def drawTrashCan(app,canvas):
    canvas.create_image(app.trashCanX, app.trashCanY, 
    image=ImageTk.PhotoImage(app.trashCan))
    
def appStarted(app):
    app.margin = 10
    app.color = "#f7f7b2"
    #scale for the selected furniture
    app.selectedFurniture=None
    #angle for the pov of the furniture 
    app.angle=0
    app.furniture=[]
    app.scale = 130

    app.colorWheel = app.loadImage('colorwheel.png')
    app.colorWheel = app.scaleImage(app.colorWheel, app.height/(4*app.colorWheel.height))
    app.colorWheelX = app.width/8
    app.colorWheelY = app.height-(app.width*1/8)
    app.colorPicked = app.color

    app.trashCan = app.loadImage('trashcan.png')
    app.trashCan = app.scaleImage(app.trashCan, app.height/(8*app.trashCan.height))
    app.trashCanX = app.margin*5 + app.height/16
    app.trashCanY = app.margin*5 + app.height/16

#check if a point is within colorwheel
def inColorWheel(app,x,y):
    return (x-app.colorWheelX)**2 + (y-app.colorWheelY)**2 <= (app.height/8)**2

def getPixelColor(app, x, y):
    app.temp = app.colorWheel.convert('RGB')
    x=x-(app.colorWheelX-app.temp.width/2)
    y=y-(app.colorWheelY-app.temp.height/2)
    return app.temp.getpixel((x,y))

#take in rgb value in tuples and return hex
def rgbToHex(rgb):
    result = "#"
    r=('{:X}').format(rgb[0])
    g=('{:X}').format(rgb[1])
    b=('{:X}').format(rgb[2])
    for part in (r,g,b):
        print(part)
        if len(part)==1:
            result+=f"0{part}"
        else:
            result+=str(part)
    return result

def keyPressed(app,event):
    if event.key == 'Up': 
        app.angle+=0.1
    if event.key == 'Down':
        app.angle-=0.1
    if event.key == 'Right':
        app.scale+=10
    if event.key == 'Left':
        app.scale-=10

def mousePressed(app,event):
    if inColorWheel(app,event.x,event.y):
        color = getPixelColor(app,event.x,event.y) 
        app.colorPicked = rgbToHex(color)


def mouseDragged(app,event):
    if inColorWheel(app,event.x,event.y):
        color = getPixelColor(app,event.x,event.y)
        app.colorPicked = rgbToHex(color)

def mouseReleased(app,event):
    pass

def timerFired(app):
    pass

def redrawAll(app,canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill=app.color)

    #The order of points matter here testing to draw a cube
    aPoints = [[-1,-1,1],[1,-1,1],[1,1,1],[-1,1,1],[-1,-1,-1],[1,-1,-1],\
    [1,1,-1],[-1,1,-1]]
    a= Cube(aPoints, app.angle, [app.width/2,app.height/2], app.scale)
    a.draw(canvas)
    #end of testing

    drawColorWheel(app, canvas)
    #draw rectangle of sample taken from colorwheel
    canvas.create_rectangle(app.colorWheelX-app.height/8,
    app.colorWheelY- app.height/8,
    app.colorWheelX- app.height/8+app.height/20, 
    app.colorWheelY- app.height/8-app.height/20, 
    fill =app.colorPicked, outline=app.colorPicked)

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
'''

