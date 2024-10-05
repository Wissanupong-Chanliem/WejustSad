import pygame
import pygame.draw_py
from ..button import Button
from classes import Resource
class TopicList():
    def __init__(
        self,
        topics:dict[str,str],
        resources:Resource
    ):
        self.resources = resources
        self.topics = topics
        self.topic_size = (250,80)
        self.position = (200,100)
        self.topics_elements:list[Button] = []
        for i,topic in enumerate(self.topics.items()):
            self.topics_elements.append(
                Button(*self.topic_size,(0,0,0),5,1)
                .add_text(self.resources.fonts["Kanit-Regular"],topic[0],(0,0,0))
                .set_coordinate((self.position[0]+(i*90),self.position[1]))
            )

    def render(self,screen:pygame.Surface):
        for ele in self.topics_elements:
            ele.render(screen)
        # pygame.draw.rect(screen, (255,255,255), (*self.position,*self.topic_size), 0)
        # for i in range(2):
        #     pygame.draw.rect(screen, (0,0,0), (self.position[0]-i,self.position[1]-i,*self.topic_size), 1)

    def add_text(
        self,
        font:pygame.font.Font,
        text:str,
        color:tuple[int,int,int],
        center = True
    ):
        self.text = font.render(text,True,color)
        self.text_rect = self.text.get_rect()
        if center:
            self.text_rect.center = self.button_rect.center
        return self

    def set_coordinate(self,coordinate:tuple[int,int],origin_center=False):
        if origin_center:
            self.button_rect.center = (coordinate[0],coordinate[1])
        else:
            self.button_rect.topleft = (coordinate[1],coordinate[0])
        if self.text:
            self.text_rect.center = self.button_rect.center
        return self
