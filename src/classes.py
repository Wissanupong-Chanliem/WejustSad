import pygame
class Resource:
    def __init__(self):
        self.fonts = {}
        self.colors = {}
        self.assets = {}
        self.members = []
        self.current_member = 0
    def add_fonts(self,font_list:dict[str,pygame.font.Font]):
        self.fonts = font_list
    def add_images(self,images:dict[str,pygame.Surface]):
        self.images = images
    def get_current_assets(self):
        return self.assets[self.members[self.current_member]]
    def get_current_sprite(self,is_hard:bool):
        if is_hard:
            return self.assets[self.members[self.current_member]]["hard-images"]
        return self.assets[self.members[self.current_member]]["normal-images"]
    def get_current_color(self,is_hard:bool):
        if is_hard:
            return self.assets[self.members[self.current_member]]["hard-color"]
        return self.assets[self.members[self.current_member]]["normal-color"]
class Redirect:
    def __init__(self,request="",data=None):
        self.request = request
        self.data = data
class Page():
    def __init__(self,screen:pygame.Surface,resources:Resource):
        self.screen_ref = screen
        self.redirect = None
        self.resources = resources
        self.data = None
    def render(self):
        pass
    def redirect_to(self,to:str):
        self.redirect = Redirect(to)
    def redirect_with_data(self,to:str,data):
        self.redirect = Redirect(to,data)
    def update(self, event:pygame.event.Event):
        pass
    def reset(self):
        self.__init__(self.screen_ref,self.resources)
