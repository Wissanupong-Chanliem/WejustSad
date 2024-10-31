import pygame
from pygame.event import Event
from classes import Page,Resource
from components.text import Text
from components.button import Button
class GameOverPage(Page):
    def __init__(self,screen:pygame.Surface,resources:Resource,data):
        Page.__init__(self,screen,resources)
        self.title_text = (
            Text(resources.fonts["Kanit-Word"],"GAME OVER",self.resources.colors["pupe-cyan"])
            .set_coordinate((self.screen_ref.get_rect().centerx,70),origin_center = True)
        )
        self.menu_button = (
            Button(300,80,self.resources.colors["pupe-cyan"],4)
            .add_text(resources.fonts["Kanit-Header"],"Back to Main Menu",self.resources.colors["black"])
            .set_coordinate((self.screen_ref.get_width()-200,640),origin_center=True)
        )
        self.score = (
            Text(resources.fonts["Kanit-Word"],f"Score : {data["score"]}",self.resources.colors["pupe-cyan"])
            .set_coordinate((50,self.screen_ref.get_height()-120))
        )
        self.word = (
            Text(resources.fonts["Kanit-Word"],f"{data["word"][0]}",self.resources.colors["pupe-cyan"])
            .set_coordinate((self.screen_ref.get_rect().centerx,470),origin_center = True)
        )
        self.meaning = (
            Text(resources.fonts["Kanit-Word"],f"{data["word"][1]}",self.resources.colors["pupe-cyan"])
            .set_coordinate((self.screen_ref.get_rect().centerx,545),origin_center = True)
        )

    def render(self):
        sad_pic = pygame.transform.scale_by(self.resources.images["pupe-sad-8"],0.3)
        self.screen_ref.blit(
            sad_pic,
            (
                self.screen_ref.get_rect().centerx - sad_pic.get_rect().centerx,
                100
            ),
        )
        self.title_text.render(self.screen_ref)
        self.menu_button.render(self.screen_ref)
        self.score.render(self.screen_ref)
        self.word.render(self.screen_ref)
        self.meaning.render(self.screen_ref)
        
    def update(self, event: Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.menu_button.button_rect.collidepoint(pygame.mouse.get_pos()):
                self.redirect_to("MainMenu")