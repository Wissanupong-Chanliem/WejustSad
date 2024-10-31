import pygame
from pygame.event import Event
from classes import Page,Resource
from components.text import Text
from components.button import Button

class MainMenuPage(Page):
    def __init__(self,screen:pygame.Surface,resources:Resource):
        Page.__init__(self,screen,resources)
        screen_rect = self.screen_ref.get_rect()
        self.classic_button = (
            Button(200,80,resources.colors["pupe-cyan"],4)
            .add_text(resources.fonts["Kanit-Header"],"Classic",self.resources.colors["white"])
            .set_coordinate((screen_rect.centerx,530),origin_center = True)
        )
        self.hard_button = (
            Button(200,80,(133,113,255),4)
            .add_text(resources.fonts["Kanit-Header"],"Hard",self.resources.colors["white"])
            .set_coordinate((screen_rect.centerx,630),origin_center = True)
        )
        self.title_text = (
            Text(resources.fonts["Kanit-Title"],"{v}JustSad ;-;",resources.colors["pupe-cyan"])
            .set_coordinate((screen_rect.centerx,50),origin_center = True)
        )
    def render(self):
        self.title_text.render(self.screen_ref)
        self.screen_ref.blit(
            self.resources.images["pupe-sad"],
            (
                self.screen_ref.get_rect().centerx - self.resources.images["pupe-sad"].get_rect().centerx,
                100
            ),
        )
        self.classic_button.render(self.screen_ref)
        self.hard_button.render(self.screen_ref)
    
    def update(self, event:Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.classic_button.button_rect.collidepoint(pygame.mouse.get_pos()):
                self.redirect_to("Topic")
            if self.hard_button.button_rect.collidepoint(pygame.mouse.get_pos()):
                self.redirect_to("HardTopic")