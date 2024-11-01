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
        self.arrow_left = pygame.draw.polygon(self.screen_ref, resources.colors["pupe-cyan"], ((350,230),(300,260),(350,290)))
        self.arrow_right = pygame.draw.polygon(self.screen_ref, resources.colors["pupe-cyan"], ((750,230),(800,260),(750,290)))
        self.sad_pic = pygame.transform.scale_by((self.resources.assets[self.resources.members[self.resources.current_member]]["normal-images"][8]),0.30)
    def render(self):
        self.title_text.render(self.screen_ref)
        self.screen_ref.blit(self.sad_pic,(self.screen_ref.get_rect().centerx-self.sad_pic.get_rect().centerx + 20,100))
        self.arrow_left = pygame.draw.polygon(self.screen_ref, self.resources.colors["pupe-cyan"], ((350,230),(300,260),(350,290)))
        self.arrow_right = pygame.draw.polygon(self.screen_ref, self.resources.colors["pupe-cyan"],  ((750,230),(800,260),(750,290)))
        self.classic_button.render(self.screen_ref)
        self.hard_button.render(self.screen_ref)
    
    def update(self, event:Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.classic_button.button_rect.collidepoint(pygame.mouse.get_pos()):
                self.redirect_to("Topic")
            if self.hard_button.button_rect.collidepoint(pygame.mouse.get_pos()):
                self.redirect_to("HardTopic")
            if self.arrow_right.collidepoint(pygame.mouse.get_pos()):
                self.resources.current_member+=1
                if self.resources.current_member > 3:
                    self.resources.current_member = 0
                #print(self.resources.current_member)
                self.sad_pic = pygame.transform.scale_by((self.resources.assets[self.resources.members[self.resources.current_member]]["normal-images"][8]),0.30)
                