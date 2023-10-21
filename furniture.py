import math 
from colorsys import rgb_to_hls, hls_to_rgb
from shape import *

#furniture class
class Furniture: 
    def __init__(self, position,scale, angle):
        self.shapes = []
        self.position = position
        self.scale=scale
        self.angle=angle
    
    def getPosition(self):
        return self.position
    
    def setPosition(self, position):
        self.position=position

    def getShapes(self):
        return self.shapes

    def getType(self):
        result = f"{type(self)}".strip("<class 'furniture").strip("'>").strip(".")
        return result
    
    def getScale(self):
        return self.scale
    
    def getAngle(self):
        return self.angle

    def setScale(self, scale):
        self.scale=scale
    
    def setAngle(self, angle):
        self.angle=angle

class Bed(Furniture):
    def draw(self, canvas):
        self.shapes =[]
        points = [[-1.2,-1.2,1.2],[1,-1.2,1.2],[1,1.2,1.2],[-1.2,1.2,1.2],\
        [-1.2,-1.2,-1],[1,-1.2,-1],[1,1.2,-1],[-1.2,1.2,-1]]
        blanket = Cuboid(self.angle,points,self.scale, "#cc80ed")
        blanket.setPosition(self.position)
        self.shapes.append(blanket)

        points2 = [[1,-1,1],[2,-1,1],[2,1,1],[1,1,1],\
        [1,-1,-1],[2,-1,-1],[2,1,-1],[1,1,-1]]
        nblanket = Cuboid(self.angle, points2, self.scale,"#f2bd77")
        nblanket.rotation3DCube(0,0,1, self.angle)
        nblanket.setPosition(self.position)
        self.shapes.append(nblanket)

        points3 = [[1.3,-0.7,1.3],[1.8,-0.7,1.3],[1.8,0.7,1.3],[1.3,0.7,1.3],\
        [1.3,-0.7,1],[1.8,-0.7,1],[1.8,0.7,1],[1.3,0.7,1]]
        pillow = Cuboid(self.angle, points3, self.scale, "#b787ed")
        pillow.rotation3DCube(0,0,1, self.angle)
        pillow.setPosition(self.position)
        self.shapes.append(pillow)

        points4 = [[2,-1,1.3],[2.3,-1,1.3],[2.3,1,1.3],[2,1,1.3],\
        [2,-1,-1],[2.3,-1,-1],[2.3,1,-1],[2,1,-1]]
        head = Cuboid(self.angle, points4, self.scale, "#735226")
        head.rotation3DCube(0,0,1, self.angle)
        head.setPosition(self.position)
        self.shapes.append(head)

        angle = self.angle
        while angle<0:
            angle+=math.pi*2
        while angle>=math.pi*2 and angle>0:
            angle-=math.pi*2
        #self shapes = blanket,nblanket,pillow,head
        if angle>=math.pi and angle<=math.pi*2:
            head.draw(canvas)
            nblanket.draw(canvas)
            pillow.draw(canvas)
            blanket.draw(canvas)
        else:
            blanket.draw(canvas)
            nblanket.draw(canvas)
            pillow.draw(canvas)
            head.draw(canvas)

class Drawer(Furniture):
    def draw(self,canvas):
        self.shapes=[]
        points = [[-1,-1,0],[1,-1,0],[1,1,0],[-1,1,0],[-1,-1,-1],[1,-1,-1],\
    [1,1,-1],[-1,1,-1]]
        lDrawer = Cuboid(self.angle,points,self.scale, "#734829")
        lDrawer.setPosition(self.position)
        self.shapes.append(lDrawer)

        points2 = [[-1,-1,0.05],[1,-1,0.05],[1,1,0.05],[-1,1,0.05],[-1,-1,0],[1,-1,0],\
    [1,1,0],[-1,1,0]]
        divider = Cuboid(self.angle, points2, self.scale, "#332012")
        divider.setPosition(self.position)
        self.shapes.append(divider)

        points2 = [[-1,-1,1.05],[1,-1,1.05],[1,1,1.05],[-1,1,1.05],[-1,-1,0.05],[1,-1,0.05],\
    [1,1,0.05],[-1,1,0.05]]
        uDrawer = Cuboid(self.angle, points2, self.scale, "#734829")
        uDrawer.setPosition(self.position)
        self.shapes.append(uDrawer)

        points3 = [[1,-0.3,0.75],[1.1,-0.3,0.75],[1.1,0.3,0.75],[1,0.3,0.75],\
        [1,-0.3,0.45],[1.1,-0.3,0.45],[1.1,0.3,0.45],[1,0.3,0.45]]
        handle1 = Cuboid(self.angle, points3, self.scale,"#332012")
        handle1.setPosition(self.position)
        self.shapes.append(handle1)

        points4 = [[1,-0.3,-0.3],[1.1,-0.3,-0.3],[1.1,0.3,-0.3],[1,0.3,-0.3],\
        [1,-0.3,-0.6],[1.1,-0.3,-0.6],[1.1,0.3,-0.6],[1,0.3,-0.6]]
        handle2 = Cuboid(self.angle, points4, self.scale,"#332012")
        handle2.setPosition(self.position)
        self.shapes.append(handle2)

        angle = self.angle
        while angle<0:
            angle+=math.pi*2
        while angle>=math.pi*2 and angle>0:
            angle-=math.pi*2
        #self shapes = lDrawer, uDrawer,handle1, handle2, divider
        if angle>=math.pi and angle<=math.pi*2:
            lDrawer.draw(canvas)
            divider.draw(canvas)
            uDrawer.draw(canvas)
        else:
            lDrawer.draw(canvas)
            divider.draw(canvas)
            uDrawer.draw(canvas)
            handle2.draw(canvas)
            handle1.draw(canvas)

