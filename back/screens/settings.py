from front.components import Button
from front.components.entry import Entry
from front.components.popup import Popup
from back.models.Screen import Screen


class Settings:
    def __init__(self, game):
        width = game.screen.get_width() / 5
        height = 120
        self.one = Button(game.screen.get_width() / 2 - width / 2, game.screen.get_height() / 5 * 2 + height,
                          width, height,
                          color=(255, 0, 0))
        self.one.add_function(self.onef)
        self.one.set_text(game.font_static, "Вернуться в меню", color=(176, 0, 0))
        self.one.add_wrap(4, color=(157, 151, 151))

        self.three = Button(game.screen.get_width() / 2 - width / 2, game.screen.get_height() / 5 * 3 + height,
                          width, height,
                          color=(255, 0, 0))
        self.three.add_function(self.threef)
        self.three.set_text(game.font_static, "Выйти из аккаунта", color=(176, 0, 0))
        self.three.add_wrap(4, color=(157, 151, 151))

        self.two = Button(game.screen.get_width() / 4 *2, game.screen.get_height() / 5 * 1 + height // 2,
                          width, height,
                          color=(255, 0, 0))
        self.two.add_function(self.twof)
        self.two.set_text(game.font_static, "Сменить пароль", color=(176, 0, 0))
        self.two.add_wrap(4, color=(157, 151, 151))

        width = game.screen.get_width() / 5
        height = game.screen.get_height() / 12

        self.one_e = Entry(game.screen.get_width() / 4, game.screen.get_height() /  5 * 1.5 - height//2, width, height,
                           color=(255, 0, 0))
        self.one_e.def_text = "Старый пароль"
        self.one_e.texts = ""
        self.one_e.set_hides()
        self.two_e = Entry(game.screen.get_width() / 4, game.screen.get_height() / 5* 1.5 + height *1, width, height,
                           color=(255, 0, 0))
        self.one_e.add_wrap(4, color=(157, 151, 151))
        self.two_e.add_wrap(4, color=(157, 151, 151))
        self.two_e.def_text = "Новый пароль"
        self.two_e.texts = ""
        self.two_e.set_hides()

    def threef(self,game):
        game.user = None
        self.sbros(game)
        game.state = Screen.auth

    def onef(self,game):
        game.state = Screen.start

    def twof(self,game):
        if game.user.exists(self.one_e.texts) and self.one_e.texts != "" and self.one_e.texts != self.one_e.def_text:
            if self.two_e.texts != "" and self.two_e.texts != self.two_e.def_text:
                game.user.encode(self.two_e.texts)
                game.user.update()
                self.sbros(game)
                Popup.fine()
            else:
                Popup.add()
        else:
            Popup.wrongpass()

    def draw(self, game):
        self.one.draw(game.screen)
        self.two.draw(game.screen)
        self.one_e.draw(game.screen)
        self.two_e.draw(game.screen)
        self.three.draw(game.screen)

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
