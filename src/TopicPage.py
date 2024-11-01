import pygame
from pygame.event import Event
from classes import Page,Resource
from components.text import Text
from components.button import Button
from components.topicpage.topic_select import TopicList
from function import random_word
from function.read_word_list import read_word_list
from function.read_wordlist_folder import read_wordlist_dir


class TopicPage(Page):
    def __init__(self,screen:pygame.Surface,resources:Resource):
        Page.__init__(self,screen,resources)
        self.title_text = (
            Text(resources.fonts["Kanit-Header-2"],"Classic Mode",self.resources.assets[self.resources.members[self.resources.current_member]]["normal-color"])
            .set_coordinate((100,60))
        )
        self.start_button = (
            Button(580,40,self.resources.assets[self.resources.members[self.resources.current_member]]["normal-color"],4)
            .add_text(resources.fonts["Kanit-Regular"],"Start!!!",self.resources.colors["white"])
            .set_coordinate((self.screen_ref.get_width()-390,620),origin_center=True)
        )
        self.topic_selection = TopicList(read_wordlist_dir(),resources)
        self.add_wordlist_button = (
            Button(250,40,self.resources.colors["black"],4,1)
            .set_coordinate((100,600))
            .add_text(resources.fonts["Kanit-Regular"],"Add Word List",self.resources.colors["black"])
        )
        self.back_to_main_menu = (
            Text(resources.fonts["Kanit-Regular"],"< Main Menu",self.resources.colors["black"])
            .set_coordinate((100,40))
        )
        self.word = (
            Text(resources.fonts["Kanit-Regular"],"Word",self.resources.colors["black"])
            .set_coordinate((400,85))
        )
        self.show_word_list = (
            Text(resources.fonts["Kanit-Regular"],"Show Word List",self.resources.colors["black"])
            .set_coordinate((840,85))
        )
        self.box_chack = (
            pygame.transform.scale_by((self.resources.images["unchack"]),0.02)
        )
        self.selected_topic_text = (
            Text(resources.fonts["Kanit-Header-1"],"Select Topic",self.resources.colors["black"])
            .set_coordinate((100,120))
        )
        self.box_rect = pygame.Rect(
            810,87,*self.box_chack.get_size()
        )
        self.show_word = False

    def render(self):
        self.title_text.render(self.screen_ref)
        self.start_button.render(self.screen_ref)
        self.topic_selection.render(self.screen_ref)
        self.add_wordlist_button.render(self.screen_ref)
        self.back_to_main_menu.render(self.screen_ref)
        self.word.render(self.screen_ref)
        self.show_word_list.render(self.screen_ref)
        self.selected_topic_text.render(self.screen_ref)
        if self.show_word == True:
            pygame.draw.rect(self.screen_ref,self.resources.assets[self.resources.members[self.resources.current_member]]["normal-color"], pygame.Rect(810, 87, 25, 25), 0, 6)
            pygame.draw.rect(self.screen_ref,(0,0,0), pygame.Rect(810, 87, 25, 25), 2, 6)
        else:
            pygame.draw.rect(self.screen_ref,(0,0,0), pygame.Rect(810, 87, 25, 25), 2, 6)
        pygame.draw.rect(self.screen_ref,self.resources.assets[self.resources.members[self.resources.current_member]]["normal-color"], pygame.Rect(400, 140, 580, 400), 2, 10)

    def update(self, event: Event):
        mouse_pos = pygame.mouse.get_pos()
        self.topic_selection.update(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.box_rect.collidepoint(mouse_pos):
                if self.show_word == False:
                    self.show_word = True
                else:
                    self.show_word = False
            if self.start_button.button_rect.collidepoint(mouse_pos):
                if self.topic_selection.get_selected():
                    word_list = list(random_word.random_word(read_word_list(f"static/wordlist/{self.topic_selection.get_selected()}.txt")).items())
                    data = {"wordlist":word_list,"current_word":0}
                    self.redirect_with_data("HangMan",data)
            if self.back_to_main_menu.text_rect.collidepoint(mouse_pos):
                self.redirect_to("MainMenu")
        
        