import pygame
import pygame as pg
import os

class ImageLoading:

    @staticmethod
    def load_fon_auth(game):
        try:
            fullname = os.path.join("/Users/markmoskvitin/Desktop/учеба/курсовая/3 семак/код/front/resourcers/auth.png")
            img = pygame.image.load(fullname)
            img = pg.transform.scale(img, (game.screen.get_width(), game.screen.get_height()))
        except:
            img = pg.Rect(0,0,game.screen.get_width(),game.screen.get_height())
        return img

    @staticmethod
    def load_fon_logo(game):
        try:
            fullname = os.path.join("/Users/markmoskvitin/Desktop/учеба/курсовая/3 семак/код/front/resourcers/auth.png")
            img = pg.image.load(fullname).convert_alpha()
            width = img.get_width()
            img = pg.transform.scale(img,(img.get_width()//2,img.get_height()//2))
        except:
            try:
                fullname = os.path.join("/Users/markmoskvitin/Desktop/учеба/курсовая/3 семак/код/front/resourcers/auth.png")
                width =0
                img = pg.font.Font(fullname, 80)
            except:
                img = pg.font.Font(None, 80)
        return img,width