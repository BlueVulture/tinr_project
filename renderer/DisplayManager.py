from pygame import *
import pygame as pg

class DisplayManager:
    def __init__(self, windowSize, caption, icon):
        self.winSize = windowSize
        self.caption = caption
        self.icon = icon

        self.screen = display.set_mode(self.winSize)
        display.set_caption(self.caption)
        display.set_icon(image.load("resources/meta/" + self.icon))


    def update(self):
        display.update()