import pygame as pg

from back.geometry import Point
from back.geometry.polyline import Polyline


class Field(pg.Rect):
    cletka = 100

    def __init__(self,x,y,width,height):
        pg.Rect.__init__(self,x,y,width,height)
        self.color = (94,33,41)
        self.polyline = Polyline()
        self.set_polyline()
        self.temporary = None
        self.temporary_point = None
        self.need = None
        self.atributtes = []


    def draw(self,game):
        pg.draw.rect(game.screen,self.color,self)
        for x in range(1,int(self.width/self.cletka)+1):
              pg.draw.line(game.screen, (192, 192, 193) , (self.cletka*x,0), (self.cletka*x, self.height))
        for y in range(1,int(self.height/self.cletka)+1):
               pg.draw.line(game.screen, (192, 192, 193) , (0,self.cletka*y), (self.width,self.cletka*y))
        self.polyline.draw(game)
        if self.temporary != None:
            self.temporary.draw(game)
        if self.temporary_point != None:
            self.temporary_point.draw(game)
        for x in range(0,len(self.atributtes)):
            self.atributtes[x].draw(game)


    def isInside(self,x,y):
        if self.left <= x <= self.right and self.top <= y <= self.bottom:
            return True
        return False

    def set_polyline(self):
        end_x = int(self.width/self.cletka) + 1
        end_y = int(self.height/self.cletka) + 1
        if self.width % self.cletka ==0:
            end_x = int(self.width / self.cletka)
        if self.height % self.cletka ==0:
            end_y = int(self.height / self.cletka)
        for x in range(1,end_x):
            for y in range(1, end_y):
                self.polyline.addPoint(Point(self.cletka*x,self.cletka * y))
        self.polyline.set_list(end_x-1,end_y-1)