class Couch(Furniture):
    def draw(self,canvas):
        self.shapes=[]
        points = [[-1,-1,1.3],[-0.5,-1,1.3],[-0.5,1,1.3],[-1,1,1.3],[-1,-1,-1],[-0.5,-1,-1],\
        [-0.5,1,-1],[-1,1,-1]]
        armRest1 = Cuboid(self.angle, points, self.scale,"#5886d6")
        armRest1.setPosition(self.position)
        self.shapes.append(armRest1)

        points2 = [[-0.5,-1,1],[1.5,-1,1],[1.5,1,1],[-0.5,1,1],\
        [-0.5,-1,0.4],[1.5,-1,0.4],[1.5,1,0.4],[-0.5,1,0.4]]
        cushion1 = Cuboid(self.angle, points2, self.scale,"#4b75bd")
        cushion1.setPosition(self.position)
        self.shapes.append(cushion1)

        points3 = [[-0.5,-1,0.4],[1.5,-1,0.4],[1.5,1,0.4],[-0.5,1,0.4],\
        [-0.5,-1,-1],[1.5,-1,-1],[1.5,1,-1],[-0.5,1,-1]]
        base1 = Cuboid(self.angle, points3, self.scale,"#6690d9")
        base1.setPosition(self.position)
        self.shapes.append(base1)

        points4 = [[1.5,-1,1],[3.5,-1,1],[3.5,1,1],[1.5,1,1],\
        [1.5,-1,0.4],[3.5,-1,0.4],[3.5,1,0.4],[1.5,1,0.4]]
        cushion2 = Cuboid(self.angle, points4, self.scale,"#4b75bd")
        cushion2.setPosition(self.position)
        self.shapes.append(cushion2)

        points5 = [[1.5,-1,0.4],[3.5,-1,0.4],[3.5,1,0.4],[1.5,1,0.4],\
        [1.5,-1,-1],[3.5,-1,-1],[3.5,1,-1],[1.5,1,-1]]
        base2 = Cuboid(self.angle, points5, self.scale,"#6690d9")
        base2.setPosition(self.position)
        self.shapes.append(base2)

        points6 = [[3.5,-1,1.3],[4,-1,1.3],[4,1,1.3],[3.5,1,1.3],\
        [3.5,-1,-1],[4,-1,-1],[4,1,-1],[3.5,1,-1]]
        armRest2 = Cuboid(self.angle, points6, self.scale,"#5886d6")
        armRest2.setPosition(self.position)
        self.shapes.append(armRest2)

        points7=[[-0.5,-1.5,2.3],[3.5,-1.5,2.3],[3.5,-1,2.3],[-0.5,-1,2.3],\
        [-0.5,-1.5,-1],[3.5,-1.5,-1],[3.5,-1,-1],[-0.5,-1,-1]]
        back = Cuboid(self.angle, points7, self.scale,"#6690d9")
        back.setPosition(self.position)
        self.shapes.append(back)

        angle = self.angle
        while angle<0:
            angle+=math.pi*2
        while angle>=math.pi*2 and angle>0:
            angle-=math.pi*2
        #self shapes = armRest1,cushion1,base1,cushion2, base2,armRest2, back
        if angle>=math.pi/2 and angle<=math.pi:
            armRest1.draw(canvas)
            base1.draw(canvas)
            cushion1.draw(canvas)
            base2.draw(canvas)
            cushion2.draw(canvas)
            armRest2.draw(canvas)
            back.draw(canvas)
        elif angle>0 and angle<=math.pi/2:
            back.draw(canvas)
            armRest1.draw(canvas)
            base1.draw(canvas)
            cushion1.draw(canvas)
            base2.draw(canvas)
            cushion2.draw(canvas)
            armRest2.draw(canvas)
        elif angle<math.pi*3/2 and angle>math.pi:
            armRest2.draw(canvas)
            base2.draw(canvas)
            cushion2.draw(canvas)
            base1.draw(canvas)
            cushion1.draw(canvas)
            back.draw(canvas)
            armRest1.draw(canvas)
        else:
            back.draw(canvas)
            armRest2.draw(canvas)
            base2.draw(canvas)
            cushion2.draw(canvas)
            base1.draw(canvas)
            cushion1.draw(canvas)
            armRest1.draw(canvas)

