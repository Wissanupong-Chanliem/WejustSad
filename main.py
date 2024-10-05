import pygame
from pygame.event import Event
from classes import Page,Resource
from components.text import Text
from components.button import Button
from components.topicpage.topic_select import TopicList
from function.read_word_list import read_word_list
from function.read_wordlist_folder import read_wordlist_dir
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
BLACK = (0,0,0)
PUPE_CYAN = (73,179,255)
class MainMenuPage(Page):
    def __init__(self,screen:pygame.Surface,resources):
        Page.__init__(self,screen,resources)
        screen_rect = self.screen_ref.get_rect()
        self.classic_button = (
            Button(200,80,PUPE_CYAN,4)
            .add_text(resources.fonts["Kanit-Header"],"Classic",WHITE)
            .set_coordinate((screen_rect.centerx,530),origin_center = True)
        )
        self.hard_button = (
            Button(200,80,(133,113,255),4)
            .add_text(resources.fonts["Kanit-Header"],"Hard",WHITE)
            .set_coordinate((screen_rect.centerx,630),origin_center = True)
        )
        self.title_text = (
            Text(resources.fonts["Kanit-Title"],"{v}JustSad ;-;",PUPE_CYAN)
            .set_coordinate((screen_rect.centerx,50),origin_center = True)
        )
    def render(self):
        self.title_text.render(self.screen_ref)
        self.screen_ref.blit(
            self.resources.images["pupe-sad"],
            (
                self.screen_ref.get_rect().centerx - self.resources.images["pupe-sad"].get_rect().centerx,
                100
            ),
        )
        self.classic_button.render(self.screen_ref)
        self.hard_button.render(self.screen_ref)
    
    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Classic Mode button is clicked
            if self.classic_button.button_rect.collidepoint(pygame.mouse.get_pos()):
                self.redirect_to("Topic")
        
class TopicPage(Page):
    def __init__(self,screen:pygame.Surface,resources):
        Page.__init__(self,screen,resources)
        self.title_text = (
            Text(resources.fonts["Kanit-Title"],"Topic",BLACK)
            .set_coordinate((self.screen_ref.get_rect().centerx,100),origin_center = True)
        )
        self.start_button = (
            Button(200,80,PUPE_CYAN,4)
            .add_text(resources.fonts["Kanit-Header"],"Start!!!",BLACK)
            .set_coordinate((self.screen_ref.get_width()-200,600),origin_center=True)
        )
        self.topic_selection = TopicList(read_wordlist_dir(),resources)

    def render(self):
        self.title_text.render(self.screen_ref)
        self.start_button.render(self.screen_ref)
        self.topic_selection.render(self.screen_ref)
    def update(self, event: Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Classic Mode button is clicked
            if self.start_button.button_rect.collidepoint(pygame.mouse.get_pos()):
                self.redirect_to("HangMan")

class HangManPage(Page):
    def __init__(self,screen:pygame.Surface,resources):
        Page.__init__(self,screen,resources)
        self.title_text = (
            Text(resources.fonts["Kanit-Title"],"Hang Man",BLACK)
            .set_coordinate((self.screen_ref.get_rect().centerx,100),origin_center = True)
        )
        self.menu_button = (
            Button(300,80,PUPE_CYAN,4)
            .add_text(resources.fonts["Kanit-Header"],"Back to Main Menu",BLACK)
            .set_coordinate((self.screen_ref.get_width()-200,600),origin_center=True)
        )
    def render(self):
        self.title_text.render(self.screen_ref)
        self.menu_button.render(self.screen_ref)
    def update(self, event: Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Classic Mode button is clicked
            if self.menu_button.button_rect.collidepoint(pygame.mouse.get_pos()):
                self.redirect_to("MainMenu")


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
            "HangMan":HangManPage(self.screen,self.resources)
        }

    def load_resource(self) -> Resource:
        resources = Resource()
        resources.add_fonts({
            "Kanit-Title": pygame.font.Font("static/font/Kanit-SemiBold.ttf",48),
            "Kanit-Header": pygame.font.Font("static/font/Kanit-Regular.ttf",32),
            "Kanit-Regular": pygame.font.Font("static/font/Kanit-Regular.ttf",20)
        })
        resources.add_images({
            "ijudge-mascot": pygame.image.load("static/images/ijudge-mascot.jpg"),
            "pupe-sad": pygame.image.load("static/images/PupeSad.png")
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
            current_page.render()
            pygame.display.update()

main = Game()
main.run()