import pygame
import pygame.draw_py
from ..button import Button
from classes import Resource
from pygame.event import Event
class TopicList():
    def __init__(
        self,
        topics:dict[str,str],
        resources:Resource,
        is_hard:bool
    ):
        self.resources = resources
        self.border = pygame.Surface((250,360))
        self.is_hard = is_hard
        self.topics_elements:list[Button] = []
        for i,topic in enumerate(topics.items()):
            self.topics_elements.append(
                Button(250,80,(0,0,0),5,1)
                .add_text(self.resources.fonts["Kanit-Regular"],topic[0],(0,0,0))
                .set_coordinate((0,(i*90)))
            )
        self.offset = 0
        self.selected = -1
    def render(self,screen:pygame.Surface):
        self.border.fill((255,255,255))
        for i in range(len(self.topics_elements)):
            self.topics_elements[i].set_coordinate((0,(i*90)-self.offset))
            self.topics_elements[i].render(self.border)
            if i == self.selected:
                pygame.draw.rect(self.border,self.resources.get_current_color(self.is_hard),(0,(i*90)-self.offset,250,80),5,5)
        pygame.draw.rect(
            self.border,
            self.resources.get_current_color(self.is_hard),
            (self.border.get_rect().right,(self.offset/len(self.topics_elements)*90)*self.border.get_rect().bottom,250,80),
            5,
            5
        )
        screen.blit(self.border,(100,180))

    def update(self,event:Event):
        if event.type == pygame.MOUSEWHEEL:
            self.offset += -event.y*30
            if self.offset < 0 :
                self.offset = 0
            highest_offset = (len(self.topics_elements) - min(len(self.topics_elements),4)) * 90
            if self.offset > highest_offset:
                self.offset = highest_offset
                    
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            clicked_pos = pygame.mouse.get_pos()
            clicked_pos = (clicked_pos[0]-100,clicked_pos[1]-180)
            for i,topic in enumerate(self.topics_elements):
                if topic.button_rect.collidepoint(clicked_pos):
                    self.selected = i
        
    def get_selected(self):
        if self.selected != -1:
            return self.topics_elements[self.selected].text
        return ""
    def update_list(self,topics:dict[str,str]):
        self.topics_elements.clear()
        for i,topic in enumerate(topics.items()):
            self.topics_elements.append(
                Button(250,80,(0,0,0),5,1)
                .add_text(self.resources.fonts["Kanit-Regular"],topic[0],(0,0,0))
                .set_coordinate((0,(i*90)))
            )