class coffeeTable(Furniture):
    def draw(self,canvas):
        self.shapes = []
        points = [[-1,-1,1],[1,-1,1],[1,1,1],[-1,1,1],\
        [-1,-1,0.5],[1,-1,0.5],[1,1,0.5],[-1,1,0.5]]
        face = Cuboid(self.angle, points, self.scale, "#66d1d9")
        face.setPosition(self.position)
        self.shapes.append(face)

        points2 = [[-1,-1,0.5],[-0.8,-1,0.5],[-0.8,-0.8,0.5],[-1,-0.8,0.5],\
        [-1,-1,-1],[-0.8,-1,-1],[-0.8,-0.8,-1],[-1,-0.8,-1]]
        leg1 = Cuboid(self.angle, points2, self.scale, "#66d1d9")
        leg1.setPosition(self.position)
        self.shapes.append(leg1)

        points3 = [[0.8,-1,0.5],[1,-1,0.5],[1,-0.8,0.5],[0.8,-0.8,0.5],\
        [0.8,-1,-1],[1,-1,-1],[1,-0.8,-1],[0.8,-0.8,-1]]
        leg2 = Cuboid(self.angle, points3, self.scale, "#66d1d9")
        leg2.setPosition(self.position)
        self.shapes.append(leg2)

        points4 = [[0.8,0.8,0.5],[1,0.8,0.5],[1,1,0.5],[0.8,1,0.5],\
        [0.8,0.8,-1],[1,0.8,-1],[1,1,-1],[0.8,1,-1]]
        leg3 = Cuboid(self.angle, points4, self.scale, "#66d1d9")
        leg3.setPosition(self.position)
        self.shapes.append(leg3)

        points5 = [[-1,0.8,0.5],[-0.8,0.8,0.5],[-0.8,1,0.5],[-1,1,0.5],\
        [-1,0.8,-1],[-0.8,0.8,-1],[-0.8,1,-1],[-1,1,-1]]
        leg4 = Cuboid(self.angle, points5, self.scale, "#66d1d9")
        leg4.setPosition(self.position)
        self.shapes.append(leg4)

        angle = self.angle
        while angle<0:
            angle+=math.pi*2
        while angle>=math.pi*2 and angle>0:
            angle-=math.pi*2
        #self shapes = armRest1,cushion1,base1,cushion2, base2,armRest2, back
        if angle>=math.pi and angle<=math.pi*2:
            leg4.draw(canvas)
            leg3.draw(canvas)
            leg2.draw(canvas)
            leg1.draw(canvas)
            face.draw(canvas)
        else:
            leg2.draw(canvas)
            leg1.draw(canvas)
            leg3.draw(canvas)
            leg4.draw(canvas)
            face.draw(canvas)
