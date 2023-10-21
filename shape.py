import math 
from colorsys import rgb_to_hls, hls_to_rgb

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

def distance(x1,y1,x2,y2):
    temp = (x1-x2)**2 + (y1-y2)**2
    return temp**(1/2)

def adjust_color_lightness(rgb, factor):
    r=rgb[0]
    g=rgb[1]
    b=rgb[2]
    h, l, s = rgb_to_hls(r / 255.0, g / 255.0, b / 255.0)
    l = max(min(l * factor, 1.0), 0.0)
    r, g, b = hls_to_rgb(h, l, s)
    return int(r * 255), int(g * 255), int(b * 255)

def lightenColor(rgb, factor=0.1):
    return adjust_color_lightness(rgb, 1 + factor)

def darkenColor(rgb, factor=0.1):
    return adjust_color_lightness(rgb, 1 - factor)

class Shape:
    def __init__(self, angle, points, scale, color):
        self.angle = angle
        self.position = 0
        self.scale = scale
        self.color = color
        self.points = points
    
    def setColor(self,color):
        self.color = color
    
    def getColor(self):
        return self.color
    
    def setScale(self, scale):
        self.scale=scale
    
    def getAngle(self):
        return self.angle
    

class Cuboid(Shape):
    #dimension is a tuple of height, length, and depth
    def __init__(self, angle, points, scale, color):
        super().__init__(angle, points, scale, color)
        self.points2D=[]
        for point in self.points:
            #get the coordinated of the 2d projection
            reshaped = reshape(point,3,1)
            rotated2d = matMulti(rotationZ(self.angle), reshaped)
            rotated2d = matMulti(rotationX(math.pi/3), rotated2d)
            rotated2d = matMulti(rotationY(0), rotated2d)
            projected2d = matMulti(projMat, rotated2d)
            x= int(projected2d[0][0] * self.scale)
            y= int(projected2d[1][0]  * self.scale)
            self.points2D.append([x,y]) 

    #x
    def getLength(self):
        return distance(self.points2D[7][0], self.points2D[7][1], self.points2D[6][0], self.points2D[6][1])
    
    #y
    def getHeight(self):
        return distance(self.points2D[2][0], self.points2D[2][1], self.points2D[6][0], self.points2D[6][1])
    
    def getPoints2D(self):
        return self.points2D
    
    #adjust points2D coordinates according to furniture position
    def setPosition(self, position):
        for point in self.points2D:
            point[0]+=position[0]
            point[1]+=position[1]
 
    @staticmethod
    def connectPoints(canvas,point1, point2, L):
        canvas.create_line(L[point1][0], L[point1][1],
        L[point2][0], L[point2][1], fill = 'black',
        )
    
    @staticmethod
    def polygon(canvas, p1, p2, p3, p4, L, color):
        canvas.create_polygon(L[p1][0],L[p1][1], L[p2][0], L[p2][1], L[p3][0],
        L[p3][1], L[p4][0], L[p4][1], fill = color)
    
    @staticmethod
    #light is coming from the top right corner
    #take in an angle and return the color of the sides of the cube
    def shade(canvas, L, angle, color):
        while angle<0:
            angle+=math.pi*2
        while angle>=math.pi*2 and angle>0:
            angle-=math.pi*2
        colorRgb = hexToRgb(color)
        lightColor = lightenColor(colorRgb,0.1)
        lightColor = rgbToHex(lightColor)
        Cuboid.polygon(canvas, 0,1,2,3, L, lightColor)
        if angle==0:
            #Cuboid.polygon(canvas, 3,2,6,7, L, color)
            base = 0
            rect1 = (0,3,7,4)
            rect2 = (3,2,6,7)
        elif angle>0 and angle<=math.pi/2:
            base = 0
            rect1 = (3,2,6,7)
            rect2 = (2,1,5,6)
        elif angle>math.pi/2 and angle<=math.pi:
            base = math.pi/2
            rect1 = (2,1,5,6)
            rect2 = (1,0,4,5)
        elif angle>math.pi and angle<=math.pi*3/2:
            base = math.pi
            rect1 = (1,0,4,5)
            rect2 = (0,3,7,4)
        elif angle>math.pi*3/2 and angle<math.pi*2:
            base = math.pi*3/2
            rect1 = (0,3,7,4)
            rect2 = (3,2,6,7)
        percent = (angle-base)/(math.pi/2)/7
        darkColor = darkenColor(colorRgb,percent)
        darkColor = rgbToHex(darkColor)
        Cuboid.polygon(canvas, rect1[0], rect1[1], rect1[2], rect1[3], L, darkColor)
        Cuboid.polygon(canvas, rect2[0], rect2[1], rect2[2], rect2[3], L, color)

    def rotation3DCube(self, x,y,z,angle):
        result=[]
        for point in self.points:
            result.append(rotation3D(x,y,z,point,angle))
        self.points=result

    #later: take in rgb for shading based on rotation
    def draw(self, canvas):
        Cuboid.shade(canvas, self.points2D, self.angle, self.color)
        # for point in self.points2D:
        #     canvas.create_text(point[0],point[1],
        #     text=f"{self.points2D.index(point)}", font = "Arial 20 bold" ,
        #     fill='black')
    
    def outline(self, canvas):
        angle = self.getAngle()
        while angle<0:
            angle+=math.pi*2
        while angle>=math.pi*2 and angle>0:
            angle-=math.pi*2
        if angle>=0 and angle<=math.pi/2:
            tempPoints=[3,0,1,5,6,7]
        elif angle>=math.pi/2 and angle<=math.pi:
            tempPoints=[3,0,4,5,6,2]
        elif angle>=math.pi and angle<=math.pi*3/2:
            tempPoints=[3,7,4,5,1,2]
        else:
            tempPoints=[0,1,2,6,7,4]
        for point in range(len(tempPoints)-1):
            Cuboid.connectPoints(canvas,tempPoints[point], tempPoints[point+1], self.points2D)
        Cuboid.connectPoints(canvas,tempPoints[0],tempPoints[-1],self.points2D)

