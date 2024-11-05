import pygame
from math import floor
class ScrollBar():
    def __init__(self,pos:tuple[int,int],width,height,track_color,thumb_color) -> None:
        self.pos = pos
        self.width = width
        self.height = height
        self.track_color = track_color
        self.thumb_color = thumb_color
        self.scrolled = 0
        self.is_dragging = False
        self.changed = False
        self.rect = pygame.draw.rect(pygame.Surface((width,height)),self.track_color,(*self.pos,self.width,self.height),0,self.width)

    def render(self,screen:pygame.Surface):
        self.rect = pygame.draw.rect(screen,self.track_color,(*self.pos,self.width,self.height),0,self.width)
        pygame.draw.rect(screen,self.thumb_color,(self.pos[0],self.pos[1]+self.scrolled,self.width,self.height//10),0,self.width)

    def set_scroll_dist(self,scrolled:float):
        self.scrolled = scrolled*(self.height-self.height//10)

    def update(self,event:pygame.event.Event):
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(pos):
            self.is_dragging = True
        if event.type == pygame.MOUSEBUTTONUP:
            self.is_dragging = False
        if self.is_dragging and event.type == pygame.MOUSEMOTION:
            self.scrolled += pygame.mouse.get_rel()[1]
            self.changed = True
            if self.scrolled < 0:
                self.scrolled = 0
            if self.scrolled > (self.height-self.height//10):
                self.scrolled = self.height-self.height//10

    def get_offset_percentage(self):
        return self.scrolled / (self.height-self.height//10)
    def has_changed(self):
        if not self.changed:
            return self.changed
        self.changed = False
        return True
