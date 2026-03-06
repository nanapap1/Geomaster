import textwrap

from front.components import Button
from front.components.popup import Popup
from back.db import db

from front.components.field import Field
from back.models.Screen import Screen


class Figure:

    def __init__(self,game):
        self.fig = Field(0, 0, game.screen.get_width() * 0.75, game.screen.get_height())
        self.text = None
        self.label = []
        self.label_rect = []
        self.height_b = 40
        num = (game.screen.get_height() / (self.height_b + 15))
        self.one = Button(self.fig.right + 10,(game.screen.get_height() /  (num)) * (num-3), game.screen.get_width() - self.fig.right -20, self.height_b,
                          color=(0, 0, 0))
        self.one.add_function(self.onef)
        self.one.set_text(game.font_static, "Стереть содержимое", color=(0, 0, 0))

        self.two = Button(self.fig.right + 10, (game.screen.get_height() / (num)) * (num - 2),
                          game.screen.get_width() - self.fig.right - 20, self.height_b,
                          color=(0, 0, 0))
        self.two.add_function(self.twof)
        self.two.set_text(game.font_static, "Пропустить задание", color=(0, 0, 0))

        self.three = Button(self.fig.right + 10, (game.screen.get_height() / (num)) * (num - 1),
                          game.screen.get_width() - self.fig.right - 20, self.height_b,
                          color=(0, 0, 0))
        self.three.add_function(self.threef)
        self.three.set_text(game.font_static, "Вернуться в меню", color=(0, 0, 0))

        self.end_label = []
        self.end_label_rect = []


    def get_field(self):
        return self.fig

    def draw(self,game):
        self.fig.draw(game)
        if len(self.label) >0:
            for x in range(0,len(self.label)):
             game.screen.blit(self.label[x], self.label_rect[x])
        self.one.draw(game.screen)
        self.two.draw(game.screen)
        self.three.draw(game.screen)

        if game.user.solved:
            if len(self.end_label) > 0:
                for x in range(0, len(self.end_label)):
                    game.screen.blit(self.end_label[x], self.end_label_rect[x])


    def set_end(self,game):
            if game.user.solved:
                self.two.set_text(game.font_static, "Решать дальше", color=(0, 0, 0))
                self.render_text(game,"Задача решена!")


    def render_text(self,game,text):
        text = textwrap.wrap(text, width=15)
        self.label.clear()
        self.label_rect.clear()
        for x in range(0,len(text)):
                self.label.append(game.font_middle.render(text[x], True, (255, 255, 255)))
                self.label_rect.append(self.label[x].get_rect(center=((game.screen.get_width() - self.fig.right)/2 + self.fig.right, 40 * (x+1))))


    def load_task(self,game):
        self.task = game.user.task
        print(self.task)

        text,resid,endid= db.info_task(self.task)
        self.render_text(game,text)

        func_res,quan,more = db.get_res(resid)
        if more is None:
            more = False
        func = getattr(game.task,func_res)
        res = func(quan,more)
        self.fig.atributtes = res

        func_end,quan = db.get_end(endid)
        func = getattr(game.check,func_end)
        game.check.set(func,quan,res)

    def onef(self,game):
        self.fig.polyline.lines.clear()
        self.fig.polyline.connections.clear()
        end_x = int(self.fig.width/self.fig.cletka) + 1
        end_y = int(self.fig.height/self.fig.cletka) + 1
        if self.fig.width % self.fig.cletka ==0:
            end_x = int(self.fig.width / self.fig.cletka)
        if self.fig.height % self.fig.cletka ==0:
            end_y = int(self.fig.height / self.fig.cletka)
        for x in range(0,end_x-1):
            for y in range(0, end_y-1):
                self.fig.polyline.addPoint(self.fig.polyline.points[x,y])

    def threef(self, game):
        game.state = Screen.start

    def twof(self, game):
       if game.user.solved:
            game.user.update_dif(check=True)
            game.user.get_task()
            self.load_task(game)
            self.onef(game)
            self.two.set_text(game.font_static, "Пропустить задание", color=(0, 0, 0))
       else:
            if Popup.show(game):
                game.user.update_dif(check=False)
                game.user.get_task()
                self.onef(game)
                self.load_task(game)