#take in hex and return rgb value in tuple
def hexToRgb(hex):
    rgb=[]
    hex=hex.strip("#")
    for i in (0,2,4):
        decimal = int(hex[i:i+2], 16)
        rgb.append(decimal)
    return tuple(rgb)

#take in rgb value in tuples and return hex
def rgbToHex(rgb):
    result = "#"
    r=('{:X}').format(rgb[0])
    g=('{:X}').format(rgb[1])
    b=('{:X}').format(rgb[2])
    for part in (r,g,b):
        if len(part)==1:
            result+=f"0{part}"
        else:
            result+=str(part)
    return result

#take in component of a vector and normalize it
#From Payton Downey and  https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/rotate3d() 
def norm(x,y,z):
    magnitude = (x**2+y**2+z**2)**(1/2)
    return x/magnitude, y/magnitude, z/magnitude

#rotate 3D points around a vector
def rotation3D(x,y,z,point,angle):
    axis = norm(x,y,z)
    x,y,z= axis[0], axis[1], axis[2]
    m11 = 1+(1-math.cos(angle))*(x**2 -1)
    m12 = z*math.sin(angle)+x*y*(angle-math.cos(angle))
    m13 = -y*math.sin(angle)+x*z*(1-math.cos(angle))

    m21 = -z*math.sin(angle)+x*y*(1-math.cos(angle))
    m22 = 1+(1-math.cos(angle))*(y**2-1)
    m23 = x*math.sin(angle)+y*z*(1-math.cos(angle))

    m31 = y*math.sin(angle)+x*z*(1-math.cos(angle))
    m32 = -x*math.sin(angle)+y*z*(1-math.cos(angle))
    m22 = 1+(1-math.cos(angle))*(z**2-1)
    rotationMatrix = [[m11,m12,m13],[m21,m22,m23],[m31,m32,33]]    
    return matMulti(rotationMatrix, reshape(point,3,1))
        

