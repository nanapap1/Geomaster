from front.components import Button
from back.models.Screen import Screen
import pygame as pg

class Start:

    def __init__(self,game):
        width = game.screen.get_width() / 5
        height = 120
        self.one = Button(game.screen.get_width() / 2 - width / 2, game.screen.get_height() / 5*1+height//2, width, height,
                     color=(255, 0, 0))
        self.one.add_function(self.onef)
        self.one.set_text(game.font_static, "ЗАДАЧИ",color=(176, 0, 0))
        self.one.add_wrap(4, color=(157, 151, 151))
        self.two = Button(game.screen.get_width() / 2 - width / 2, game.screen.get_height() / 5*2+height//2, width, height,
                     color=(255, 0, 0))
        self.two.add_function(self.twof)
        self.two.set_text(game.font_static, "БАЗА ЗНАНИЙ", color=(176, 0, 0))
        self.two.add_wrap(4, color=(157, 151, 151))
        self.three = Button(game.screen.get_width() / 2 - width / 2, game.screen.get_height() / 5*3+height//2, width, height,
                       color=(255, 0, 0))
        self.three.set_text(game.font_static, "НАСТРОЙКИ", color=(176, 0, 0))
        self.three.add_wrap(4, color=(157, 151, 151))
        self.three.add_function(self.threef)
        text = "GEOMASTER"
        self.label = game.font_header.render(text, True, (169, 169, 176))

    def objects(self):
        return [self.one, self.two, self.three, self.label]

    def draw(self,game):
        if isinstance(game.fon_auth,pg.Rect):
            pg.draw.rect(game.screen, (0, 0, 0), game.fon_auth)
        else:
            game.screen.blit(game.fon_auth,(0,0))
        self.one.draw(game.screen)
        self.two.draw(game.screen)
        self.three.draw(game.screen)
        label_rect = self.label.get_rect(center=(game.screen.get_width() / 2, game.screen.get_height()  /8 + 40))
        game.screen.blit(self.label, label_rect)

    def onef(self,game):
        game.fig.load_task(game)
        game.state = Screen.figure

    def twof(self,game):
        game.know.clear()
        game.know.render_text(game,"Выберите справочник")
        game.state = Screen.know

    def threef(self,game):
        game.state = Screen.set



