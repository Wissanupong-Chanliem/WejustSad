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
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
BLACK = (0,0,0)
PUPE_CYAN = (73,179,255)

class Game():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("IjustSad")
        self.screen = pygame.display.set_mode((1080, 720))
        self.screen.fill(WHITE)
        self.resources = self.load_resource()
        self.pages:dict[str,Page] = {
            "MainMenu":MainMenuPage(self.screen,self.resources),
            "Topic":TopicPage(self.screen,self.resources),
            "HangMan":HangManPage(self.screen,self.resources),
            "GameOver":GameOverPage(self.screen,self.resources),
            "WinPage":WinPage(self.screen,self.resources)
        }

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
        return resources

    def run(self):
        current_page:Page = self.pages["MainMenu"]
        running = True
        while running:
            if current_page.redirect:
                to = current_page.redirect
                current_page.reset()
                current_page = self.pages[to]
                self.screen.fill(WHITE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    quit()
                current_page.update(event)
            self.screen.fill((255,255,255))
            current_page.render()
            pygame.display.update()

main = Game()
main.run()