import pygame
from pygame.event import Event
from classes import Page,Resource
from components.text import Text
from components.button import Button
from components.topicpage.topic_select import TopicList
from function.read_word_list import read_word_list
from function.read_wordlist_folder import read_wordlist_dir

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
BLACK = (0,0,0)
PUPE_CYAN = (73,179,255)

class TopicPage(Page):
    def __init__(self,screen:pygame.Surface,resources):
        Page.__init__(self,screen,resources)
        self.title_text = (
            Text(resources.fonts["Kanit-Header-2"],"Classic Mode",PUPE_CYAN)
            .set_coordinate((100,60))
        )
        self.start_button = (
            Button(200,80,PUPE_CYAN,4)
            .add_text(resources.fonts["Kanit-Header"],"Start!!!",BLACK)
            .set_coordinate((self.screen_ref.get_width()-200,600),origin_center=True)
        )
        self.topic_selection = TopicList(read_wordlist_dir(),resources)
        self.add_wordlist_button = (
            Button(400,80,BLACK,4,1)
            .set_coordinate((300,600),origin_center=True)
            .add_text(resources.fonts["Kanit-Regular"],"Add Word List",BLACK)
        )
        self.back_to_main_menu = (
            Text(resources.fonts["Kanit-Regular"],"< Main Menu",BLACK)
            .set_coordinate((100,40))
        )


    def render(self):
        self.title_text.render(self.screen_ref)
        self.start_button.render(self.screen_ref)
        self.topic_selection.render(self.screen_ref)
        self.add_wordlist_button.render(self.screen_ref)
        self.back_to_main_menu.render(self.screen_ref)
        
    def update(self, event: Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Classic Mode button is clicked
            if self.start_button.button_rect.collidepoint(pygame.mouse.get_pos()):
                self.redirect_to("HangMan")
            if self.back_to_main_menu.text_rect.collidepoint(pygame.mouse.get_pos()):
                self.redirect_to("MainMenu")