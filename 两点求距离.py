import math
class Point:
    def __init__(self,x1,y1):
        self.x = x1
        self.y = y1
        #在用init函数的时候别忘了加self.，不然改动无法带到def外面。
        #用self之前不用初始化x、y。效果等同于在函数外定义x = 某某某。
class Line:
    def __init__(self,x1,x2):
        self.x = x1.x - x2.x
        self.y = x1.y - x2.y
        
def getLine(l0):
    return math.sqrt(l0.x**2+l0.y**2)

p1 = Point(1,1)
p2 = Point(4,5)
l = Line(p1,p2)
print(getLine(l))
