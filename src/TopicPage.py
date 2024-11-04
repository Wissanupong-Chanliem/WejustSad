from typing import TypeAlias
import pygame
from pygame.event import Event
from classes import Page,Resource
from components.text import Text
from components.button import Button
from components.topicpage.topic_select import TopicList
from components.topicpage.show_word_list import ShowWordList
from function import random_word
from function.wordlist_folder import open_file_selection,remove_wordlist
from function.read_wordlist_folder import read_user_wordlist_dir
data_in:TypeAlias = dict[
    "is_hard":bool,
]


class TopicPage(Page):
    def __init__(self,screen:pygame.Surface,resources:Resource,data:data_in):
        Page.__init__(self,screen,resources)
        self.data = data
        self.show_word = False
        self.word_list_box = ShowWordList({},resources,self.data["is_hard"],False)
        self.topic_selection = TopicList(read_user_wordlist_dir(),resources,self.data["is_hard"])
        self.title_text = (
            Text(resources.fonts["Kanit-Header-2"],"Classic Mode" if not self.data["is_hard"] else "Hard Mode",self.resources.get_current_color(self.data["is_hard"]))
            .set_coordinate((100,60))
        )
        self.start_button = (
            Button(580,60,self.resources.get_current_color(self.data["is_hard"]),4)
            .add_text(resources.fonts["Kanit-Regular"],"Start!!!",self.resources.colors["white"])
            .set_coordinate((self.screen_ref.get_width()-390,630),origin_center=True)
        )
        self.add_wordlist_button = (
            Button(250,40,self.resources.colors["black"],4,1)
            .set_coordinate((100,620))
            .add_text(resources.fonts["Kanit-Regular"],"Add Word List",self.resources.colors["black"])
        )
        self.remove_wordlist_button = (
            Button(250,40,self.resources.colors["black"],4,1)
            .set_coordinate((100,570))
            .add_text(resources.fonts["Kanit-Regular"],"Remove Word List",self.resources.colors["black"])
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
        self.selected_topic_text = (
            Text(resources.fonts["Kanit-Header-1"],"Select Topic",self.resources.colors["black"])
            .set_coordinate((100,120))
        )
        

    def render(self):
        self.title_text.render(self.screen_ref)
        self.start_button.render(self.screen_ref)
        self.topic_selection.render(self.screen_ref)
        self.add_wordlist_button.render(self.screen_ref)
        self.remove_wordlist_button.render(self.screen_ref)
        self.back_to_main_menu.render(self.screen_ref)
        self.word.render(self.screen_ref)
        self.show_word_list.render(self.screen_ref)
        self.selected_topic_text.render(self.screen_ref)
        if self.show_word == True:
            pygame.draw.rect(self.screen_ref,self.resources.get_current_color(self.data["is_hard"]), pygame.Rect(810, 87, 25, 25), 0, 6)
            pygame.draw.rect(self.screen_ref,(0,0,0), pygame.Rect(810, 87, 25, 25), 2, 6)
        else:
            pygame.draw.rect(self.screen_ref,(0,0,0), pygame.Rect(810, 87, 25, 25), 2, 6)
        self.word_list_box.render(self.screen_ref)

    def update(self, event: Event):
        mouse_pos = pygame.mouse.get_pos()
        self.topic_selection.update(event)
        self.word_list_box.update(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.Rect(810,87,25,25).collidepoint(mouse_pos):
                if self.show_word == False:
                    self.show_word = True
                else:
                    self.show_word = False
                self.word_list_box.__init__(self.topic_selection.get_selected(),self.resources,self.data["is_hard"],self.show_word)
            
            if self.start_button.button_rect.collidepoint(mouse_pos):
                select = self.topic_selection.get_selected()
                is_builtin = self.topic_selection.is_builtin()
                if select:
                    word_list = list(random_word.random_word(select).items())
                    data = {"wordlist":word_list,"current_word":0,"is_hard":self.data["is_hard"],"current_sad":0,"is_builtin":is_builtin}
                    self.redirect_with_data("HangMan",data)

            if self.back_to_main_menu.text_rect.collidepoint(mouse_pos):
                self.redirect_to("MainMenu")

            if self.add_wordlist_button.button_rect.collidepoint(mouse_pos):
                open_file_selection()
                self.topic_selection.update_list(read_user_wordlist_dir())

            if self.remove_wordlist_button.button_rect.collidepoint(mouse_pos):
                path = self.topic_selection.get_selected_path()
                if path:
                    remove_wordlist(path)
                    self.topic_selection.update_list(read_user_wordlist_dir())

        if self.topic_selection.has_changed():
            self.word_list_box.__init__(self.topic_selection.get_selected(),self.resources,self.data["is_hard"],self.show_word)
        
        