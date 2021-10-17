import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from generate_sentence import Sentence
import pygame


class Interface:
    SCREEN_WIDTH: int = 800
    SCREEN_HEIGHT: int = 600
    text: str = 'test'
    white = (255, 255, 255)
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(
            (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.font = pygame.font.SysFont(pygame.font.get_default_font(), 50)
        fonts = pygame.font.get_fonts()
        self.input_box = pygame.Rect(100, 450, 205, 50)
        self.color = pygame.Color('green')
        self.color2 = 'green'
        pygame.display.flip()
        self.color_active = pygame.Color('dodgerblue2')

    def render(self):
        running = True
        active = False
        temp = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.input_box.collidepoint(event.pos):
                        # Toggle the active variable.
                        active = not active
                    else:
                        active = False
                if active:

                    self.color = self.color_active
                    self.color2 = self.color_active

                if not active:
                    self.color = 'green'
                    self.color2 = 'green'
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            print(self.text)
                            self.text = ''
                        elif event.key == pygame.K_BACKSPACE:
                            print(self.text)

                            self.text = self.text[:-1]
                            self.screen.fill('black')
                            print(self.text)
                        else:
                            self.text += event.unicode

            text_surface = self.font.render(self.text, True, 'green')
            self.screen.blit(text_surface, (400, 200))

            pygame.draw.rect(self.screen,'black',self.input_box,2)
            pygame.draw.line(self.screen, self.color2, (100, 450), (100, 500))
            pygame.display.update()


screen = Interface()
screen.render()
print('aa')
