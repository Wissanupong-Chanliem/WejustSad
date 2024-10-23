import pygame
from pygame.event import Event
from classes import Page,Resource
from components.text import Text
from components.button import Button
from components.topicpage.topic_select import TopicList
from function.read_word_list import read_word_list
from function.read_wordlist_folder import read_wordlist_dir


class TopicPage(Page):
    def __init__(self,screen:pygame.Surface,resources):
        Page.__init__(self,screen,resources)
        self.title_text = (
            Text(resources.fonts["Kanit-Header-2"],"Classic Mode",self.resources.colors["pupe-cyan"])
            .set_coordinate((100,60))
        )
        self.start_button = (
            Button(200,80,self.resources.colors["pupe-cyan"],4)
            .add_text(resources.fonts["Kanit-Header"],"Start!!!",self.resources.colors["black"])
            .set_coordinate((self.screen_ref.get_width()-200,600),origin_center=True)
        )
        self.topic_selection = TopicList(read_wordlist_dir(),resources)
        self.add_wordlist_button = (
            Button(400,80,self.resources.colors["black"],4,1)
            .set_coordinate((300,600),origin_center=True)
            .add_text(resources.fonts["Kanit-Regular"],"Add Word List",self.resources.colors["black"])
        )
        self.back_to_main_menu = (
            Text(resources.fonts["Kanit-Regular"],"< Main Menu",self.resources.colors["black"])
            .set_coordinate((100,40))
        )
        self.word = (
            Text(resources.fonts["Kanit-Regular"],"Word",self.resources.colors["black"])
            .set_coordinate((530,85))
        )
        self.box_chack = (
            
        )


    def render(self):
        self.title_text.render(self.screen_ref)
        self.start_button.render(self.screen_ref)
        self.topic_selection.render(self.screen_ref)
        self.add_wordlist_button.render(self.screen_ref)
        self.back_to_main_menu.render(self.screen_ref)
        self.word.render(self.screen_ref)
        pygame.draw.rect(self.screen_ref,(73,179,255), pygame.Rect(520, 120, 480, 400), 2, 10)

    def update(self, event: Event):
        mouse_pos = pygame.mouse.get_pos()
        self.topic_selection.update(event)
        #print(event,self.topic_selection.get_selected())
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Classic Mode button is clicked
            if self.start_button.button_rect.collidepoint(mouse_pos):
                if self.topic_selection.get_selected():
                    self.redirect_with_data("HangMan",read_word_list(f"static/wordlist/{self.topic_selection.get_selected()}.txt"))
            if self.back_to_main_menu.text_rect.collidepoint(mouse_pos):
                self.redirect_to("MainMenu")
        
        