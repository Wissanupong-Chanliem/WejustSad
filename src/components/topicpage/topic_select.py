import pygame
import pygame.draw_py
from ..button import Button
from classes import Resource
from pygame.event import Event
class TopicList():
    def __init__(
        self,
        topics:dict[str,str],
        resources:Resource
    ):
        self.resources = resources
        self.topics = topics
        self.topic_size = (250,80)
        self.position = (0,0)
        self.border = pygame.Surface((250,360))
        self.topics_elements:list[Button] = []
        for i,topic in enumerate(self.topics.items()):
            self.topics_elements.append(
                Button(*self.topic_size,(0,0,0),5,1)
                .add_text(self.resources.fonts["Kanit-Regular"],topic[0],(0,0,0))
                .set_coordinate((0,(i*90)))
            )
        self.offset = 0
        self.selected = ""
    def render(self,screen:pygame.Surface):
        self.border.fill((255,255,255))
        for i in range(len(self.topics)):
            self.topics_elements[i].set_coordinate((0,(i*90)-self.offset))
            self.topics_elements[i].render(self.border)
        screen.blit(self.border,(100,150))
        #self.offset += 1

    def update(self,event:Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked_pos = pygame.mouse.get_pos()
            clicked_pos = (clicked_pos[0]-100,clicked_pos[1])
            for topic in self.topics_elements:
                if topic.button_rect.collidepoint(clicked_pos):
                    self.selected = topic.text
    def get_selected(self):
        return self.selected