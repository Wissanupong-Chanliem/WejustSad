from typing import TypeAlias
import pygame
from pygame.event import Event
from classes import Page,Resource
from components.text import Text
from function.encrypt_decrypt import add_klong,check_klong

data_in:TypeAlias = dict[
    "is_hard":bool,
]

class WinPage(Page):
    def __init__(self,screen:pygame.Surface,resources:Resource,data:data_in):
        Page.__init__(self,screen,resources)
        self.check = 0
        if not check_klong():
            add_klong()
            self.check = 1
            resources.members.append("klong")
            resources.assets["klong"] = {
                "normal-color":(255,170,0),
                "hard-color":(255,144,0),
                "normal-images":{
                    0 : pygame.image.load("static/images/HappyKlong.webp"),
                    1 : pygame.image.load("static/images/KlongSad-1.webp"),
                    2 : pygame.image.load("static/images/KlongSad-2.webp"),
                    3 : pygame.image.load("static/images/KlongSad-3.webp"),
                    4 : pygame.image.load("static/images/KlongSad-4.webp"),
                    5 : pygame.image.load("static/images/KlongSad-5.webp"),
                    6 : pygame.image.load("static/images/KlongSad-6.webp"),
                    7 : pygame.image.load("static/images/KlongSad-7.webp"),
                    8 : pygame.image.load("static/images/KlongSad-8.webp"),
                    9 : pygame.image.load("static/images/KlongSad-9.webp"),
                },
                "hard-images":{
                    0 : pygame.image.load("static/images/HappyKlong_Hard.webp"),
                    1 : pygame.image.load("static/images/KlongSad_Hard-1.webp"),
                    2 : pygame.image.load("static/images/KlongSad_Hard-2.webp"),
                    3 : pygame.image.load("static/images/KlongSad_Hard-3.webp"),
                    4 : pygame.image.load("static/images/KlongSad_Hard-4.webp"),
                    5 : pygame.image.load("static/images/KlongSad_Hard-5.webp"),
                    6 : pygame.image.load("static/images/KlongSad_Hard-6.webp"),
                    7 : pygame.image.load("static/images/KlongSad_Hard-7.webp"),
                    8 : pygame.image.load("static/images/KlongSad_Hard-8.webp"),
                    9 : pygame.image.load("static/images/KlongSad_Hard-9.webp"),
                }
            }
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
        self.klong_pic = pygame.transform.scale_by(pygame.image.load("static/images/Klong.webp"),0.47)
    def render(self):
        self.back_to_main_menu.render(self.screen_ref)
        self.winning_text.render(self.screen_ref)
        self.screen_ref.blit(self.klong_pic,(330,150))
        self.klong_text.render(self.screen_ref)
        
    def update(self, event: Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.back_to_main_menu.text_rect.collidepoint(pygame.mouse.get_pos()):
                if self.check:
                    self.resources.current_member = len(self.resources.members)-1
                self.redirect_to("MainMenu")