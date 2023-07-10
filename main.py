import pygame, sys
from settings import WIDTH, HEIGHT
from world import World

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

class Main:
	def __init__(self, screen):
		self.screen = screen
		self.bg_img = pygame.image.load('assets/terrain/bg.png')
		self.bg_img = pygame.transform.scale(self.bg_img, (WIDTH, HEIGHT))

	def main(self):
		world = World(screen)
		while True:
			self.screen.blit(self.bg_img, (0, 0))

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			world.update()
			pygame.display.update()

if __name__ == "__main__":
	play = Main(screen)
	play.main()
