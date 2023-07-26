import pygame as pg
from settings import *

class InputBox:
    def __init__(self):
        pg.font.init()

        self.left_rect = pg.Rect(170, 335, 175, 50)
        self.right_rect = pg.Rect(SCREEN_WIDTH-345, 335, 175, 50)

        self.text = ""
        self.active = False

        self.font = pg.font.Font(None, 32)

    def get_input(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == True and self.left_rect.collidepoint(event.pos):
                self.active = True
            else: 
                self.active = False
        elif event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    return self.text
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
    
    def return_input(self) -> str:
        return self.text
        
    def draw_self(self):
        rect_color = (255,255,255) if self.active else (222,222,222)
        pg.draw.rect(SCREEN, rect_color, self.left_rect, 3)

        text_surf = self.font.render(self.text, True, "white")
        SCREEN.blit(text_surf, (self.left_rect.x + 10, self.left_rect.y + 10))

    def draw_right_rect(self):
        pg.draw.rect(SCREEN, "white", self.right_rect, 3)

    def update(self):
        self.draw_self()
        self.draw_right_rect()

input_box = InputBox()

input_box.update()