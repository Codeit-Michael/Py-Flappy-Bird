import pygame

class Pipe(pygame.sprite.Sprite):
	def __init__(self, pos, width, height, is_flip):
		super().__init__()
		img_path = 'assets/terrain/pipe.png'
		self.image = pygame.image.load(img_path)
		self.image = pygame.transform.scale(self.image, (width, height))
		if is_flip:
			flipped_image = pygame.transform.flip(self.image, False, True)
			self.image = flipped_image
		self.rect = self.image.get_rect(topleft = pos)

	# update object position due to world scroll
	def update(self, x_shift):
		self.rect.x += x_shift