from front.components import Button
from front.components.field import Field
import textwrap

from back.models.Screen import Screen


class Know:

    def __init__(self, game):
        self.fig = Field(0, 0, game.screen.get_width() * 0.75, game.screen.get_height())
        self.text = None
        self.label = []
        self.label_rect = []
        self.height_b = 40
        num = (game.screen.get_height() / (self.height_b + 15))
        self.one = Button(self.fig.right + 10, (game.screen.get_height() / (num))* (num-6),
                          game.screen.get_width() - self.fig.right - 20, self.height_b,
                          color=(0, 0, 0))
        self.one.add_function(self.onef)
        self.one.set_text(game.font_static, "Узел", color=(0, 0, 0))
        self.one.add_wrap(4)

        self.two = Button(self.fig.right + 10, (game.screen.get_height() / (num)) * (num-5),
                          game.screen.get_width() - self.fig.right - 20, self.height_b,
                          color=(0, 0, 0))
        self.two.add_function(self.twof)
        self.two.set_text(game.font_static, "Прямая", color=(0, 0, 0))
        self.two.add_wrap(4)

        self.three = Button(self.fig.right + 10, (game.screen.get_height() / (num)) * (num-4),
                            game.screen.get_width() - self.fig.right - 20, self.height_b,
                            color=(0, 0, 0))
        self.three.set_text(game.font_static, "Треугольник", color=(0, 0, 0))
        self.three.add_function(self.threef)
        self.three.add_wrap(4)

        self.four = Button(self.fig.right + 10, (game.screen.get_height() / (num)) * (num-3),
                            game.screen.get_width() - self.fig.right - 20, self.height_b,
                            color=(0, 0, 0))
        self.four.set_text(game.font_static, "Четырехугольник", color=(0, 0, 0))
        self.four.add_function(self.fourf)
        self.four.add_wrap(4)

        self.five = Button(self.fig.right + 10, (game.screen.get_height() / (num)) * (num-2),
                            game.screen.get_width() - self.fig.right - 20, self.height_b,
                            color=(0, 0, 0))
        self.five.set_text(game.font_static, "Пятиугольник", color=(0, 0, 0))
        self.five.add_function(self.fifth)
        self.five.add_wrap(4)

        self.six = Button(self.fig.right + 10, (game.screen.get_height() / (num)) * (num - 1),
                           game.screen.get_width() - self.fig.right - 20, self.height_b,
                           color=(0, 0, 0))
        self.six.add_function(self.sixf)
        self.six.set_text(game.font_static, "Вернутся в меню", color=(0, 0, 0))


    def draw(self,game):
        self.fig.draw(game)
        self.one.draw(game.screen)
        self.two.draw(game.screen)
        self.three.draw(game.screen)
        self.four.draw(game.screen)
        self.five.draw(game.screen)
        self.six.draw(game.screen)

        if len(self.label) >0:
            for x in range(0,len(self.label)):
             game.screen.blit(self.label[x], self.label_rect[x])


    def render_text(self,game,text):
        text = textwrap.wrap(text, width=15)
        self.label.clear()
        self.label_rect.clear()
        for x in range(0,len(text)):
                self.label.append(game.font_middle.render(text[x], True, (255, 255, 255)))
                self.label_rect.append(self.label[x].get_rect(center=((game.screen.get_width() - self.fig.right)/2 + self.fig.right, 40 * (x+1))))


    def clear(self):
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

    def onef(self,game):
        self.clear()
        one, two = self.fig.polyline.points.shape
        self.fig.polyline.addDrawPoint(self.fig.polyline.points[one//2,two//2])
        self.render_text(game, "Точка на сетке")

    def twof(self,game):
        self.clear()
        one, two = self.fig.polyline.points.shape
        self.fig.polyline.addDrawPoint(self.fig.polyline.points[one//2-2,two//2])
        self.fig.polyline.addDrawPoint(self.fig.polyline.points[one // 2 + 2, two // 2])
        print()
        self.fig.polyline.addLine(self.fig.polyline.points[one//2-2, two//2],self.fig.polyline.points[one // 2 + 2, two // 2],self.fig.cletka)
        self.render_text(game, "Прямая с концами в узлах")
    def threef(self,game):
        self.clear()
        one, two = self.fig.polyline.points.shape
        self.fig.polyline.addPoint(self.fig.polyline.points[one//2,two//2-2])
        self.fig.polyline.addPoint(self.fig.polyline.points[one // 2 - 2, two // 2])
        self.fig.polyline.addPoint(self.fig.polyline.points[one // 2 + 2, two // 2])
        self.fig.polyline.addLine(self.fig.polyline.points[one//2-2, two//2],self.fig.polyline.points[one // 2 + 2, two // 2],self.fig.cletka)
        self.fig.polyline.addLine(self.fig.polyline.points[one // 2 - 2, two // 2],
                                  self.fig.polyline.points[one // 2, two // 2-2], self.fig.cletka)
        self.fig.polyline.addLine(self.fig.polyline.points[one // 2 + 2, two // 2],
                                  self.fig.polyline.points[one // 2, two // 2 - 2], self.fig.cletka)
        self.render_text(game, "Треугольник – фигура, соедиянющая три узла")

    def fourf(self,game):
        self.clear()
        one, two = self.fig.polyline.points.shape
        self.fig.polyline.addPoint(self.fig.polyline.points[one//2-1,two//2-2])
        self.fig.polyline.addPoint(self.fig.polyline.points[one // 2 +1, two // 2-2])
        self.fig.polyline.addPoint(self.fig.polyline.points[one // 2 - 2, two // 2])
        self.fig.polyline.addPoint(self.fig.polyline.points[one // 2 + 2, two // 2])
        self.fig.polyline.addLine(self.fig.polyline.points[one//2-2, two//2],self.fig.polyline.points[one // 2 + 2, two // 2],self.fig.cletka)
        self.fig.polyline.addLine(self.fig.polyline.points[one // 2 - 2, two // 2],
                                  self.fig.polyline.points[one // 2-1, two // 2-2], self.fig.cletka)
        self.fig.polyline.addLine(self.fig.polyline.points[one // 2 + 2, two // 2],
                                  self.fig.polyline.points[one // 2+1, two // 2 - 2], self.fig.cletka)
        self.fig.polyline.addLine(self.fig.polyline.points[one // 2 -1, two // 2-2],
                                  self.fig.polyline.points[one // 2+1, two // 2 - 2], self.fig.cletka)
        self.render_text(game, "Четырехугольник – фигура, соедиянющая четыре узла")

    def fifth(self,game):
        self.clear()
        one, two = self.fig.polyline.points.shape
        self.fig.polyline.addPoint(self.fig.polyline.points[one//2-1,two//2-2])
        self.fig.polyline.addPoint(self.fig.polyline.points[one // 2 +1, two // 2-2])
        self.fig.polyline.addPoint(self.fig.polyline.points[one // 2, two // 2-3])
        self.fig.polyline.addPoint(self.fig.polyline.points[one // 2 - 2, two // 2])
        self.fig.polyline.addPoint(self.fig.polyline.points[one // 2 + 2, two // 2])
        self.fig.polyline.addLine(self.fig.polyline.points[one//2-2, two//2],self.fig.polyline.points[one // 2 + 2, two // 2],self.fig.cletka)
        self.fig.polyline.addLine(self.fig.polyline.points[one // 2 - 2, two // 2],
                                  self.fig.polyline.points[one // 2-1, two // 2-2], self.fig.cletka)
        self.fig.polyline.addLine(self.fig.polyline.points[one // 2 + 2, two // 2],
                                  self.fig.polyline.points[one // 2+1, two // 2 - 2], self.fig.cletka)
        self.fig.polyline.addLine(self.fig.polyline.points[one // 2 -1, two // 2-2],
                                  self.fig.polyline.points[one // 2, two // 2 - 3], self.fig.cletka)
        self.fig.polyline.addLine(self.fig.polyline.points[one // 2 + 1, two // 2 - 2],
                                  self.fig.polyline.points[one // 2, two // 2 - 3], self.fig.cletka)
        self.render_text(game, "Пятиугольник – фигура, соедиянющая пять узлов")

    def sixf(self, game):
        game.state = Screen.start


