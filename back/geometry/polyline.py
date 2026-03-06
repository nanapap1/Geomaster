import math

import pygame as pg
import pygame.draw
from pygame.examples.music_drop_fade import play_next
import numpy as np

class Polyline:

    def __init__(self,color=(255,0,0)):
        self.connections = dict()
        self.color = color
        self.points = None
        self.lines  = dict()

    def addPoint(self,point):
        self.connections.update({point: set()})

    def addDrawPoint(self,point):
        self.lines.update({point: set()})


    def addLine(self,start,end,cletka):
        if start not in self.lines.keys():
            self.lines.update({start: set()})
        self.lines[start].add(end)
        if end not in self.lines.keys():
            self.lines.update({end: set()})
        self.mark(start,end,cletka)

    def addLineNotEnd(self, start, end):
        self.lines[start].add(end)


    def draw(self,game):
        for k,v in self.lines.items():
            k.draw(game)
            for point in v:
                pygame.draw.aaline(game.screen, point.color, k.center, point.center)

    def hasPoint(self,point):
        return point in self.connections.keys()

    def update(self,polyline):
        for key,value in polyline.connections.items():
            self.connections.update({key: value})

    def search(self,length):
        self.all_variants = list()
        print()
        for x in self.connections.keys():
                self.path = list()
                if len(self.connections[x]) >0:
                    self.dfs(x, length,x)
        return self.all_variants

    def dfs(self,point,length,start,comefrome=None):
        if len(self.path) >= length:
            return
        self.path.append(point)
        for one in self.connections[point]:
            if one == start and len(self.path) == length:
                candidate = sorted(self.path)
                if candidate not in self.all_variants:
                    self.all_variants.append(candidate)
            elif one != start and one != comefrome and one not in self.path:
                self.dfs(one,length,start,point)
        self.path.pop(-1)

    def set_list(self,x,y):
        self.points = np.array(list(self.connections.keys())).reshape(x,y)

    def get_point(self,wait,cletka):
        if wait[0]//cletka-1 < self.points.shape[0] and wait[1]//cletka-1 < self.points.shape[1] :
            return self.points[wait[0]//cletka-1,wait[1]//cletka-1]

    def mark(self,start,end,cletka):
        star1 = min(start.center[0] // cletka, end.center[0] // cletka)
        end1 = max(end.center[0] // cletka, start.center[0] // cletka)
        star2 = min(start.center[1] // cletka, end.center[1] // cletka)
        end2 = max(end.center[1] // cletka, start.center[1] // cletka)
        ls = list(self.points[star1 - 1:end1, star2 - 1:end2].flatten())
        node = list()
        for one in ls:
            if ((one.center[0]//cletka - start.center[0]//cletka) * (end.center[1]//cletka - start.center[1]//cletka)) == ((one.center[1]//cletka - start.center[1]//cletka) * (end.center[0]//cletka - start.center[0]//cletka)):
                    node.append(one)
        ending = len(node)
        for x in range(ending):
            for one in range(x + 1, ending):
                self.connections[node[x]].add(node[one])
                self.connections[node[one]].add(node[x])
























