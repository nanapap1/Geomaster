import numpy as np
import random
class Task:

    def __init__(self,game):
        self.game = game
        self.field = game.fig.fig
        pass


    def sered(self,quatity,param=False):
        self.game.check.sered = True
        #сделать с=здесь проверку
        return self.points(quatity,param)

    def nothing(self,quatity,param=False):
        return []

    def points(self,quatity,param=False):
        poit = None
        self.check = []
        ls = [poit:=self.point(param,poit) for x in range(0,quatity)]
        return ls

    def point(self,param=False,point=None):
        if point is None:
            select=np.random.choice(self.field.polyline.points[3:7,3:6].copy().flatten(),size =1)[0]
        else:
            if param:
                prop = random.choice(["updown","turn"])
                if prop =="turn":
                    ls = [x for x in range(1,self.field.polyline.points.shape[0]+1) if x+3 <= point.center[0] // self.field.cletka or point.center[0] // self.field.cletka <= x-3]
                    num = random.choice(ls)
                    select = self.field.polyline.points[num-1,point.center[1]//self.field.cletka -1]
                elif prop =="updown":
                    ls = [x for x in range(1, self.field.polyline.points.shape[1]+1) if
                            x + 3 <= point.center[1] // self.field.cletka or point.center[1] // self.field.cletka<= x-3]
                    num = random.choice(ls)
                    select = self.field.polyline.points[point.center[0]//self.field.cletka -1,num-1]
            else:
                ls = [x for x in range(1, self.field.polyline.points.shape[0] + 1) if
                      x + 3 <= point.center[0] // self.field.cletka or point.center[0] // self.field.cletka <= x - 3]
                num = random.choice(ls)
                ls = [x for x in range(1, self.field.polyline.points.shape[1] + 1) if
                      x + 3 <= point.center[1] // self.field.cletka or point.center[1] // self.field.cletka <= x - 3]
                num2 = random.choice(ls)
                select = self.field.polyline.points[num-1, num2 - 1]
        if select not in self.check:
            self.check.append(select)
            return select
        else:
            return self.point(param,point)








