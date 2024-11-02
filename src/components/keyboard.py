import keyboardlayout as kl
import keyboardlayout.pygame as klp
import pygame
import classes
# This is black magic, I don't know what I'm doing
def get_keyboard(resource:classes.Resource,is_hard:bool) -> klp.KeyboardLayout:
    key_size = 60
    keyboard_info = kl.KeyboardInfo(
        position=(20, 400),
        padding=2,
        color=(255,255,255),
    )
    key_info = kl.KeyInfo(
        margin=5,
        color=(255,255,255),
        txt_color=(255,255,255),
        txt_font=pygame.font.Font("static/font/Kanit-Regular.ttf", key_size//3),
        txt_padding=(key_size//6, key_size//10)
    )
    letter_key_size = (key_size, key_size)  # width, height
    keyboard_layout = klp.KeyboardLayout(
        kl.LayoutName.QWERTY,
        keyboard_info,
        letter_key_size,
        key_info
    )
    show_key = kl.KeyInfo(
        margin=5,
        color=resource.get_current_color(is_hard),
        txt_color=(255,255,255),  # invert grey
        txt_font=pygame.font.Font("static/font/Kanit-Regular.ttf", key_size//3),
        txt_padding=(key_size//6, key_size//10)
    )
    for i in range(97,123):
        keyboard_layout.update_key(get_key_from_ascii(keyboard_layout,i),show_key)
    return keyboard_layout

def used_key(layout:klp.KeyboardLayout,pressed_key:str):
    key_size = 60
    if not pressed_key:
        return
    number = ord(pressed_key.lower())
    grey = pygame.Color('grey')
    disable_key = kl.KeyInfo(
        margin=5,
        color=grey,
        txt_color=(255,255,255),  # invert grey
        txt_font=pygame.font.Font("static/font/Kanit-Regular.ttf", key_size//3),
        txt_padding=(key_size//6, key_size//10)
    )
    layout.update_key(get_key_from_ascii(layout,number),disable_key)

def get_key_from_ascii(layout:klp.KeyboardLayout,number:int):
    return layout.get_key(pygame.event.Event(pygame.KEYDOWN,{"key":number}))