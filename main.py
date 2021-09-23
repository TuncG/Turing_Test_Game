import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from generate_sentence import Sentence
import pygame


class Interface:
    SCREEN_WIDTH: int = 1000
    SCREEN_HEIGHT: int = 800
    text: str = 'test'
    white = (255, 255, 255)
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(
            (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.font = pygame.font.SysFont(pygame.font.get_default_font(), 72)
        fonts = pygame.font.get_fonts()
        print(len(fonts))
        for f in fonts:
            print(f)
        self.color = pygame.Color('green')
        pygame.display.flip()


    def render(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


            text_surface = self.font.render(self.text, True, self.color)
            self.screen.blit(text_surface, (50, 100))
            pygame.display.update()


screen = Interface()
screen.render()
print('aa')
