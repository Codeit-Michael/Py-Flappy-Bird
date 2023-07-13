import pygame
from settings import WIDTH, HEIGHT

pygame.font.init()

class GameIndicator:
	def __init__(self, screen):
		self.screen = screen
		self.font_size  = 60
		self.font = pygame.font.SysFont('Bauhaus 93', self.font_size)
		self.message_color = pygame.Color("white")

	def show_score(self, int_score):
		bird_score = str(int_score)
		score = self.font.render(bird_score, True, self.message_color)
		self.screen.blit(score,((WIDTH//2) - (self.font_size * len(bird_score) // 2), 50))

	def instructions(self):
		pass

	def game_over_message(self):
		pass