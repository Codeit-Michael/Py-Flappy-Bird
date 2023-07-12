import pygame
from pipe import Pipe
from bird import Bird
from settings import WIDTH, HEIGHT, pipe_size, pipe_gap, pipe_pair_sizes
import random

class World:
	def __init__(self, screen):
		self.screen = screen
		self.world_shift = 0
		self.current_x = 0
		self.gravity = 0.1
		self.current_pipe = None
		self.pipes = pygame.sprite.Group()
		self.player = pygame.sprite.GroupSingle()
		self._generate_world()
		self.playing = False
		self.game_over = False

	def _generate_world(self):
		self._add_pipe()
		bird = Bird((100, HEIGHT//2), 30)
		self.player.add(bird)

	def _add_pipe(self):
		pipe_pair_size = random.choice(pipe_pair_sizes)
		top_pipe_height, bottom_pipe_height = pipe_pair_size[0] * pipe_size, pipe_pair_size[1] * pipe_size

		pipe_top = Pipe((WIDTH, 0 - (bottom_pipe_height + pipe_gap)), pipe_size, HEIGHT, True)
		pipe_bottom = Pipe((WIDTH, top_pipe_height + pipe_gap), pipe_size, HEIGHT, False)
		self.pipes.add(pipe_top)
		self.pipes.add(pipe_bottom)
		self.current_pipe = pipe_top

	def _scroll_x(self):
		if self.playing:
			self.world_shift = -2
		else:
			self.world_shift = 0

	def _apply_gravity(self, player):
		if self.playing or self.game_over:
			player.direction.y += self.gravity
			player.rect.y += player.direction.y

	def _handle_collisions(self):
		#look for collision
		bird = self.player.sprite
		if pygame.sprite.groupcollide(self.player, self.pipes, False, False) or bird.rect.bottom >= HEIGHT or bird.rect.top <= 0:
			self.playing = False
			self.game_over = True

	def update(self, player_event = None):
		if self.current_pipe.rect.centerx  <= WIDTH // 2:
			self._add_pipe()
		
		self.pipes.update(self.world_shift)
		self.pipes.draw(self.screen)

		self._apply_gravity(self.player.sprite)
		self._scroll_x()
		self._handle_collisions()

		self.player.update(player_event)
		self.player.draw(self.screen)