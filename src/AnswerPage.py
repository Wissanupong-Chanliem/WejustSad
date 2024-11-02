import pygame
from pygame.event import Event
from classes import Page,Resource
from components.text import Text
from components.button import Button
from typing import TypeAlias

data_in:TypeAlias = dict[
    "score":int,
    "word":str,
    "current_wordlist":list[(str,str)],
    "is_hard":bool
]
class AnswerPage(Page):
    def __init__(self,screen:pygame.Surface,resources:Resource,data:data_in):
        Page.__init__(self,screen,resources)
        self.data = data
        self.title_text = (
            Text(resources.fonts["Kanit-Word"],"ถูกต้องง!",self.resources.get_current_color(self.data["is_hard"]))
            .set_coordinate((self.screen_ref.get_rect().centerx,70),origin_center = True)
        )
        self.next_button = (
            Button(300,80,self.resources.get_current_color(self.data["is_hard"]),4)
            .add_text(resources.fonts["Kanit-Header"],"Next",self.resources.colors["white"])
            .set_coordinate((self.screen_ref.get_width()-200,640),origin_center=True)
        )
        self.score = (
            Text(resources.fonts["Kanit-Word"],f"Score : {data["score"]}",self.resources.get_current_color(self.data["is_hard"]))
            .set_coordinate((50,self.screen_ref.get_height()-120))
        )
        self.word = (
            Text(resources.fonts["Kanit-Word"],f"{data["word"][0]}",self.resources.get_current_color(self.data["is_hard"]))
            .set_coordinate((self.screen_ref.get_rect().centerx,470),origin_center = True)
        )
        self.meaning = (
            Text(resources.fonts["Kanit-Word"],f"{data["word"][1]}",self.resources.get_current_color(self.data["is_hard"]))
            .set_coordinate((self.screen_ref.get_rect().centerx,545),origin_center = True)
        )
        scale_factor = 0.3
        if self.resources.members[self.resources.current_member] in ("akita","gnome"):
            scale_factor = 0.25
        self.happy_pic = pygame.transform.scale_by(self.resources.get_current_sprite(self.data["is_hard"])[0],scale_factor)
    def render(self):
        self.screen_ref.blit(
            self.happy_pic,
            (
                self.screen_ref.get_rect().centerx - self.happy_pic.get_rect().centerx,
                100
            ),
        )
        self.title_text.render(self.screen_ref)
        self.next_button.render(self.screen_ref)
        self.score.render(self.screen_ref)
        self.word.render(self.screen_ref)
        self.meaning.render(self.screen_ref)
        
    def update(self, event: Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.next_button.button_rect.collidepoint(pygame.mouse.get_pos()):
                if self.data["score"] >= len(self.data["current_wordlist"]):
                    self.redirect_with_data("WinPage",{"is_hard":self.data["is_hard"]})
                else:
                    self.redirect_with_data("HangMan",{"current_word":self.data["score"],"wordlist":self.data["current_wordlist"],"is_hard":self.is_hard})
                