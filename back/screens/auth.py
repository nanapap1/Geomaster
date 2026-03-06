import pygame as pg

from front.components.button import Button
from front.components.entry import Entry
from front.components.popup import Popup
from back.entity import User
from back.models import Screen


class Auth:
    def __init__(self, game):
        self.width = game.screen.get_width() / 5
        width = self.width
        height = game.screen.get_height() / 12
        self.one = Button(game.screen.get_width() / 3 - self.width / 2, game.screen.get_height() / 6 * 4, self.width, height,
                          color=(255, 0, 0))
        self.one.set_text(game.font_static, "РЕГИСТРАЦИЯ",color=(176, 0, 0))
        self.one.add_function(self.onef)
        self.one.add_wrap(4,color=(157,151,151))
        self.two = Button(game.screen.get_width() / 3 * 2 - self.width / 2, game.screen.get_height() / 6 * 4, self.width, height,
                          color=(255, 0, 0))
        self.two.add_function(self.twof)
        self.two.set_text(game.font_static, "ВХОД",color=(176, 0, 0))
        self.two.add_wrap(4,color=(157,151,151))

        self.one_e = Entry(game.screen.get_width() / 2 - width / 2, game.screen.get_height() / 6 * 2, width, height,
                          color=(255, 0, 0))
        self.one_e.def_text = "Логин"
        self.one_e.texts = ""
        self.two_e = Entry(game.screen.get_width() / 2 - width / 2, game.screen.get_height() / 6 * 3, width, height,
                           color=(255, 0, 0))
        self.one_e.add_wrap(4, color=(157, 151, 151))
        self.two_e.add_wrap(4, color=(157, 151, 151))
        self.two_e.def_text = "Пароль"
        self.two_e.texts = ""
        self.two_e.set_hides()
        self.sbros(game)

        text = "GEOMASTER"
        self.label = game.font_header.render(text, True, (169, 169, 176))

    def draw(self, game):
        if isinstance(game.fon_auth,pg.Rect):
            pg.draw.rect(game.screen, (0, 0, 0), game.fon_auth)
        else:
            game.screen.blit(game.fon_auth,(0,0))
        self.one.draw(game.screen)
        self.two.draw(game.screen)
        self.one_e.draw(game.screen)
        self.two_e.draw(game.screen)

        label_rect = self.label.get_rect(center=(game.screen.get_width() / 2, game.screen.get_height() / 5))
        game.screen.blit(self.label, label_rect)

    def onef(self,game):
        self.sbros(game)
        game.state = Screen.register

    def twof(self,game):
            user = User(self.one_e.texts)
            if user.exists(self.two_e.texts):
                game.state = Screen.start
                self.sbros(game)
                game.user = user
            else:
                Popup.wrongauth()

    def one_input(self,event,font):
        if self.one_e.input:
            self.two_e.change_input(font)
        self.one_e.validate(event,font,spec="+_-–=!@#$$%^&*?|<>",alnum=True)

    def two_input(self,event,font):
        if self.two_e.input:
            self.one_e.change_input(font)
        self.two_e.validate(event,font,spec="+_-–=!@#$$%^&*?|<>",alnum=True)

    def sbros(self,game):
        self.one_e.input = False
        self.one_e.texts = self.one_e.def_text
        self.one_e.default = True
        self.one_e.set_text(game.font_static,color=(192,192,192))
        self.two_e.texts = self.two_e.def_text
        self.two_e.default = True
        self.two_e.input = False
        self.two_e.set_text(game.font_static, color=(192,192,192))



