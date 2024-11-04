import pygame
import pygame.draw_py
from .text import Text
class Button():
    def __init__(
        self,
        width:int,
        height:int,
        color:tuple[int,int,int],
        border_radius = 0,
        is_border = 0,
    ):
        self.button_rect = pygame.rect.Rect(0,0,width,height)
        self.color = color
        self.text_image = None
        self.text_rect = None
        self.border_radius = border_radius
        self.is_border = is_border
        self.text = ""

    def render(self,screen:pygame.Surface):
        pygame.draw.rect(screen,self.color,self.button_rect,self.is_border,border_radius=self.border_radius)
        if self.text_image:
            screen.blit(self.text_image,self.text_rect)

    def add_text(
        self,
        font:pygame.font.Font,
        text:str,
        color:tuple[int,int,int],
        center = True,
        auto_readjust = False,
        padding = 0
    ):
        self.text = text
        self.text_image = font.render(text,True,color)
        if auto_readjust and self.text_image.get_width() > (self.button_rect.right-self.button_rect.left):
            self.button_rect.width = self.text_image.get_width() + padding * 2
        self.text_rect = self.text_image.get_rect()
        if center:
            self.text_rect.center = self.button_rect.center
        else:
            self.text_rect.topleft = self.button_rect.topleft
        return self

    def set_coordinate(self,coordinate:tuple[int,int],origin_center=False):
        if origin_center:
            self.button_rect.center = (coordinate[0],coordinate[1])
        else:
            self.button_rect.topleft = (coordinate[0],coordinate[1])
        if self.text_image:
            self.text_rect.center = self.button_rect.center
        return self
