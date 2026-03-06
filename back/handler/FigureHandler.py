from back.geometry import Point
from front.components.field import Field
from back.geometry.polyline import Polyline


class FigureHandler:
    temp_color = (152,251,152)
    def __init__(self,fig):
        self.field = fig
        self.end = None
        self.poi = None
        self.margin = Field.cletka * 0.2


    def hander(self,pressed,current_pos,current_status,game):

        if current_status[0] and self.field.get_field().isInside(*current_pos) and self.poi == None:
            wait = self.check(current_pos)
            if len(wait)==2:
                self.poi = self.field.get_field().polyline.get_point(wait,Field.cletka)
                if self.poi != None and self.poi not in self.field.get_field().polyline.lines.keys():
                    self.field.get_field().polyline.addDrawPoint(self.poi)

        elif current_status[0] and self.poi != None:
            wait = self.check(current_pos)
            if len(wait)==2 and self.poi.center != wait:
                self.end = self.field.get_field().polyline.get_point(wait,Field.cletka)
                if self.end != None and self.end != self.poi:
                    one = Polyline()
                    self.end = Point(self.end.center[0],self.end.center[1],color=self.temp_color)
                    one.addDrawPoint(self.poi)
                    one.addLineNotEnd(self.poi, self.end)
                    self.set_temporary(one,self.end)
                else:
                    self.set_temporary()

            elif self.poi.center != wait and len(wait)!=2:
                if self.isField(current_pos):
                    self.end = Point(x = current_pos[0],y=current_pos[1],color=self.temp_color)
                    one = Polyline()
                    one.addDrawPoint(self.poi)
                    one.addLineNotEnd(self.poi, self.end)
                    self.set_temporary(one)
                else:
                    self.set_temporary()

        elif not(current_status[0]) and self.poi != None:
            wait = self.check(current_pos)
            if len(wait)==2 and self.poi.center != wait:
                    self.end = self.field.get_field().polyline.get_point(wait,Field.cletka)
                    if self.end != None:
                        if self.poi not in self.field.get_field().polyline.lines.keys():
                            self.field.get_field().polyline.addDrawPoint(self.poi)
                        self.field.get_field().polyline.addLine(self.poi,self.end,Field.cletka)

            self.end = None
            self.poi = None
            self.set_temporary()

    def set_temporary(self,polyline = None,point=None):
        self.field.get_field().temporary = polyline
        self.field.get_field().temporary_point = point


    def check(self,current_pos):
        wait = list()
        if current_pos[0] % Field.cletka <= self.margin and Field.cletka  <= current_pos[0] <= self.field.get_field().width:
            wait.append(current_pos[0] - current_pos[0] % Field.cletka)
        elif (Field.cletka - current_pos[0] % Field.cletka) <= self.margin and Field.cletka  <= current_pos[0] < self.field.get_field().width:
            wait.append(current_pos[0] + (Field.cletka - current_pos[0] % Field.cletka))
        if current_pos[1] % Field.cletka <= self.margin and Field.cletka  <= current_pos[1] <= self.field.get_field().height:
            wait.append(current_pos[1] - current_pos[1] % Field.cletka)
            wait = tuple(wait)
        elif (Field.cletka - current_pos[1] % Field.cletka) <= self.margin and Field.cletka  <= current_pos[1] < self.field.get_field().height:
            wait.append(current_pos[1] + (Field.cletka - current_pos[1] % Field.cletka))
            wait = tuple(wait)
        return wait

    def isField(self,current_pos):
        return Field.cletka//2  <= current_pos[0] <= self.field.get_field().width - 10 and Field.cletka//2  <= current_pos[1] < self.field.get_field().height - 10




