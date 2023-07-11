import pygame
from settings import import_sprite

class Bird(pygame.sprite.Sprite):
	def __init__(self, pos, img_size):
		super().__init__()
		self.bird_img = import_sprite("assets/bird")
		self.frame_index = 0
		self.animation_delay = 3
		self.image = self.bird_img[self.frame_index]
		self.image = pygame.transform.scale(self.image, (img_size, img_size))
		self.mask = pygame.mask.from_surface(self.image)
		self.rect = self.image.get_rect(topleft = pos)

	# adds the spinning effect to the Blade trap
	def update(self):
		sprites = self.bird_img
		sprite_index = (self.frame_index // self.animation_delay) % len(sprites)
		self.image = sprites[sprite_index]
		self.frame_index += 1
		self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
		self.mask = pygame.mask.from_surface(self.image)
		if self.frame_index // self.animation_delay > len(sprites):
			self.frame_index = 0