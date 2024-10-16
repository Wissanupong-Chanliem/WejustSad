import pygame
from pygame.event import Event
from classes import Page,Resource
from components.text import Text
from components.button import Button
from components.topicpage.topic_select import TopicList
from function.read_word_list import read_word_list
from function.read_wordlist_folder import read_wordlist_dir

from WinPage import WinPage
from MainMenuPage import MainMenuPage
from TopicPage import TopicPage
from HangManPage import HangManPage
from GameOverPage import GameOverPage

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
            "klong":pygame.image.load("static/images/Klong.jpg")
        })
        resources.colors = {
            "white":(255,255,255),
            "black":(0,0,0),
            "pupe-cyan":(73,179,255)
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
                        current_page = TopicPage(self.screen,self.resources)
                    case "HangMan":
                        current_page = HangManPage(self.screen,self.resources,data_attach)
                    case "GameOver":
                        current_page = GameOverPage(self.screen,self.resources)
                    case "WinPage":
                        current_page = WinPage(self.screen,self.resources)
                #current_page.reset()
                #current_page = self.pages[to]
                #current_page.data = data_attach
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