from idlelib.colorizer import prog_group_name_to_tag

import pygame as pg

class Entry (pg.Rect):
    def __init__(self, x, y, width, height, color):
        pg.Rect.__init__(self, x, y, width, height)
        self.color = color
        self.function = None
        self.label = None
        self.label_rect = None
        self.texts = ""
        self.wait = False
        self.input = False
        self.delete = False
        self.count = 10
        self.hide = False
        self.rect1 = None
        self.rect_color = None
        self.change = False
        self.default = True
        self.def_text=""


    def isClicked(self, x, y, game, mouse):
            if self.left <= x <= self.right and self.top <= y <= self.bottom:
                if mouse[0] and not self.wait:
                    self.wait = True
                elif not (mouse[0]) and self.wait:
                    self.input = not self.input
                    self.wait = False
            elif self.wait:
                self.wait = False

            if self.input and not(self.change):
                self.oddrect1 = self.rect1
                self.odd_color = self.rect_color
                self.change = True
                self.add_wrap(7,color=(167,252,0))
            elif not(self.input):
                if self.change:
                    self.rect1 = self.oddrect1
                    self.rect_color = self.odd_color
                    self.change = False

            if self.texts == "" and not(self.input):
                self.default = True
                self.texts = self.def_text
                self.set_text(game.font_static, color=(192, 192, 192))

    def change_input(self,font):
        if self.input:
            self.input = False
            if self.texts == "":
                self.default = True
                self.texts = self.def_text
                self.set_text(font, color=(192, 192, 192))


    def set_text(self,font,color=(0,0,0)):
        if not(self.hide) or self.default:
            self.label = font.render(self.texts, True, color)
        elif not(self.default):
            self.label = font.render("*" * len(self.texts), True,color)
        self.label_rect = self.label.get_rect(midleft=(self.midleft[0]+10,self.midleft[1]))
        if self.label_rect.right  >= self.right:
            self.label = font.render("Cлишком длинно", True, color)
        self.label_rect = self.label.get_rect(midleft=(self.midleft[0] + 10, self.midleft[1]))

    def get_text(self):
        return self.texts

    def set_hides(self):
        self.hide = True

    def add_wrap(self, width, color=(72, 6, 7)):
        self.rect1 = pg.Rect(self.x - width, self.y - width, self.width + width * 2, self.height + width * 2)
        self.rect_color = color


    def validate(self,event,font,spec=list(),alnum=False):
        self.count +=1
        if self.input and event !=None:
            if self.default:
                self.texts = ""
                self.default = False
            if event.key != pg.K_BACKSPACE and event.type == pg.KEYDOWN:
                symb = event.unicode
                if symb !=None:
                    if (alnum and symb.isalnum()) or symb in spec:
                            self.texts += symb
                            self.set_text(font)
            else:
                if event.type == pg.KEYDOWN:
                    self.delete = True
                elif event.type == pg.KEYUP and self.delete:
                    self.delete = False
                    self.count = 10

        if self.delete and self.count > 10 and self.texts != self.def_text:
                self.count = 0
                self.texts = self.texts[:-1]
                self.set_text(font)








    def draw(self,screen):
        if self.rect1 != None:
            pg.draw.rect(screen,self.rect_color,self.rect1)

        pg.draw.rect(screen,(255,255,255),self)
        if self.label != None:
            screen.blit(self.label, self.label_rect)


