from front.components import Button
from front.components.entry import Entry
from front.components.popup import Popup
from back.entity import User
from back.models import Screen
import pygame as pg

class Reg:
    def __init__(self,game):
        width = game.screen.get_width() / 5
        height = game.screen.get_height() / 12
        self.one = Button(game.screen.get_width() / 3 - width / 2, game.screen.get_height() / 6 * 4, width, height,
                          color=(255, 0, 0))
        self.one.set_text(game.font_static, "ОКНО ВХОДА",color=(176, 0, 0))
        self.one.add_function(self.onef)
        self.one.add_wrap(4, color=(157, 151, 151))

        self.two = Button(game.screen.get_width() / 3 * 2 - width / 2, game.screen.get_height() / 6 * 4, width, height,
                          color=(255, 0, 0))
        self.two.add_function(self.twof)
        self.two.set_text(game.font_static, "ЗАРЕГИСТРИРОВАТЬСЯ",color=(176, 0, 0))
        self.two.add_wrap(4, color=(157, 151, 151))

        self.one_e = Entry(game.screen.get_width() / 2 - width / 2, game.screen.get_height() / 6 * 1.5, width, height,
                           color=(255, 0, 0))
        self.one_e.def_text = "Уникальный логин"
        self.one_e.add_wrap(4, color=(157, 151, 151))
        self.two_e = Entry(game.screen.get_width() / 2 - width / 2, game.screen.get_height() / 6 * 2.25, width, height,
                           color=(255, 0, 0))
        self.two_e.def_text = "Пароль"
        self.two_e.set_hides()
        self.two_e.add_wrap(4, color=(157, 151, 151))
        self.three_e = Entry(game.screen.get_width() / 2 - width / 2, game.screen.get_height() / 6 * 3, width, height,
                           color=(255, 0, 0))
        self.three_e.def_text = "Подтверждение пароля"
        self.three_e.set_hides()
        self.three_e.add_wrap(4, color=(157, 151, 151))
        self.sbros(game)
        text = "GEOMASTER"
        self.label = game.font_header.render(text, True, (169, 169, 176))

    def onef(self,game):
        self.sbros(game)
        game.state = Screen.auth

    def twof(self,game):
        if self.two_e.texts == self.three_e.texts and self.one_e.texts != self.one_e.def_text and self.two_e.texts != self.two_e.def_text and self.three_e.texts != self.three_e.def_text and self.one_e.texts != "" and self.two_e.texts != "" and self.three_e.texts != "":
            user = User(self.one_e.texts,id = self.three_e.texts)
            if user.add_user():
                self.sbros(game)
                game.state = Screen.auth
            else:
                Popup.exists()
        else:
            Popup.unequal()

    def draw(self, game):
        if isinstance(game.fon_auth,pg.Rect):
            pg.draw.rect(game.screen, (0, 0, 0), game.fon_auth)
        else:
            game.screen.blit(game.fon_auth,(0,0))
        self.one.draw(game.screen)
        self.two.draw(game.screen)
        self.one_e.draw(game.screen)
        self.two_e.draw(game.screen)
        self.three_e.draw(game.screen)
        label_rect = self.label.get_rect(center=(game.screen.get_width() / 2, game.screen.get_height()  /8 + 25))
        game.screen.blit(self.label, label_rect)

    def sbros(self,game):
        self.one_e.input = False
        self.one_e.texts = self.one_e.def_text
        self.one_e.default = True
        self.one_e.set_text(game.font_static,color=(192,192,192))
        self.two_e.texts = self.two_e.def_text
        self.two_e.default = True
        self.two_e.input = False
        self.two_e.set_text(game.font_static, color=(192,192,192))
        self.three_e.texts = self.three_e.def_text
        self.three_e.input = False
        self.three_e.default = True
        self.three_e.set_text(game.font_static, color=(192,192,192))

    def one_input(self,event,font):
        if self.one_e.input:
            self.two_e.change_input(font)
            self.three_e.change_input(font)
        self.one_e.validate(event,font,spec="+_-–=!@#$$%^&*?|<>",alnum=True)

    def two_input(self,event,font):
        if self.two_e.input:
            self.one_e.change_input(font)
            self.three_e.change_input(font)
        self.two_e.validate(event,font,spec="+_-–=!@#$$%^&*?|<>",alnum=True)

    def three_input(self,event,font):
        if self.three_e.input:
            self.one_e.change_input(font)
            self.two_e.change_input(font)
        self.three_e.validate(event,font,spec="+_-–=!@#$$%^&*?|<>",alnum=True)
