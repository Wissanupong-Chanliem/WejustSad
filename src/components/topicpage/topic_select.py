import pygame
import pygame.draw_py
from ..button import Button
from classes import Resource
from pygame.event import Event
from function.read_word_list import read_word_list
from .scrollbar import ScrollBar
class TopicList():
    def __init__(
        self,
        topics:dict[str,str],
        resources:Resource,
        is_hard:bool
    ):
        self.resources = resources
        self.border = pygame.Surface((250,360))
        self.is_hard = is_hard
        self.topics_elements:list[tuple[Button,str]] = []
        for topic,words in BUILT_IN_WORDLIST.items():
            self.topics_elements.append((
                Button(250,80,(0,0,0),5,1)
                .add_text(self.resources.fonts["Kanit-Regular"],topic,(0,0,0)),
                words
            ))
        for topic in topics.items():
            self.topics_elements.append((
                Button(250,80,(0,0,0),5,1)
                .add_text(self.resources.fonts["Kanit-Regular"],topic[0],(0,0,0)),
                topic[1]
            ))
        self.offset = 0
        self.selected = -1
        self.scrollbar = ScrollBar((360,180),10,350,(219, 219, 219),(176, 176, 176))
        self.change = False
    def render(self,screen:pygame.Surface):
        self.border.fill((255,255,255))
        for i in range(len(self.topics_elements)):
            self.topics_elements[i][0].set_coordinate((0,(i*90)-self.offset))
            self.topics_elements[i][0].render(self.border)
            if i == self.selected:
                pygame.draw.rect(self.border,self.resources.get_current_color(self.is_hard),(0,(i*90)-self.offset,250,80),5,5)
        pygame.draw.rect(
            self.border,
            self.resources.get_current_color(self.is_hard),
            (self.border.get_rect().right,(self.offset/len(self.topics_elements)*90)*self.border.get_rect().bottom,250,80),
            5,
            5
        )
        screen.blit(self.border,(100,180))
        self.scrollbar.render(screen)

    def update(self,event:Event):
        self.scrollbar.update(event)
        if self.scrollbar.has_changed():
            self.offset = self.scrollbar.get_offset_percentage() * (len(self.topics_elements) - min(len(self.topics_elements),4)) * 90
        if event.type == pygame.MOUSEWHEEL:
            mouse_pos = pygame.mouse.get_pos()
            if pygame.Rect(100,180,250,360).collidepoint(mouse_pos):
                self.offset += -event.y*30
                if self.offset < 0 :
                    self.offset = 0
                highest_offset = (len(self.topics_elements) - min(len(self.topics_elements),4)) * 90
                if self.offset > highest_offset:
                    self.offset = highest_offset
                self.scrollbar.set_scroll_dist(self.offset/highest_offset)
                    
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            clicked_pos = pygame.mouse.get_pos()
            clicked_pos = (clicked_pos[0]-100,clicked_pos[1]-180)
            for i,topic in enumerate(self.topics_elements):
                if topic[0].button_rect.collidepoint(clicked_pos):
                    self.set_selected(i)

    def set_selected(self,index:int):
        self.selected = index
        self.change = True

    def get_selected(self):
        if self.selected != -1:
            if isinstance(self.topics_elements[self.selected][1],str):
                return read_word_list(self.topics_elements[self.selected][1])
            return self.topics_elements[self.selected][1]
        return {}

    def is_builtin(self):
        if self.selected != -1:
            return not isinstance(self.topics_elements[self.selected][1],str)
        return False

    def get_selected_path(self):
        if self.selected != -1:
            if isinstance(self.topics_elements[self.selected][1],str):
                return self.topics_elements[self.selected][1]
            return ""
        return ""

    def update_list(self,topics:dict[str,str]):
        self.topics_elements.clear()
        for topic,words in BUILT_IN_WORDLIST.items():
            self.topics_elements.append((
                Button(250,80,(0,0,0),5,1)
                .add_text(self.resources.fonts["Kanit-Regular"],topic,(0,0,0)),
                words
            ))
        for topic in topics.items():
            self.topics_elements.append((
                Button(250,80,(0,0,0),5,1)
                .add_text(self.resources.fonts["Kanit-Regular"],topic[0],(0,0,0)),
                topic[1]
            ))
        highest_offset = (len(self.topics_elements) - min(len(self.topics_elements),4)) * 90
        if self.offset > highest_offset:
            self.offset = highest_offset
        self.scrollbar.set_scroll_dist(self.offset/highest_offset)

    def has_changed(self):
        if not self.change:
            return self.change
        self.change = False
        return True


