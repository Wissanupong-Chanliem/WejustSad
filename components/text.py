import pygame
class Text():
    def __init__(
        self,
        font:pygame.font.Font,
        text:str,
        color:tuple[int,int,int],
    ):
        self.text = font.render(text,True,color)
        self.text_rect = self.text.get_rect()

    def render(self,screen:pygame.Surface):
        screen.blit(self.text,self.text_rect)

    def set_coordinate(self,coordinate:tuple[int,int],origin_center=False):
        if origin_center:
            self.text_rect.center = (coordinate[0],coordinate[1])
        else:
            self.text_rect.topleft = (coordinate[0],coordinate[1])
        return self

