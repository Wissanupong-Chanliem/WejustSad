import pygame
from pygame.event import Event
from classes import Page,Resource
from components.text import Text
from components.button import Button

class HangManPage(Page):
    def __init__(self,screen:pygame.Surface,resources):
        Page.__init__(self,screen,resources)
        self.title_text = (
            Text(resources.fonts["Kanit-Word"],"Hang Man",self.resources.colors["pupe-cyan"])
            .set_coordinate((self.screen_ref.get_rect().centerx,70),origin_center = True)
        )
        self.menu_button = (
            Button(250,80,self.resources.colors["pupe-cyan"],4)
            .add_text(resources.fonts["Kanit-Header"],"Confirm",self.resources.colors["black"])
            .set_coordinate((self.screen_ref.get_width()-200,600),origin_center=True)
        )
        self.score = (
            Text(resources.fonts["Kanit-Bold-Regular-Size"],"Score",self.resources.colors["pupe-cyan"])
            .set_coordinate((self.screen_ref.get_width()-150,20))
        )
        self.kanan_num = 0
        self.kanan = (
            Text(resources.fonts["Kanit-Bold-Regular-Size"],str(self.kanan_num),self.resources.colors["pupe-cyan"])
            .set_coordinate((self.screen_ref.get_width()-111,70))
        )
        self.current_key = "Y"
        self.guessing = (
            Text(resources.fonts["Kanit-Bold-Regular-Size"],"Guessing",self.resources.colors["pupe-cyan"])
            .set_coordinate((self.screen_ref.get_width()-200,440),origin_center=True)
        )
        self.guess =(
            Text(resources.fonts["Kanit-Title"],"\""+self.current_key+"\"",self.resources.colors["pupe-cyan"])
            .set_coordinate((self.screen_ref.get_width()-200,500),origin_center=True)
        )
    def render(self):
        self.title_text.render(self.screen_ref)
        self.menu_button.render(self.screen_ref)
        self.score.render(self.screen_ref)
        self.kanan.render(self.screen_ref)
        self.guessing.render(self.screen_ref)
        self.guess.render(self.screen_ref)
    def update(self, event: Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Confirm now is go to GameOverPage
            # MenuBotton is ConfirmButton
            if self.menu_button.button_rect.collidepoint(pygame.mouse.get_pos()):
                self.redirect_to("GameOver")
        if event.type == pygame.KEYDOWN:
            # Get input from keyboard
            if event.unicode.isalpha():
                self.current_key = event.unicode
                self.guess.update_text("\""+self.current_key+"\"").set_coordinate((self.screen_ref.get_width()-200,500),origin_center=True)
                print(f"Current key: {self.current_key}")
