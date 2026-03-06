import pygame as pg

class Button(pg.Rect):
    def __init__(self, x, y, width, height, color):
        pg.Rect.__init__(self, x, y, width, height)
        self.color = color
        self.function = None
        self.label = None
        self.label_rect = None
        self.wait = False
        self.rect1 = None
        self.rect_color = None
        self.change = False


    def isClicked(self,x,y,game,mouse):
        if self.left <= x <= self.right and self.top <= y <= self.bottom:
            self.change = True
            self.add_wrap(7, color=(167, 252, 0))
            if mouse[0] and not self.wait:
                self.wait = True
            elif not(mouse[0]) and self.wait:
                if self.function != None:
                    self.function(game)
                    self.wait = False
                    return True
        elif self.wait:
            self.rect1 = self.oddrect1
            self.rect_color = self.odd_color
            self.change = False
            self.wait = False
        else:
            self.add_wrap(4, color=(157, 151, 151))
        return False

    def add_wrap(self,width,color= (72,6,7),ch = False):
        if not(ch):
            self.rect1 = pg.Rect(self.x-width,self.y-width,self.width+width*2,self.height+width*2)
            self.rect_color = color
            self.oddrect1 = self.rect1
            self.odd_color = self.rect_color
        else:
            self.rect1 = pg.Rect(self.x - width, self.y - width, self.width + width * 2, self.height + width * 2)
            self.rect_color = color


    def set_text(self, text, string, color=(0, 255, 0)):
        self.label = text.render(string, True,color )
        self.label_rect = self.label.get_rect(center=self.center)



    def add_function(self,function):
        self.function = function

    def draw(self,screen):
        if self.rect1 != None:
            pg.draw.rect(screen,self.rect_color,self.rect1)
        pg.draw.rect(screen,(255,255,255),self)
        if self.label != None:
            screen.blit(self.label, self.label_rect)
