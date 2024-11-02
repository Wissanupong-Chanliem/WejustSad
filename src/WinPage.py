from typing import TypeAlias
import pygame
from pygame.event import Event
from classes import Page,Resource
from components.text import Text

data_in:TypeAlias = dict[
    "is_hard":bool,
]

class WinPage(Page):
    def __init__(self,screen:pygame.Surface,resources:Resource,data:data_in):
        Page.__init__(self,screen,resources)
        self.back_to_main_menu = (
            Text(resources.fonts["Kanit-Regular"],"< Main Menu",self.resources.colors["black"])
            .set_coordinate((100,40))
        )
        self.winning_text = (
            Text(resources.fonts["Kanit-Word"],"ชนะแล้วหรอฮะ?",self.resources.get_current_color(data["is_hard"]))
            .set_coordinate((self.screen_ref.get_rect().centerx,90),origin_center=True)
        )
        self.klong_text = (
            Text(resources.fonts["Kanit-Klong"],"เป็นไปได้ยังไงกันฮะ!!",self.resources.get_current_color(data["is_hard"]))
            .set_coordinate((self.screen_ref.get_rect().centerx,self.screen_ref.get_height()-100),origin_center=True)
        )
        self.klong_pic = pygame.transform.scale_by(pygame.image.load("static/images/Klong.jpg"),0.47)
    def render(self):
        self.back_to_main_menu.render(self.screen_ref)
        self.winning_text.render(self.screen_ref)
        self.screen_ref.blit(self.klong_pic,(330,150))
        self.klong_text.render(self.screen_ref)
        
    def update(self, event: Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.back_to_main_menu.text_rect.collidepoint(pygame.mouse.get_pos()):
                self.redirect_to("MainMenu")