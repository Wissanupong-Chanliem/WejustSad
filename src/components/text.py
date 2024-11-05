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
        self.text_str = text
        self.font = font
        self.color = color
        
    def render(self,screen:pygame.Surface):
        
        screen.blit(self.text,self.text_rect)

    def set_coordinate(self,coordinate:tuple[int,int],origin_center=False):
        if origin_center:
            self.text_rect.center = (coordinate[0],coordinate[1])
        else:
            self.text_rect.topleft = (coordinate[0],coordinate[1])
        return self
    def update_text(self,text,anchor_center=True):
        if anchor_center:
            old_pos = self.text.get_rect().center
            self.text = self.font.render(text,True,self.color)
            self.text_rect = self.text.get_rect()
            self.text_rect.center = old_pos
        else:
            old_pos = self.text.get_rect().topleft
            self.text = self.font.render(text,True,self.color)
            self.text_rect = self.text.get_rect()
            self.text_rect.topleft = old_pos
        self.text_str = text
        return self
