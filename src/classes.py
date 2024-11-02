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

    def change_character(self,direction):
        self.current_member+=direction
        if self.current_member > len(self.members)-1:
            self.current_member = 0
        if self.current_member < 0:
            self.current_member = len(self.members)-1
        self.load_character_assets()

    def load_character_assets(self):
        match self.members[self.current_member]:
            case "klong":
                self.assets = {
                    "normal-color":(255,170,0),
                    "hard-color":(255,144,0),
                    "normal-images":{
                        0 : pygame.image.load("static/images/HappyKlong.png"),
                        1 : pygame.image.load("static/images/KlongSad-1.png"),
                        2 : pygame.image.load("static/images/KlongSad-2.png"),
                        3 : pygame.image.load("static/images/KlongSad-3.png"),
                        4 : pygame.image.load("static/images/KlongSad-4.png"),
                        5 : pygame.image.load("static/images/KlongSad-5.png"),
                        6 : pygame.image.load("static/images/KlongSad-6.png"),
                        7 : pygame.image.load("static/images/KlongSad-7.png"),
                        8 : pygame.image.load("static/images/KlongSad-8.png"),
                        9 : pygame.image.load("static/images/KlongSad-9.png"),
                    },
                    "hard-images":{
                        0 : pygame.image.load("static/images/HappyKlong_Hard.png"),
                        1 : pygame.image.load("static/images/KlongSad_Hard-1.png"),
                        2 : pygame.image.load("static/images/KlongSad_Hard-2.png"),
                        3 : pygame.image.load("static/images/KlongSad_Hard-3.png"),
                        4 : pygame.image.load("static/images/KlongSad_Hard-4.png"),
                        5 : pygame.image.load("static/images/KlongSad_Hard-5.png"),
                        6 : pygame.image.load("static/images/KlongSad_Hard-6.png"),
                        7 : pygame.image.load("static/images/KlongSad_Hard-7.png"),
                        8 : pygame.image.load("static/images/KlongSad_Hard-8.png"),
                        9 : pygame.image.load("static/images/KlongSad_Hard-9.png"),
                    }
                }
            case "pupe":
                self.assets = {
                    "normal-color":(73,179,255),
                    "hard-color":(170,0,255),
                    "normal-images":{
                            0 : pygame.image.load("static/images/HappyPupe.png"),
                            1 : pygame.image.load("static/images/PupeSad-1.png"),
                            2 : pygame.image.load("static/images/PupeSad-2.png"),
                            3 : pygame.image.load("static/images/PupeSad-3.png"),
                            4 : pygame.image.load("static/images/PupeSad-4.png"),
                            5 : pygame.image.load("static/images/PupeSad-5.png"),
                            6 : pygame.image.load("static/images/PupeSad-6.png"),
                            7 : pygame.image.load("static/images/PupeSad-7.png"),
                            8 : pygame.image.load("static/images/PupeSad-8.png"),
                    },
                    "hard-images":{
                            0 : pygame.image.load("static/images/HappyPupe_Hard.png"),
                            1 : pygame.image.load("static/images/PupeSad_Hard-1.png"),
                            2 : pygame.image.load("static/images/PupeSad_Hard-2.png"),
                            3 : pygame.image.load("static/images/PupeSad_Hard-3.png"),
                            4 : pygame.image.load("static/images/PupeSad_Hard-4.png"),
                            5 : pygame.image.load("static/images/PupeSad_Hard-5.png"),
                            6 : pygame.image.load("static/images/PupeSad_Hard-6.png"),
                            7 : pygame.image.load("static/images/PupeSad_Hard-7.png"),
                            8 : pygame.image.load("static/images/PupeSad_Hard-8.png"),
                    }
                }
            case "arse":
                self.assets = {
                    "normal-color":(132,214,255),
                    "hard-color":(8,0,96),
                    "normal-images":{
                        0 : pygame.image.load("static/images/HappyArse.png"),
                        1 : pygame.image.load("static/images/ArseSad-1.png"),
                        2 : pygame.image.load("static/images/ArseSad-2.png"),
                        3 : pygame.image.load("static/images/ArseSad-3.png"),
                        4 : pygame.image.load("static/images/ArseSad-4.png"),
                        5 : pygame.image.load("static/images/ArseSad-5.png"),
                        6 : pygame.image.load("static/images/ArseSad-6.png"),
                        7 : pygame.image.load("static/images/ArseSad-7.png"),
                        8 : pygame.image.load("static/images/ArseSad-8.png"),
                    },
                    "hard-images":{
                        0 : pygame.image.load("static/images/HappyArse_Hard.png"),
                        1 : pygame.image.load("static/images/ArseSad_Hard-1.png"),
                        2 : pygame.image.load("static/images/ArseSad_Hard-2.png"),
                        3 : pygame.image.load("static/images/ArseSad_Hard-3.png"),
                        4 : pygame.image.load("static/images/ArseSad_Hard-4.png"),
                        5 : pygame.image.load("static/images/ArseSad_Hard-5.png"),
                        6 : pygame.image.load("static/images/ArseSad_Hard-6.png"),
                        7 : pygame.image.load("static/images/ArseSad_Hard-7.png"),
                        8 : pygame.image.load("static/images/ArseSad_Hard-8.png"),
                    }
                }
            case "akita":
                self.assets = {
                    "normal-color":(255,85,0),
                    "hard-color":(255,32,43),
                    "normal-images":{
                        0 : pygame.image.load("static/images/HappyAkita.png"),
                        1 : pygame.image.load("static/images/AkitaSad-1.png"),
                        2 : pygame.image.load("static/images/AkitaSad-2.png"),
                        3 : pygame.image.load("static/images/AkitaSad-3.png"),
                        4 : pygame.image.load("static/images/AkitaSad-4.png"),
                        5 : pygame.image.load("static/images/AkitaSad-5.png"),
                        6 : pygame.image.load("static/images/AkitaSad-6.png"),
                        7 : pygame.image.load("static/images/AkitaSad-7.png"),
                        8 : pygame.image.load("static/images/AkitaSad-8.png"),
                    },
                    "hard-images":{
                        0 : pygame.image.load("static/images/HappyAkita_Hard.png"),
                        1 : pygame.image.load("static/images/AkitaSad_Hard-1.png"),
                        2 : pygame.image.load("static/images/AkitaSad_Hard-2.png"),
                        3 : pygame.image.load("static/images/AkitaSad_Hard-3.png"),
                        4 : pygame.image.load("static/images/AkitaSad_Hard-4.png"),
                        5 : pygame.image.load("static/images/AkitaSad_Hard-5.png"),
                        6 : pygame.image.load("static/images/AkitaSad_Hard-6.png"),
                        7 : pygame.image.load("static/images/AkitaSad_Hard-7.png"),
                        8 : pygame.image.load("static/images/AkitaSad_Hard-8.png"),
                    }
                }
            case "penguin":
                self.assets = {
                    "normal-color":(204,183,229),
                    "hard-color":(240,183,231),
                    "normal-images":{
                        0 : pygame.image.load("static/images/HappyPenguin.png"),
                        1 : pygame.image.load("static/images/PenguinSad-1.png"),
                        2 : pygame.image.load("static/images/PenguinSad-2.png"),
                        3 : pygame.image.load("static/images/PenguinSad-3.png"),
                        4 : pygame.image.load("static/images/PenguinSad-4.png"),
                        5 : pygame.image.load("static/images/PenguinSad-5.png"),
                        6 : pygame.image.load("static/images/PenguinSad-6.png"),
                        7 : pygame.image.load("static/images/PenguinSad-7.png"),
                        8 : pygame.image.load("static/images/PenguinSad-8.png"),
                    },
                    "hard-images":{
                        0 : pygame.image.load("static/images/HappyPenguin_Hard.png"),
                        1 : pygame.image.load("static/images/PenguinSad_Hard-1.png"),
                        2 : pygame.image.load("static/images/PenguinSad_Hard-2.png"),
                        3 : pygame.image.load("static/images/PenguinSad_Hard-3.png"),
                        4 : pygame.image.load("static/images/PenguinSad_Hard-4.png"),
                        5 : pygame.image.load("static/images/PenguinSad_Hard-5.png"),
                        6 : pygame.image.load("static/images/PenguinSad_Hard-6.png"),
                        7 : pygame.image.load("static/images/PenguinSad_Hard-7.png"),
                        8 : pygame.image.load("static/images/PenguinSad_Hard-8.png"),
                    }
                }
            case "gnome":
                self.assets = {
                    "normal-color":(118,205,38),
                    "hard-color":(255,222,33),
                    "normal-images":{
                        0 : pygame.image.load("static/images/HappyGnome.png"),
                        1 : pygame.image.load("static/images/GnomeSad-1.png"),
                        2 : pygame.image.load("static/images/GnomeSad-2.png"),
                        3 : pygame.image.load("static/images/GnomeSad-3.png"),
                        4 : pygame.image.load("static/images/GnomeSad-4.png"),
                        5 : pygame.image.load("static/images/GnomeSad-5.png"),
                        6 : pygame.image.load("static/images/GnomeSad-6.png"),
                        7 : pygame.image.load("static/images/GnomeSad-7.png"),
                        8 : pygame.image.load("static/images/GnomeSad-8.png"),
                    },
                    "hard-images":{
                        0 : pygame.image.load("static/images/HappyGnome_Hard.png"),
                        1 : pygame.image.load("static/images/GnomeSad_Hard-1.png"),
                        2 : pygame.image.load("static/images/GnomeSad_Hard-2.png"),
                        3 : pygame.image.load("static/images/GnomeSad_Hard-3.png"),
                        4 : pygame.image.load("static/images/GnomeSad_Hard-4.png"),
                        5 : pygame.image.load("static/images/GnomeSad_Hard-5.png"),
                        6 : pygame.image.load("static/images/GnomeSad_Hard-6.png"),
                        7 : pygame.image.load("static/images/GnomeSad_Hard-7.png"),
                        8 : pygame.image.load("static/images/GnomeSad_Hard-8.png"),
                    }
                }
    def get_current_assets(self):
        return self.assets

    def get_current_sprite(self,is_hard:bool):
        if is_hard:
            return self.assets["hard-images"]
        return self.assets["normal-images"]

    def get_current_color(self,is_hard:bool):
        if is_hard:
            return self.assets["hard-color"]
        return self.assets["normal-color"]
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