class Chair(Furniture):
    def draw(self,canvas):
        self.shapes = []
        points = [[-1,-1,1],[1,-1,1],[1,1,1],[-1,1,1],\
        [-1,-1,0.5],[1,-1,0.5],[1,1,0.5],[-1,1,0.5]]
        face = Cuboid(self.angle, points, self.scale, "#a86925")
        face.setPosition(self.position)
        self.shapes.append(face)

        points2 = [[-1,-1,0.5],[-0.8,-1,0.5],[-0.8,-0.8,0.5],[-1,-0.8,0.5],\
        [-1,-1,-1],[-0.8,-1,-1],[-0.8,-0.8,-1],[-1,-0.8,-1]]
        leg1 = Cuboid(self.angle, points2, self.scale, "#a86925")
        leg1.setPosition(self.position)
        self.shapes.append(leg1)

        points3 = [[0.8,-1,0.5],[1,-1,0.5],[1,-0.8,0.5],[0.8,-0.8,0.5],\
        [0.8,-1,-1],[1,-1,-1],[1,-0.8,-1],[0.8,-0.8,-1]]
        leg2 = Cuboid(self.angle, points3, self.scale, "#a86925")
        leg2.setPosition(self.position)
        self.shapes.append(leg2)

        points4 = [[0.8,0.8,0.5],[1,0.8,0.5],[1,1,0.5],[0.8,1,0.5],\
        [0.8,0.8,-1],[1,0.8,-1],[1,1,-1],[0.8,1,-1]]
        leg3 = Cuboid(self.angle, points4, self.scale, "#a86925")
        leg3.setPosition(self.position)
        self.shapes.append(leg3)

        points5 = [[-1,0.8,0.5],[-0.8,0.8,0.5],[-0.8,1,0.5],[-1,1,0.5],\
        [-1,0.8,-1],[-0.8,0.8,-1],[-0.8,1,-1],[-1,1,-1]]
        leg4 = Cuboid(self.angle, points5, self.scale, "#a86925")
        leg4.setPosition(self.position)
        self.shapes.append(leg4)

        points6 = [[-1,-1,3.5],[1,-1,3.5],[1,-0.8,3.5],[-1,-0.8,3.5],\
        [-1,-1,1],[1,-1,1],[1,-0.8,1],[-1,-0.8,1]]
        back = Cuboid(self.angle, points6, self.scale, "#a86925")
        back.setPosition(self.position)
        self.shapes.append(back)

        angle = self.angle
        while angle<0:
            angle+=math.pi*2
        while angle>=math.pi*2 and angle>0:
            angle-=math.pi*2
        #self shapes = armRest1,cushion1,base1,cushion2, base2,armRest2, back
        if angle>=math.pi and angle<=math.pi*2:
            leg4.draw(canvas)
            leg3.draw(canvas)
            leg2.draw(canvas)
            leg1.draw(canvas)
            face.draw(canvas)
            back.draw(canvas)
        else:
            leg2.draw(canvas)
            leg1.draw(canvas)
            leg3.draw(canvas)
            leg4.draw(canvas)
            face.draw(canvas)
            back.draw(canvas)

class singleSofa(Furniture):
    def draw(self,canvas):
        self.shapes = []
        points = [[-1,-1,1.3],[-0.5,-1,1.3],[-0.5,1,1.3],[-1,1,1.3],[-1,-1,-1],[-0.5,-1,-1],\
        [-0.5,1,-1],[-1,1,-1]]
        armRest1 = Cuboid(self.angle, points, self.scale,"#8763eb")
        armRest1.setPosition(self.position)
        self.shapes.append(armRest1)

        points2 = [[-0.5,-1,1],[1.5,-1,1],[1.5,1,1],[-0.5,1,1],\
        [-0.5,-1,0.4],[1.5,-1,0.4],[1.5,1,0.4],[-0.5,1,0.4]]
        cushion = Cuboid(self.angle, points2, self.scale,"#7d5ae0")
        cushion.setPosition(self.position)
        self.shapes.append(cushion)

        points3 = [[-0.5,-1,0.4],[1.5,-1,0.4],[1.5,1,0.4],[-0.5,1,0.4],\
        [-0.5,-1,-1],[1.5,-1,-1],[1.5,1,-1],[-0.5,1,-1]]
        base = Cuboid(self.angle, points3, self.scale,"#8f6eeb")
        base.setPosition(self.position)
        self.shapes.append(base)

        points4 = [[1.5,-1,1.3],[2,-1,1.3],[2,1,1.3],[1.5,1,1.3],
        [1.5,-1,-1],[2,-1,-1],[2,1,-1],[1.5,1,-1]]
        armRest2 = Cuboid(self.angle, points4, self.scale,"#8763eb")
        armRest2.setPosition(self.position)
        self.shapes.append(armRest2)

        points5=[[-0.5,-1.5,2.7],[1.5,-1.5,2.7],[1.5,-1,2.7],[-0.5,-1,2.7],\
        [-0.5,-1.5,-1],[1.5,-1.5,-1],[1.5,-1,-1],[-0.5,-1,-1]]
        back = Cuboid(self.angle, points5, self.scale,"#8f6eeb")
        back.setPosition(self.position)
        self.shapes.append(back)

        angle = self.angle
        while angle<0:
            angle+=math.pi*2
        while angle>=math.pi*2 and angle>0:
            angle-=math.pi*2
        if angle>=0 and angle<=math.pi/2:
            back.draw(canvas)
            armRest1.draw(canvas)
            base.draw(canvas)
            cushion.draw(canvas)
            armRest2.draw(canvas)
        elif angle>=math.pi/2 and angle<=math.pi:
            armRest1.draw(canvas)
            base.draw(canvas)
            cushion.draw(canvas)
            armRest2.draw(canvas)
            back.draw(canvas)
        elif angle>=math.pi and angle<=math.pi*3/2:
            armRest2.draw(canvas)
            base.draw(canvas)
            cushion.draw(canvas)
            back.draw(canvas)
            armRest1.draw(canvas)
        elif angle>=math.pi*3/2 and angle<=math.pi*2:
            back.draw(canvas)
            armRest2.draw(canvas)
            base.draw(canvas)
            cushion.draw(canvas)
            armRest1.draw(canvas)






