import os
import pygame as pg


class FontLoading():

    @staticmethod
    def load_font_headers():
        try:
            fullname = os.path.join("/Users/markmoskvitin/Desktop/учеба/курсовая/3 семак/код/front/resourcers/fon2.ttf")
            font = pg.font.Font(fullname, 90)
        except:
            font = pg.font.Font(None, 60)
        return font

    @staticmethod
    def load_font_middle():
        try:
            fullname = os.path.join("/Users/markmoskvitin/Desktop/учеба/курсовая/3 семак/код/front/resourcers/fon2.ttf")
            font = pg.font.Font(fullname, 30)
        except:
            font = pg.font.Font(None, 40)
        return font


    @staticmethod
    def load_font_standart():
        try:
            fullname = os.path.join("/Users/markmoskvitin/Desktop/учеба/курсовая/3 семак/код/front/resourcers/fon2.ttf")
            font = pg.font.Font(fullname, 20)
        except:
            font = pg.font.Font(None, 20)
        return font
