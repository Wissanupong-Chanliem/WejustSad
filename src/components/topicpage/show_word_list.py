import pygame
import pygame.draw_py

from components.text import Text
from function.read_word_list import read_word_list
from ..button import Button
from classes import Resource
from pygame.event import Event
from function.sort_word import sort_word
class ShowWordList():
    def __init__(
        self,
        current_word_list:str,
        resources:Resource,
        is_hard:bool,
        view:bool
    ):
        self.resources = resources
        self.is_hard = is_hard
        self.viewing = view
        self.word_list = read_word_list(f"static/wordlist/{current_word_list}.txt") if current_word_list else {}
        self.border = pygame.Surface((580, 410))
        self.word_elements:dict[str,Button] = {}
        sorting_element:dict[str,int] = {}
        for word in self.word_list.keys():
            word_str = word
            check = 0
            while self.resources.fonts["Kanit-Regular"].render(word_str,True,(0,0,0)).get_width() + 20 > 540:
                word_str = word_str[:-1]
                check = 1
            if check:
                word_str += "..."
            self.word_elements[word_str] = (
                Button(1,40,(0,0,0),5,1)
                .add_text(self.resources.fonts["Kanit-Regular"],word_str,(0,0,0),auto_readjust=True,padding=20)
            )
            sorting_element[word_str] = self.word_elements[word_str].button_rect.width + 10
        self.lines = sort_word(sorting_element,560)
        self.offset = 0
        self.text = Text(self.resources.fonts["Kanit-Regular"],"W"*33,self.resources.colors["black"]).set_coordinate((415,150))
    def render(self,screen:pygame.Surface):
        if self.viewing:
            self.border.fill((255,255,255))
            offset = 10 - self.offset
            for line in self.lines:
                left_offset = 10
                for word in line:
                    self.word_elements[word].set_coordinate((left_offset,offset)).render(self.border)
                    left_offset += self.word_elements[word].button_rect.width + 10
                offset += 50
            screen.blit(self.border,(400, 130))
        pygame.draw.rect(screen,self.resources.get_current_color(self.is_hard), pygame.Rect(400, 130, 580, 410), 2, 10)

    def update(self,event:Event):
        if event.type == pygame.MOUSEWHEEL and self.viewing:
            mouse_pos = pygame.mouse.get_pos()
            if pygame.Rect(400, 130, 580, 410).collidepoint(mouse_pos):
                self.offset += -event.y*30
                if self.offset < 0 :
                    self.offset = 0
                highest_offset = (len(self.lines) - min(len(self.lines),8)) * 50
                if self.offset > highest_offset:
                    self.offset = highest_offset

