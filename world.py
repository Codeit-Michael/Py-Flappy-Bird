import pygame     
from pipe import Pipe
from settings import WIDTH, pipe_size, pipe_gap, pipe_pair_sizes
import random

class World:
	def __init__(self, screen):
		self.screen = screen
		self.world_shift = -2
		self.current_x = 0
		self.current_pipe = None
		self.pipes = pygame.sprite.Group()
		self.player = pygame.sprite.GroupSingle()
		self.add_pipe()
		self.start_game = False

	def add_pipe(self):
		pipe_pair_size = random.choice(pipe_pair_sizes)
		top_pipe_height, bottom_pipe_height = pipe_pair_size[0] * pipe_size, pipe_pair_size[1] * pipe_size

		pipe_top = Pipe((WIDTH, 0 - (bottom_pipe_height + pipe_gap)), pipe_size, 700, True)
		pipe_bottom = Pipe((WIDTH, top_pipe_height + pipe_gap), pipe_size, 700, False)
		self.pipes.add(pipe_top)
		self.pipes.add(pipe_bottom)
		self.current_pipe = pipe_top

	def scroll_x(self):
		if self.start_game:
			self.world_shift = -2
		else:
			self.world_shift = 0

	def add_gravity(self):
		pass

	def handle_collisions(self):
		pass

	def update(self):
		# trigger once user start to play, cancelled once user loss
		# self.scroll_x()

		if self.current_pipe.rect.centerx  == WIDTH // 2:
			self.add_pipe()
		
		self.pipes.update(self.world_shift)
		self.pipes.draw(self.screen)
