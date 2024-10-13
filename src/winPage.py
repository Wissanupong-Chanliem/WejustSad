import pygame
from pygame.event import Event
from classes import Page,Resource
from components.text import Text
from components.button import Button

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
BLACK = (0,0,0)
PUPE_CYAN = (73,179,255)

class winPage(Page):
    def __init__(self,screen:pygame.Surface,resources:Resource):
        Page.__init__(self,screen,resources)
        self.back_to_main_menu = (
            Text(resources.fonts["Kanit-Regular"],"< Main Menu",BLACK)
            .set_coordinate((100,40))
        )
        self.winning_text = (
            Text(resources.fonts["Kanit-Word"],"ชนะแล้วหรอฮะ?",PUPE_CYAN)
            .set_coordinate((self.screen_ref.get_rect().centerx,90),origin_center=True)
        )
        self.klong_text = (
            Text(resources.fonts["Kanit-Klong"],"เป็นไปได้ยังไงกันฮะ!!",PUPE_CYAN)
            .set_coordinate((self.screen_ref.get_rect().centerx,self.screen_ref.get_height()-100),origin_center=True)
        )

    def render(self):
        self.back_to_main_menu.render(self.screen_ref)
        self.winning_text.render(self.screen_ref)
        self.screen_ref.blit(pygame.transform.scale_by((self.resources.images["klong"]),0.47),(330,150))
        self.klong_text.render(self.screen_ref)
        
    def update(self, event: Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Classic Mode button is clicked
            if self.back_to_main_menu.text_rect.collidepoint(pygame.mouse.get_pos()):
                self.redirect_to("MainMenu")
