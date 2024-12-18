import pygame
from pygame.event import Event
import pythainlp.util
from classes import Page,Resource
from components.text import Text
from components.button import Button
from function import check_answer
import pythainlp
from components.keyboard import get_keyboard,used_key
from typing import TypeAlias

data_in:TypeAlias = dict[
    "current_word":int,
    "wordlist":list[(str,str)],
    "is_hard":bool,
    "current_sad":int,
    "is_builtin":bool
]
SCALE = 0.28
class HangManPage(Page):
    def __init__(self,screen:pygame.Surface,resources:Resource,data:data_in):
        Page.__init__(self,screen,resources)
        self.data = data
        self.word_list = data["wordlist"]
        self.current_key = ""
        self.kanan_num = data["current_word"]
        self.wrong_count = data["current_sad"]
        self.guessed = []
        self.word_status = check_answer.check_answer(self.word_list[self.kanan_num][0],"_"*len(self.word_list[self.kanan_num][0]),self.current_key)
        self.word = (
            Text(resources.fonts["Kanit-Word"],self.word_status,self.resources.get_current_color(self.data["is_hard"]))
            .set_coordinate((self.screen_ref.get_rect().centerx,70),origin_center = True)
        )
        self.menu_button = (
            Button(250,80,self.resources.get_current_color(self.data["is_hard"]),4)
            .add_text(resources.fonts["Kanit-Header"],"Confirm",self.resources.colors["white"])
            .set_coordinate((self.screen_ref.get_width()-200,600),origin_center=True)
        )
        self.score = (
            Text(resources.fonts["Kanit-Bold-Regular-Size"],"Score",self.resources.get_current_color(self.data["is_hard"]))
            .set_coordinate((self.screen_ref.get_width()-150,20))
        )
        self.kanan = (
            Text(resources.fonts["Kanit-Bold-Regular-Size"],str(self.kanan_num),self.resources.get_current_color(self.data["is_hard"]))
            .set_coordinate((self.screen_ref.get_width()-111,70))
        )
        self.guessing = (
            Text(resources.fonts["Kanit-Bold-Regular-Size"],"Guessing",self.resources.get_current_color(self.data["is_hard"]))
            .set_coordinate((self.screen_ref.get_width()-200,440),origin_center=True)
        )
        self.guess =(
            Text(resources.fonts["Kanit-Title"],"\""+self.current_key+"\"",self.resources.get_current_color(self.data["is_hard"]))
            .set_coordinate((self.screen_ref.get_width()-200,500),origin_center=True)
        )
        self.keyboard = get_keyboard(self.resources,self.data["is_hard"])
        self.image = pygame.transform.scale_by(self.resources.get_current_sprite(self.data["is_hard"])[self.wrong_count],SCALE)
    def render(self):
        match self.wrong_count:
            case 0:
                pass
            case _:
                self.screen_ref.blit(
                    self.image,
                    (
                        self.screen_ref.get_rect().centerx - self.image.get_rect().centerx,
                        90
                    ),
            )
        self.keyboard.draw(self.screen_ref)
        self.menu_button.render(self.screen_ref)
        self.score.render(self.screen_ref)
        self.kanan.render(self.screen_ref)
        self.guessing.render(self.screen_ref)
        if self.current_key:
            self.guess.render(self.screen_ref)
        self.word.render(self.screen_ref)
        
    def update(self, event: Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.menu_button.button_rect.collidepoint(pygame.mouse.get_pos()):
                if self.current_key in self.guessed:
                    return
                self.guessed.append(self.current_key)
                used_key(self.keyboard,self.current_key)
                if self.current_key.lower() in self.word_list[self.kanan_num][0].lower():
                    current_status = check_answer.check_answer(self.word_list[self.kanan_num][0],self.word.text_str,self.current_key)
                    self.word.update_text(current_status).set_coordinate((self.screen_ref.get_rect().centerx,70),origin_center = True)
                    if current_status == self.word_list[self.kanan_num][0]:
                        self.kanan_num += 1
                        data = {
                            "score":self.kanan_num,
                            "word":self.word_list[self.kanan_num-1],
                            "current_wordlist":self.word_list,
                            "is_hard":self.data["is_hard"],
                            "current_sad":self.wrong_count,
                            "is_builtin":self.data["is_builtin"]
                        }
                        self.redirect_with_data("Answer",data)  
                else:
                    self.wrong_count += 1
                    self.image = pygame.transform.scale_by(self.resources.get_current_sprite(self.data["is_hard"])[self.wrong_count],SCALE)
                    if self.wrong_count >= len(self.resources.get_current_sprite(self.data["is_hard"])) - 1:
                        data = {
                            "score":self.kanan_num,
                            "word":self.word_list[self.kanan_num],
                            "is_hard":self.data["is_hard"]
                        }
                        self.redirect_with_data("GameOver",data)
                self.current_key = ""
                self.guess.update_text("\""+self.current_key+"\"").set_coordinate((self.screen_ref.get_width()-200,500),origin_center=True)
        if event.type == pygame.KEYDOWN:
            current_key = pythainlp.util.thai_to_eng(event.unicode).upper()
            if current_key.isalpha():
                self.current_key = current_key
                self.guess.update_text("\""+self.current_key+"\"").set_coordinate((self.screen_ref.get_width()-200,500),origin_center=True)
            if event.key == pygame.K_RETURN:
                if self.current_key in self.guessed:
                    return
                self.guessed.append(self.current_key)
                used_key(self.keyboard,self.current_key)
                if self.current_key.lower() in self.word_list[self.kanan_num][0].lower():
                    current_status = check_answer.check_answer(self.word_list[self.kanan_num][0],self.word.text_str,self.current_key)
                    self.word.update_text(current_status).set_coordinate((self.screen_ref.get_rect().centerx,70),origin_center = True)
                    if current_status == self.word_list[self.kanan_num][0]:
                        self.kanan_num += 1
                        data = {
                            "score":self.kanan_num,
                            "word":self.word_list[self.kanan_num-1],
                            "current_wordlist":self.word_list,
                            "is_hard":self.data["is_hard"],
                            "current_sad":self.wrong_count,
                            "is_builtin":self.data["is_builtin"]
                        }
                        self.redirect_with_data("Answer",data)  
                else:
                    self.wrong_count += 1
                    self.image = pygame.transform.scale_by(self.resources.get_current_sprite(self.data["is_hard"])[self.wrong_count],SCALE)
                    if self.wrong_count >= len(self.resources.get_current_sprite(self.data["is_hard"])) - 1:
                        data = {
                            "score":self.kanan_num,
                            "word":self.word_list[self.kanan_num],
                            "is_hard":self.data["is_hard"]
                        }
                        self.redirect_with_data("GameOver",data)
                self.current_key = ""
                self.guess.update_text("\""+self.current_key+"\"").set_coordinate((self.screen_ref.get_width()-200,500),origin_center=True)
