import pygame
import pygame as pg

from back.geometry.check import Check
from back.geometry import Task
from back.handler import FigureHandler
from front.loading.FontLoading import FontLoading
from front.loading.ImageLoading import ImageLoading
from back.models.Screen import Screen
from back.screens.auth import Auth
from back.screens.know import Know
from back.screens.reg import Reg
from back.screens.settings import Settings
from back.screens.start import Start
from back.screens.figure import Figure
from back.db import db

class Game:
    def __init__(self,width,height):
        pg.init()
        self.screen = pg.display.set_mode((width, height))
        self.width = width
        self.height = height
        self.clock = pg.time.Clock()
        self.running = True
        self.user = None
        self.state = Screen.auth

    def start(self):
        self.resource()
        while self.running:
            event_r = None
            for event in pg.event.get():
                if event.type == pygame.QUIT:
                    self.state = Screen.end
                if event.type == pygame.KEYDOWN or event.type == pg.KEYUP:
                    event_r = event
            pressed = pg.key.get_pressed()
            current_pos = pg.mouse.get_pos()
            current_press = pg.mouse.get_pressed()
            if self.state == Screen.graphs:
                    self.state = Screen.graphs
            elif self.state == Screen.know:
                self.know.one.isClicked(*current_pos, self, current_press)
                self.know.two.isClicked(*current_pos, self, current_press)
                self.know.three.isClicked(*current_pos, self, current_press)
                self.know.four.isClicked(*current_pos, self, current_press)
                self.know.five.isClicked(*current_pos, self, current_press)
                self.know.six.isClicked(*current_pos, self, current_press)
            elif self.state == Screen.start:
                self.start.one.isClicked(*current_pos, self, current_press)
                self.start.two.isClicked(*current_pos, self, current_press)
                self.start.three.isClicked(*current_pos, self, current_press)
            elif self.state == Screen.set:
                self.set.one.isClicked(*current_pos, self, current_press)
                self.set.two.isClicked(*current_pos, self, current_press)
                self.set.three.isClicked(*current_pos, self, current_press)
                self.set.one_e.isClicked(*current_pos, self, current_press)
                self.set.one_input(event_r, self.font_static)
                self.set.two_e.isClicked(*current_pos, self, current_press)
                self.set.two_input(event_r, self.font_static)
            elif self.state == Screen.auth:
                self.auth.one.isClicked(*current_pos, self, current_press)
                self.auth.two.isClicked(*current_pos, self, current_press)
                self.auth.one_e.isClicked(*current_pos, self, current_press)
                self.auth.one_input(event_r,self.font_static)

                self.auth.two_e.isClicked(*current_pos, self, current_press)
                self.auth.two_input(event_r, self.font_static)
            elif self.state == Screen.register:
                self.reg.one.isClicked(*current_pos, self, current_press)
                self.reg.two.isClicked(*current_pos, self, current_press)

                self.reg.one_e.isClicked(*current_pos, self, current_press)
                self.reg.one_input(event_r, self.font_static)

                self.reg.two_e.isClicked(*current_pos, self, current_press)
                self.reg.two_input(event_r, self.font_static)

                self.reg.three_e.isClicked(*current_pos, self, current_press)
                self.reg.three_input(event_r, self.font_static)
            elif self.state == Screen.figure:
                    self.fig.one.isClicked(*current_pos, self, current_press)
                    self.fig.two.isClicked(*current_pos, self, current_press)
                    self.fig.three.isClicked(*current_pos, self, current_press)
                    self.figureh.hander(pressed,current_pos,current_press,self)
                    if self.check.apply():
                        self.user.solved = True
                        self.fig.set_end(self)
            if self.draw():
                    pg.display.flip()
                    self.clock.tick(60)


    def draw(self):
        self.screen.fill((192, 111, 93))
        if self.state == Screen.figure:
            self.fig.draw(self)
        elif self.state == Screen.start:
            self.start.draw(self)
        elif self.state == Screen.auth:
            self.auth.draw(self)
        elif self.state == Screen.register:
            self.reg.draw(self)
        elif self.state == Screen.know:
            self.know.draw(self)
        elif self.state == Screen.set:
            self.set.draw(self)
        elif self.state == Screen.end:
            self.running = False
            pygame.quit()
            return False
        return True

    def resource(self):
        self.font_header = FontLoading.load_font_headers()
        self.font_static = FontLoading.load_font_standart()
        self.font_middle = FontLoading.load_font_middle()
        self.fon_auth = ImageLoading.load_fon_auth(self)
        self.fon_long,self.l_width = ImageLoading.load_fon_logo(self)
        self.start = Start(self)
        self.fig = Figure(self)
        self.auth = Auth(self)
        self.reg = Reg(self)
        self.task = Task(self)
        self.check = Check(self)
        self.know = Know(self)
        self.figureh = FigureHandler(self.fig)
        self.set = Settings(self)


    def end(self):
        db.update_task(self.user.login,self.user.task)
        db.close()
        pg.quit()
