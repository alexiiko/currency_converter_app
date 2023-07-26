import requests
import pygame as pg
from settings import *
from api_key import api_key
from input_box import *
from buttons_right_side import *
from buttons_left_side import *

api_key = api_key

class Converter:
    def __init__(self) -> None:
        pg.font.init()
        self.font = pg.font.Font(None, 32)

        self.convert_button = pg.image.load("buttons/convert_button.png")
        self.convert_button_rect = self.convert_button.get_rect(center = (340, 465))

        self.clicked = False

        self.error_info = ""
        self.error_text = "Try with number/currency."
        self.error_text_surf = self.font.render(self.error_text, True, "white")

        self.new_amount = 0.0
        self.new_amount_surf = self.font.render(str(self.new_amount), True, "white")
        self.show_new_amount = False

        self.show_error = False

    def make_request(self):
        self.old_amount = input_box.return_input()
        self.old_currency = buttons_left_side.get_currency()
        self.new_currency = buttons_right_side.get_currency()

        api_url = f'https://api.api-ninjas.com/v1/convertcurrency?want={self.new_currency}&have={self.old_currency}&amount={self.old_amount}'
        response = requests.get(api_url, headers={'X-Api-Key': f'{api_key}'})
        data = response.json()

        if response.status_code == requests.codes.ok:
            self.show_error = False
            self.new_amount = data["new_amount"]
            self.new_amount_surf = self.font.render(str(self.new_amount), True, "white")
            self.show_new_amount = True
        else:
            self.error_info = f"Error: {str(response.status_code)}"
            self.error_info_surf = self.font.render(self.error_info, True, "white")

            self.show_new_amount = False
            self.show_error = True

    def blit_new_amount(self):
        if self.show_new_amount:
            SCREEN.blit(self.new_amount_surf, (365,345))

    def show_error_message(self):
        if self.show_error == True:
            SCREEN.blit(self.error_info_surf, (420, 430))
            SCREEN.blit(self.error_text_surf, (420, 475))

    def check_click(self):
        x,y = pg.mouse.get_pos()

        if self.convert_button_rect.collidepoint(x,y):
            if pg.mouse.get_pressed()[0] and self.clicked == False:
                self.clicked = True
                self.make_request()

        self.reset_click()
    
    def reset_click(self):
        if pg.mouse.get_pressed()[0] == False:
            self.clicked = False

    def draw_self(self):
        SCREEN.blit(self.convert_button, self.convert_button_rect)

    def update(self):
        self.blit_new_amount()
        self.show_error_message()
        self.draw_self()
        self.check_click()

converter = Converter()
converter.update()