BUILT_IN_WORDLIST = {
    "Animals": {
        "Elephant": "ช้าง",
        "Rabbit": "กระต่าย",
        "Dolphin": "ปลาโลมา",
        "Pigeon": "นกพิราบ",
        "Kangaroo": "จิงโจ้",
        "Penguin": "เพนกวิน",
        "Donkey": "ลา",
        "Otter": "นาก",
        "Peacock": "นกยูง",
        "Leopard": "เสือดาว",
        "Parrot": "นกแก้ว",
        "Buffalo": "ควาย",
        "Jaguar": "เสือจากัวร์",
        "Hyena": "ไฮยีน่า",
        "Cheetah": "เสือชีตาห์",
        "Raccoon": "แรคคูน",
        "Porcupine": "เม่น",
        "Turkey": "ไก่งวง",
        "Spider": "แมงมุม",
        "Octopus": "ปลาหมึกยักษ์",
        "Chameleon": "กิ้งก่า",
        "Mongoose": "พังพอน",
        "Alligator": "จระเข้",
        "Shark": "ฉลาม",
        "Hedgehog": "เม่นแคระ",
        "Cricket": "จิ้งหรีด",
        "Bison": "กระทิง",
        "Giraffe": "ยีราฟ",
        "Gorilla": "กอริลลา",
        "Lobster": "กุ้งล็อบสเตอร์",
        "Salmon": "ปลาแซลมอน",
        "Piranha": "ปลาปิรันย่า",
        "Koala": "โคอาลา",
        "Beetle": "ด้วง",
        "Vulture": "นกแร้ง",
        "Eagle": "นกอินทรี",
        "Falcon": "นกเหยี่ยว",
        "Manatee": "พะยูน",
        "Hamster": "แฮมสเตอร์",
        "Chimpanzee": "ลิงชิมแปนซี",
        "Platypus": "ตุ่นปากเป็ด",
        "Woodpecker": "นกหัวขวาน",
        "Anaconda": "งูอนาคอนดา",
        "Hummingbird": "นกฮัมมิ่งเบิร์ด",
        "Goldfish": "ปลาทอง",
        "Rhino": "แรด",
        "Scorpion": "แมงป่อง",
        "Capybara": "คาปิบารา",
        "Hippopotamus": "ฮิปโปโปเตมัส",
        "Sloth": "สลอธ"
    },
    "Country": {
        "United States": "สหรัฐอเมริกา",
        "Canada": "แคนาดา",
        "Mexico": "เม็กซิโก",
        "Argentina": "อาร์เจนตินา",
        "United Kingdom": "สหราชอาณาจักร",
        "France": "ฝรั่งเศส",
        "Germany": "เยอรมนี",
        "Italy": "อิตาลี",
        "Spain": "สเปน",
        "Netherlands": "เนเธอร์แลนด์",
        "Belgium": "เบลเยียม",
        "Switzerland": "สวิตเซอร์แลนด์",
        "Sweden": "สวีเดน",
        "Norway": "นอร์เวย์",
        "Denmark": "เดนมาร์ก",
        "Finland": "ฟินแลนด์",
        "Russia": "รัสเซีย",
        "China": "จีน",
        "Japan": "ญี่ปุ่น",
        "South Korea": "เกาหลีใต้",
        "India": "อินเดีย",
        "Australia": "ออสเตรเลีย",
        "New Zealand": "นิวซีแลนด์",
        "South Africa": "แอฟริกาใต้",
        "Egypt": "อียิปต์",
        "Kenya": "เคนยา",
        "Nigeria": "ไนจีเรีย",
        "Turkey": "ตุรกี",
        "Greece": "กรีซ",
        "Saudi Arabia": "ซาอุดีอาระเบีย",
        "United Arab Emirates": "สหรัฐอาหรับเอมิเรตส์",
        "Israel": "อิสราเอล",
        "Thailand": "ประเทศไทย",
        "Singapore": "สิงคโปร์",
        "Malaysia": "มาเลเซีย",
        "Indonesia": "อินโดนีเซีย",
        "Philippines": "ฟิลิปปินส์",
        "Vietnam": "เวียดนาม",
        "Brazil": "บราซิล",
        "Portugal": "โปรตุเกส",
        "Poland": "โปแลนด์",
        "Ireland": "ไอร์แลนด์",
        "Austria": "ออสเตรีย",
        "Hungary": "ฮังการี",
        "Czech Republic": "สาธารณรัฐเช็ก",
        "North Korea": "เกาหลีเหนือ",
        "Pakistan": "ปากีสถาน",
        "Bangladesh": "บังกลาเทศ",
        "Greenland": "กรีนแลนด์",
        "Ukraine": "ยูเครน"
    },
    "Fruits": {
        "Avocado": "อะโวคาโด",
        "Banana": "กล้วย",
        "Canistel": "ม่อนไข่",
        "Chikoo": "ละมุด",
        "Coconut": "มะพร้าว",
        "Durian": "ทุเรียน",
        "Fig": "มะเดื่อ",
        "Grape": "องุ่น",
        "Grapefruit": "ส้มโอ",
        "Guava": "ฝรั่ง",
        "Jackfruit": "ขนุน",
        "Kiwi": "กีวี่",
        "Lemon": "เลมอน",
        "Longan": "ลำไย",
        "Lychee": "ลิ้นจี่",
        "Mango": "มะม่วง",
        "Mangosteen": "มังคุด",
        "Muskmelon": "แตงไทย",
        "Orange": "ส้ม",
        "Papaya": "มะละกอ",
        "Pineapple": "สับปะรด",
        "Pomegranate": "ทับทิม",
        "Rambutan": "เงาะ",
        "Starfruit": "มะเฟือง",
        "Watermelon": "แตงโม",
        "Apple": "แอปเปิ้ล",
        "Bananas": "กล้วย",
        "Blackberry": "แบล็คเบอรี่",
        "Blueberry": "บลูเบอรี่",
        "Cheery": "เชอร์รี่",
        "Clementine": "ส้มคลีเมนไทน์",
        "Cranberry": "แครนเบอรี่",
        "Date": "อินทผาลัม",
        "Kumquat": "ส้มจี๊ด",
        "Lime": "มะนาว",
        "Mulberry": "ลูกหม่อน",
        "Pear": "ลูกแพร์",
        "Persimmon": "ลูกพลับ",
        "Pomegranat": "ผลทับทิม",
        "Pomelo": "ส้มโอ",
        "Quince": "ผลควินซ์",
        "Rambutans": "เงาะ",
        "Raspberry": "ราสเบอรี่",
        "Satsuma plum": "บ๊วยญี่ปุ่น",
        "Strawberry": "สตรอวเบอรี่",
        "Tangerine": "ส้มจีน",
        "Berry": "เบอร์รี่"
    },
    "PokemonGen1": {
        "Bulbasaur": "ฟุชิกิดาเนะ",
        "Ivysaur": "ฟุชิกิโซ",
        "Venusaur": "ฟุชิกิบานะ",
        "Charmander": "ฮิโตคาเงะ",
        "Charmeleon": "ลิซาร์โดะ",
        "Charizard": "ลิซาร์ดอน",
        "Squirtle": "เซนิกาเมะ",
        "Wartortle": "คาเมล",
        "Blastoise": "คาเม็กซ์",
        "Caterpie": "คาเตอร์ปี",
        "Metapod": "ทรานเซล",
        "Butterfree": "บัตเตอร์ฟรี",
        "Weedle": "บีเดิล",
        "Kakuna": "โคคูน",
        "Beedrill": "สเปียร์",
        "Pidgey": "ป็อปโปะ",
        "Pidgeotto": "พีเจียน",
        "Pidgeot": "พีเจอตโตะ",
        "Rattata": "คอร์รัตตะ",
        "Raticate": "ราติคาเตะ",
        "Spearow": "ยูโตะ",
        "Fearow": "เฟียโรว์",
        "Ekans": "เอคานส์",
        "Arbok": "อาร์บอก",
        "Pikachu": "ปิกาจู",
        "Raichu": "ไรชู",
        "Sandshrew": "ซันดัชช์",
        "Sandslash": "ซันดัชช์",
        "Nidoran": "นิโดรัน",
        "Nidorina": "นิโดรีนา",
        "Nidoqueen": "นิโดควีน",
        "Nidorino": "นิโดรีโน",
        "Nidoking": "นิโดคิง",
        "Clefairy": "เคลฟารี่",
        "Clefable": "เคลแฟเบิล",
        "Vulpix": "วัลพิกซ์",
        "Ninetales": "ไนน์เทลส์",
        "Jigglypuff": "จิกกลี่พัฟ",
        "Wigglytuff": "วิกกลี่ทัฟ",
        "Zubat": "ซูบัต",
        "Golbat": "โกลบัต",
        "Oddish": "ออดดิช",
        "Gloom": "กลูม",
        "Vileplume": "ไวล์พูล์ม",
        "Paras": "พาราส",
        "Parasect": "พาราเซ็คท์",
        "Venonat": "เวโนเนต",
        "Venomoth": "เวโนมอธ",
        "Diglett": "ดิเกล็ต",
        "Dugtrio": "ดักทริโอ",
        "Meowth": "เมียวธ์",
        "Persian": "เพอร์เซียน",
        "Psyduck": "ไซดัค",
        "Golduck": "โกลดัค",
        "Mankey": "มังกี้",
        "Primeape": "ไพรม์เอป",
        "Growlithe": "โกรว์ไลท์",
        "Arcanine": "อาร์แคนไนน์",
        "Poliwag": "โปลิวาก",
        "Poliwhirl": "โปลิไวร์ล",
        "Poliwrath": "โปลิแวร์ธ",
        "Abra": "อาบรา",
        "Kadabra": "คาดาบรา",
        "Alakazam": "อะลาคาซัม",
        "Machop": "มาโชป",
        "Machoke": "มาโช้ค",
        "Machamp": "มาแชมป์",
        "Bellsprout": "เบลล์สปรา",
        "Weepinbell": "วีปปิ้งเบลล์",
        "Victreebel": "วิคทรีเบล",
        "Tentacool": "เทนทาคูล",
        "Tentacruel": "เทนทาครูเอล",
        "Geodude": "จิโอดูด",
        "Graveler": "แกรเวลเลอร์",
        "Golem": "โกเล็ม",
        "Ponyta": "โปนี่ตะ",
        "Rapidash": "ราปิดแอช",
        "Slowpoke": "โสโล่พ็อก",
        "Slowbro": "โสโล่โบร่",
        "Magnemite": "แม็กเนไมท์",
        "Magneton": "แม็กเนตอน",
        "Farfetch'd": "ดั๊กเล็ต",
        "Doduo": "โดดูโอ",
        "Dodrio": "โดดริโอ",
        "Seel": "ซีล",
        "Dewgong": "ดูว์กอง",
        "Grimer": "ไกรมเมอร์",
        "Muk": "มัค",
        "Shellder": "เชลเดอร์",
        "Cloyster": "คลอยสเตอร์",
        "Gastly": "แกสต์ลี่",
        "Haunter": "ฮอนเตอร์",
        "Gengar": "เก็งการ์",
        "Onix": "โอไนซ์",
        "Drowzee": "ดรอวซี่",
        "Hypno": "ฮิปโน",
        "Krabby": "คราบบี้",
        "Kingler": "คิงเลอร์",
        "Voltorb": "โวลทอร์บ",
        "Electrode": "อิเล็กโทรด",
        "Exeggcute": "เอ็กเซ็กคิวท์",
        "Exeggutor": "เอ็กเซ็กคิวเตอร์",
        "Cubone": "คิวโบน",
        "Marowak": "มารอว์วัก",
        "Hitmonlee": "ฮิตมอนลี",
        "Hitmonchan": "ฮิตมอนแชน",
        "Lickitung": "ลิคคิตัง",
        "Koffing": "คอฟฟิง",
        "Weezing": "วีซิ่ง",
        "Rhyhorn": "ไรฮอร์น",
        "Rhydon": "ไรดอน",
        "Chansey": "แชนซี",
        "Tangela": "แทนเจลา",
        "Kangaskhan": "คังคังสคาน",
        "Horsea": "ฮอร์เซีย",
        "Seadra": "ซีดร้า",
        "Goldeen": "โกลดีน",
        "Seaking": "ซีคิง",
        "Staryu": "สตารี่",
        "Starmie": "สตาร์มี",
        "Mr. Mime": "มิสเตอร์ ไมม์",
        "Scyther": "ไซเธอร์",
        "Jynx": "จิงซ์",
        "Electabuzz": "อิเล็คทราบัซ",
        "Magmar": "แม็กมาร์",
        "Pinsir": "พินเซอร์",
        "Tauros": "ทอรัส",
        "Magikarp": "แม็กคาพ",
        "Gyarados": "แกราโดส",
        "Lapras": "แลปราส",
        "Ditto": "ดิตโต้",
        "Eevee": "อีวุย",
        "Vaporeon": "แวปอเรี่ยน",
        "Jolteon": "โจลเทียน",
        "Flareon": "แฟลร์เรี่ยน",
        "Porygon": "โปริกอน",
        "Omanyte": "โอแมนไนต์",
        "Omastar": "โอมาสตาร์",
        "Kabuto": "คาบูโตะ",
        "Kabutops": "คาบูโตปส์",
        "Aerodactyl": "แอร์แด็กไทล์",
        "Snorlax": "สนอร์แล็กซ์",
        "Articuno": "อาร์ติคูโน่",
        "Zapdos": "แซพดอส",
        "Moltres": "มอลเทรส",
        "Dratini": "ดราทินี่",
        "Dragonair": "ดรากอนแอร์",
        "Dragonite": "ดรากอนไนท์",
        "Mewtwo": "มิวทู",
        "Mew": "มิว"
    },
    "PokemonGen2": {
        "Chikorita": "ชิกอริตะ",
        "Bayleef": "เบย์ลีฟ",
        "Meganium": "เมกะเนียม",
        "Cyndaquil": "ไซน์แดควิล",
        "Quilava": "ควิลาว่า",
        "Typhlosion": "ไทเฟลอชัน",
        "Totodile": "โทโตไดล์",
        "Croconaw": "โครโคเนา",
        "Feraligatr": "เฟอราริกาเตอร์",
        "Sentret": "เซนเทรท",
        "Furret": "เฟอร์เรท",
        "Hoothoot": "ฮูทฮุต",
        "Noctowl": "น็อกทาวล์",
        "Ledyba": "เลดีบา",
        "Ledian": "เลเดียน",
        "Spinarak": "สปินารัค",
        "Ariados": "แอเรียดอส",
        "Crobat": "โครแบต",
        "Chinchou": "ชินชู",
        "Lanturn": "แลนเทิร์น",
        "Pichu": "ปิชุ",
        "Cleffa": "เคลฟฟ่า",
        "Igglybuff": "อิกลีบัฟ",
        "Togepi": "โทเกะปิ",
        "Togetic": "โทเกติค",
        "Natu": "นาตู",
        "Xatu": "ซาตู",
        "Mareep": "มารีป",
        "Flaaffy": "ฟลาฟฟี่",
        "Ampharos": "แอมเฟรอส",
        "Bellossom": "เบลอสซอม",
        "Marill": "มาริลล์",
        "Azumarill": "อะซูมาริลล์",
        "Sudowoodo": "ซูโดวูดโด",
        "Politoed": "โปลิโตเอ็ด",
        "Hoppip": "ฮอปปิป",
        "Skiploom": "สคิปลูม",
        "Jumpluff": "จัมพลัฟ",
        "Aipom": "ไอพอม",
        "Sunkern": "ซันเคิร์น",
        "Sunflora": "ซันฟลอร่า",
        "Yanma": "ยันม่า",
        "Wooper": "วูเปอร์",
        "Quagsire": "ควากไซร์",
        "Espeon": "เอสเปียน",
        "Umbreon": "อัมเบรอน",
        "Murkrow": "มอร์คราว",
        "Slowking": "สโลว์คิง",
        "Misdreavus": "มิสเดรฟัส",
        "Unown": "อูนาวน์",
        "Wobbuffet": "วอบบัฟเฟต",
        "Girafarig": "จิราฟาริก",
        "Pineco": "ไพน์โค",
        "Forretress": "ฟอร์เรสเทรส",
        "Dunsparce": "ดันสปาร์ซ",
        "Gligar": "กลิกการ์",
        "Steelix": "สตีลิกซ์",
        "Snubbull": "สนับบล์",
        "Granbull": "แกรนบล์",
        "Qwilfish": "ควิลฟิช",
        "Scizor": "ไซเซอร์",
        "Shuckle": "ชัคเคิล",
        "Heracross": "เฮอราครอส",
        "Sneasel": "สเนสเซล",
        "Teddiursa": "เท็ดดี้เออร์ซ่า",
        "Ursaring": "อูร์ซาริง",
        "Slugma": "สลักม่า",
        "Magcargo": "แมกคาร์โก",
        "Swinub": "สวินับ",
        "Piloswine": "ไพลอสไวน์",
        "Corsola": "คอร์ซาลา",
        "Remoraid": "รีโมรอยด์",
        "Octillery": "อ็อกทิลเลอรี",
        "Delibird": "เดลิเบิร์ด",
        "Mantine": "แมนไทน์",
        "Skarmory": "สคาร์โมรี",
        "Houndour": "ฮาวน์ดัวร์",
        "Houndoom": "ฮาวน์ดุม",
        "Kingdra": "คิงดร้า",
        "Phanpy": "ฟานพี",
        "Donphan": "ดอนฟาน",
        "Porygon2": "พอร์กิกัน 2",
        "Stantler": "สแตนท์เลอร์",
        "Smeargle": "สมียร์กล์",
        "Tyrogue": "ไทโรเกะ",
        "Hitmontop": "ฮิตมอนท็อป",
        "Smoochum": "สมูชัม",
        "Elekid": "อิเล็กคิด",
        "Magby": "แมกบี้",
        "Miltank": "มิลค์แทนค์",
        "Blissey": "บลิสซีย์",
        "Raikou": "ไรโก",
        "Entei": "เอนไท",
        "Suicune": "ซุยคูน์",
        "Larvitar": "ลาร์วิตาร์",
        "Pupitar": "พูปิตาร์",
        "Tyranitar": "ไทแรนนิทาร์",
        "Lugia": "ลูเกีย",
        "Ho-Oh": "โฮ-โอห์"
    },
    "Sports": {
        "Sport": "กีฬา",
        "Badminton": "แบดมินตัน",
        "Baseball": "เบสบอล",
        "Basketball": "บาสเก็ทบอล",
        "Bowling": "โบว์ลิ่ง",
        "Football": "ฟุตบอล",
        "Golf": "กอล์ฟ",
        "Rugby": "รักบี้",
        "Tennis": "เทนนิส",
        "Volleyball": "วอลเลย์บอล",
        "Archery": "ยิงธนู",
        "Athletics": "กรีฑา",
        "Boxing": "ต่อยมวย",
        "Cricket": "คริกเก็ต",
        "Cycling": "ปั่นจักรยาน",
        "Darts": "ปาเป้า",
        "Fencing": "ฟันดาบ",
        "Fishing": "ตกปลา",
        "Gymnastics": "ยิมนาสติก",
        "Handball": "แฮนด์บอล",
        "Hockey": "ฮอกกี้",
        "Judo": "ยูโด",
        "Polo": "โปโล",
        "Karate": "คาราเต้",
        "Running": "วิ่งแข่ง",
        "Sailing": "แข่งเรือใบ",
        "Softball": "ซอฟต์บอล",
        "Shooting": "ยิงปืน",
        "Skateboarding": "สเกตบอร์ด",
        "Skating": "สเกต",
        "Skiing": "สกี",
        "Sqaush": "สควอช",
        "Snooker": "สนุกเกอร์",
        "Snowboarding": "สโนว์บอร์ด",
        "Swimming": "ว่ายน้ำ",
        "Taekwondo": "เทควันโด",
        "Wrestling": "มวยปล้ำ",
        "Surfing": "กีฬาโต้คลื่น",
        "Rowing": "การพายเรือ",
        "Marathon": "วิ่งมาราธอน",
        "Hiking": "เดินป่า",
        "Canoeing": "พายเรือแคนู",
        "Aerobics": "แอโรบิก",
        "Winner": "ผู้ชนะ",
        "Loser": "ผู้แพ้",
        "Opponent": "ฝ่ายตรงข้าม",
        "Spectator": "ผู้ชม",
        "Defeat": "พ่ายแพ้",
        "Referee": "กรรมการ",
        "Injury": "บาดเจ็บ"
    }
}