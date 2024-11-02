import pygame
from classes import Page,Resource
from WinPage import WinPage
from MainMenuPage import MainMenuPage
from TopicPage import TopicPage
from HangManPage import HangManPage
from GameOverPage import GameOverPage
from AnswerPage import AnswerPage
from HardTopicPage import HardTopicPage
WHITE = (255, 255, 255)

class Game():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("IjustSad")
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
        resources.add_images({
            "ijudge-mascot": pygame.image.load("static/images/ijudge-mascot.jpg"),
            "pupe-sad": pygame.image.load("static/images/PupeSad.png"),
            "pupe-happy": pygame.image.load("static/images/HappyPupe.png"),
            "klong":pygame.image.load("static/images/Klong.jpg"),
            "pupe-sad-1":pygame.image.load("static/images/PupeSad-1.png"),
            "pupe-sad-2":pygame.image.load("static/images/PupeSad-2.png"),
            "pupe-sad-3":pygame.image.load("static/images/PupeSad-3.png"),
            "pupe-sad-4":pygame.image.load("static/images/PupeSad-4.png"),
            "pupe-sad-5":pygame.image.load("static/images/PupeSad-5.png"),
            "pupe-sad-6":pygame.image.load("static/images/PupeSad-6.png"),
            "pupe-sad-7":pygame.image.load("static/images/PupeSad-7.png"),
            "pupe-sad-8":pygame.image.load("static/images/PupeSad-8.png"),
            "unchack":pygame.image.load("static/images/unchack.png"),
            "chack":pygame.image.load("static/images/chack.png")
        })
        resources.colors = {
            "white":(255,255,255),
            "black":(0,0,0),
            "pupe-cyan":(73,179,255),
            "pupe-violet":(133,113,255),
        }
        resources.assets = {
            "pupe":{
               "normal-color":(73,179,255),
               "hard-color":(133,113,255),
               "normal-images":{
                   1 : pygame.image.load("static/images/PupeSad-1.png"),
                    2 : pygame.image.load("static/images/PupeSad-2.png"),
                    3 : pygame.image.load("static/images/PupeSad-3.png"),
                    4 : pygame.image.load("static/images/PupeSad-4.png"),
                    5 : pygame.image.load("static/images/PupeSad-5.png"),
                    6 : pygame.image.load("static/images/PupeSad-6.png"),
                    7 : pygame.image.load("static/images/PupeSad-7.png"),
                    8 : pygame.image.load("static/images/PupeSad-8.png"),
               }
            },
            "arse":{
                "normal-color":(132,214,255),
                "hard-color":(8,0,96),
                "normal-images":{
                    1 : pygame.image.load("static/images/ArseSad-1.png"),
                    2 : pygame.image.load("static/images/ArseSad-2.png"),
                    3 : pygame.image.load("static/images/ArseSad-3.png"),
                    4 : pygame.image.load("static/images/ArseSad-4.png"),
                    5 : pygame.image.load("static/images/ArseSad-5.png"),
                    6 : pygame.image.load("static/images/ArseSad-6.png"),
                    7 : pygame.image.load("static/images/ArseSad-7.png"),
                    8 : pygame.image.load("static/images/ArseSad-8.png"),

               }
            },
            "akita":{
                "normal-color":(255,85,0),
                "hard-color":(255,32,43),
                "normal-images":{
                    1 : pygame.image.load("static/images/AkitaSad-1.png"),
                    2 : pygame.image.load("static/images/AkitaSad-2.png"),
                    3 : pygame.image.load("static/images/AkitaSad-3.png"),
                    4 : pygame.image.load("static/images/AkitaSad-4.png"),
                    5 : pygame.image.load("static/images/AkitaSad-5.png"),
                    6 : pygame.image.load("static/images/AkitaSad-6.png"),
                    7 : pygame.image.load("static/images/AkitaSad-7.png"),
                    8 : pygame.image.load("static/images/AkitaSad-8.png"),
                }
            },
            "penguin":{
                "normal-color":(204,183,229),
                "hard-color":(240,183,231),
                "normal-images":{
                    1 : pygame.image.load("static/images/PenguinSad-1.png"),
                    2 : pygame.image.load("static/images/PenguinSad-2.png"),
                    3 : pygame.image.load("static/images/PenguinSad-3.png"),
                    4 : pygame.image.load("static/images/PenguinSad-4.png"),
                    5 : pygame.image.load("static/images/PenguinSad-5.png"),
                    6 : pygame.image.load("static/images/PenguinSad-6.png"),
                    7 : pygame.image.load("static/images/PenguinSad-7.png"),
                    8 : pygame.image.load("static/images/PenguinSad-8.png"),
                }
            },
            "gnome":{
                "normal-color":(118,205,38),
                "hard-color":(255,222,33),
                "normal-images":{
                    1 : pygame.image.load("static/images/GnomeSad-1.png"),
                    2 : pygame.image.load("static/images/GnomeSad-2.png"),
                    3 : pygame.image.load("static/images/GnomeSad-3.png"),
                    4 : pygame.image.load("static/images/GnomeSad-4.png"),
                    5 : pygame.image.load("static/images/GnomeSad-5.png"),
                    6 : pygame.image.load("static/images/GnomeSad-6.png"),
                    7 : pygame.image.load("static/images/GnomeSad-7.png"),
                    8 : pygame.image.load("static/images/GnomeSad-8.png"),
                }
            }
        }
        resources.members = ["pupe","arse","akita","penguin","gnome"]
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
                        current_page = TopicPage(self.screen,self.resources)
                    case "HardTopic":
                        current_page = HardTopicPage(self.screen,self.resources)
                    case "HangMan":
                        current_page = HangManPage(self.screen,self.resources,data_attach)
                    case "GameOver":
                        current_page = GameOverPage(self.screen,self.resources,data_attach)
                    case "WinPage":
                        current_page = WinPage(self.screen,self.resources)
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