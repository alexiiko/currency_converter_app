import pygame as pg
from settings import *

class ButtonsLeftSide:
    def __init__(self):
        pg.font.init()
        self.select_button = pg.image.load("buttons/select_button.png")
        self.select_button_rect = self.select_button.get_rect(center = (90, 360))

        self.aud_button = pg.transform.scale(pg.image.load("buttons/aud_button.png"), (CURRENY_BUTTON_SIZE, CURRENY_BUTTON_SIZE))
        self.aud_button_rect = self.aud_button.get_rect(center = (53, 255))

        self.cad_button = pg.transform.scale(pg.image.load("buttons/cad_button.png"), (CURRENY_BUTTON_SIZE, CURRENY_BUTTON_SIZE))
        self.cad_button_rect = self.aud_button.get_rect(center = (153, 255))

        self.chf_button = pg.transform.scale(pg.image.load("buttons/chf_button.png"), (CURRENY_BUTTON_SIZE, CURRENY_BUTTON_SIZE))
        self.chf_button_rect = self.aud_button.get_rect(center = (253, 255))

        self.eur_button = pg.transform.scale(pg.image.load("buttons/eur_button.png"), (CURRENY_BUTTON_SIZE, CURRENY_BUTTON_SIZE))
        self.eur_button_rect = self.aud_button.get_rect(center = (53, 155))

        self.gbp_button = pg.transform.scale(pg.image.load("buttons/gbp_button.png"), (CURRENY_BUTTON_SIZE, CURRENY_BUTTON_SIZE))
        self.gbp_button_rect = self.aud_button.get_rect(center = (153, 155))

        self.jpy_button = pg.transform.scale(pg.image.load("buttons/jpy_button.png"), (CURRENY_BUTTON_SIZE, CURRENY_BUTTON_SIZE))
        self.jpy_button_rect = self.aud_button.get_rect(center = (253, 155))

        self.usd_button = pg.transform.scale(pg.image.load("buttons/usd_button.png"), (CURRENY_BUTTON_SIZE, CURRENY_BUTTON_SIZE))
        self.usd_button_rect = self.aud_button.get_rect(center = (153, 55))

        self.clicked = False

        self.show_currencies = False

        self.font = pg.font.Font(None, 32)

        self.current_currency = ""
        self.current_currency_surf = self.font.render(self.current_currency, True, "white")

    def get_currency(self):
        return self.current_currency

    def show_current_currency(self):
        SCREEN.blit(self.current_currency_surf, (170,310))

    def check_click(self):
        x,y = pg.mouse.get_pos()
        
        if self.select_button_rect.collidepoint(x,y):
            if pg.mouse.get_pressed()[0] and self.clicked == False:
                self.clicked = True
                self.show_currencies = True if self.show_currencies == False else False

        if self.aud_button_rect.collidepoint(x,y): 
            if pg.mouse.get_pressed()[0] and self.clicked == False:
                self.clicked = True
                self.show_currencies = False
                self.current_currency = "AUD"

        if self.cad_button_rect.collidepoint(x,y): 
            if pg.mouse.get_pressed()[0] and self.clicked == False:
                self.clicked = True
                self.show_currencies = False
                self.current_currency = "CAD"

        if self.chf_button_rect.collidepoint(x,y): 
            if pg.mouse.get_pressed()[0] and self.clicked == False:
                self.clicked = True
                self.show_currencies = False
                self.current_currency = "CHF"
                

        if self.eur_button_rect.collidepoint(x,y): 
            if pg.mouse.get_pressed()[0] and self.clicked == False:
                self.clicked = True
                self.show_currencies = False
                self.current_currency = "EUR"

        if self.gbp_button_rect.collidepoint(x,y): 
            if pg.mouse.get_pressed()[0] and self.clicked == False:
                self.clicked = True
                self.show_currencies = False
                self.current_currency = "GBP"

        if self.jpy_button_rect.collidepoint(x,y): 
            if pg.mouse.get_pressed()[0] and self.clicked == False:
                self.clicked = True
                self.show_currencies = False
                self.current_currency = "JPY"

        if self.usd_button_rect.collidepoint(x,y): 
            if pg.mouse.get_pressed()[0] and self.clicked == False:
                self.clicked = True
                self.show_currencies = False
                self.current_currency = "USD"

        self.current_currency_surf = self.font.render(self.current_currency, True, "white")
        self.reset_click()

    def reset_click(self):
        if pg.mouse.get_pressed()[0] == False:
            self.clicked = False

    def draw_selecter(self):
        SCREEN.blit(self.select_button, self.select_button_rect)

    def blit_currencies(self):
        if self.show_currencies:
            SCREEN.blit(self.aud_button, self.aud_button_rect)
            SCREEN.blit(self.cad_button, self.cad_button_rect)
            SCREEN.blit(self.chf_button, self.chf_button_rect)
            SCREEN.blit(self.eur_button, self.eur_button_rect)
            SCREEN.blit(self.gbp_button, self.gbp_button_rect)
            SCREEN.blit(self.jpy_button, self.jpy_button_rect)
            SCREEN.blit(self.usd_button, self.usd_button_rect)

    def update(self):
        self.show_current_currency()
        self.blit_currencies()
        self.check_click()
        self.draw_selecter()

buttons_left_side = ButtonsLeftSide()
buttons_left_side.update()