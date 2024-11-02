import pygame
from classes import Page,Resource
from WinPage import WinPage
from MainMenuPage import MainMenuPage
from TopicPage import TopicPage
from HangManPage import HangManPage
from GameOverPage import GameOverPage
from AnswerPage import AnswerPage
WHITE = (255, 255, 255)

class Game():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("{v}justSad")
        self.screen = pygame.display.set_mode((1080, 720))
        self.screen.fill(WHITE)
        self.resources = self.load_resource()

    def load_resource(self) -> Resource:
        resources = Resource()
        resources.add_fonts({
            "Kanit-Title": pygame.font.Font("static/font/Kanit-SemiBold.ttf",48),
            "Kanit-Header": pygame.font.Font("static/font/Kanit-Regular.ttf",32),
            "Kanit-Header-1": pygame.font.Font("static/font/Kanit-Regular.ttf",28),
            "Kanit-Regular": pygame.font.Font("static/font/Kanit-Regular.ttf",20),
            "Kanit-Header-2":pygame.font.Font("static/font/Kanit-Regular.ttf",40),
            "Kanit-Word":pygame.font.Font("static/font/Kanit-SemiBold.ttf",58),
            "Kanit-Bold-Regular-Size":pygame.font.Font("static/font/Kanit-SemiBold.ttf",40),
            "Kanit-Klong":pygame.font.Font("static/font/Kanit-Bold.ttf",90)
        })
        resources.colors = {
            "white":(255,255,255),
            "black":(0,0,0),
        }
        resources.assets = {
            "pupe":{
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
            },
            "arse":{
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
            },
            "akita":{
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
            },
            "penguin":{
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
            },
            "gnome":{
                "normal-color":(118,205,38),
                "hard-color":(255,192,0),
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
            },
        }
        resources.members = ["pupe","arse","akita","penguin","gnome"]
        if True:
            resources.members.append("klong")
            resources.assets["klong"] = {
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
                }
            }
        return resources

    def run(self):
        current_page:Page = MainMenuPage(self.screen,self.resources)
        running = True
        while running:
            if current_page.redirect:
                to = current_page.redirect.request
                data_attach = current_page.redirect.data
                match to:
                    case "MainMenu":
                        current_page = MainMenuPage(self.screen,self.resources)
                    case "Topic":
                        current_page = TopicPage(self.screen,self.resources,data_attach)
                    case "HangMan":
                        current_page = HangManPage(self.screen,self.resources,data_attach)
                    case "GameOver":
                        current_page = GameOverPage(self.screen,self.resources,data_attach)
                    case "WinPage":
                        current_page = WinPage(self.screen,self.resources,data_attach)
                    case "Answer":
                        current_page = AnswerPage(self.screen,self.resources,data_attach)
                self.screen.fill(WHITE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    quit()
                current_page.update(event)
            self.screen.fill(WHITE)
            current_page.render()
            pygame.display.update()

main = Game()
main.run()