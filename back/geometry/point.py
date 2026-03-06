import pygame as pg

class Point:

    def __init__(self,x,y,color = (255,207,64)):
        self.center = (x,y)
        self.radius = 7
        self.connected_line = None
        self.color = color

    def draw(self,game):
        pg.draw.circle(game.screen,self.color, self.center, self.radius)

    def isFigure(self, x, y):
        return ((x - self.center[0]) ** 2 + (y - self.center[1]) ** 2) <= (self.radius) ** 2

    def changeColor(self,color):
        self.color = color

    def __gt__(self, other):
        return self.center > other.center

    def __str__(self):
        return str(self.center)