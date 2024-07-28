import pygame as pg


class Window:
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        self.clock = pg.time.Clock()
