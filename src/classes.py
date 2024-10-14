import pygame
class Resource:
    def __init__(self):
        self.fonts = {}
        self.images = {}
        self.colors = {}
    def add_fonts(self,font_list:dict[str,pygame.font.Font]):
        self.fonts = font_list
    def add_images(self,images:dict[str,pygame.Surface]):
        self.images = images
class Page():
    def __init__(self,screen:pygame.Surface,resources:Resource):
        self.screen_ref = screen
        self.redirect = None
        self.resources = resources
    def render():
        pass
    def redirect_to(self,new_page:str):
        self.redirect = new_page
    def update(self, event:pygame.event.Event):
        pass
    def reset(self):
        self.__init__(self.screen_ref,self.resources)