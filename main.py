import pygame as pg
from sys import exit
from settings import *
from converter import *
from input_box import *
from buttons_left_side import *
from buttons_right_side import *

class App:
    def __init__(self):
        pg.init()
        pg.font.init()

        pg.display.set_caption("Currency Converter")
        
        icon_surf = pg.image.load("icon.png")
        pg.display.set_icon(icon_surf)

        self.clock = pg.time.Clock()

    def draw_window(self):
        SCREEN.fill("#228979")
        buttons_left_side.update()
        buttons_right_side.update()
        converter.update()
        input_box.update()

    def check_for_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            else:
                input_box.get_input(event)

    def update(self):
        self.clock.tick(FPS)
        pg.display.update()

    def run(self):
        while True:
            self.check_for_events()
            self.update()
            self.draw_window()

app = App()
app.run()