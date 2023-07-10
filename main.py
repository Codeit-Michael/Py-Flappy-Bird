import pygame, sys
from settings import WIDTH, HEIGHT
from world import World

pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

class Main:
	def __init__(self, screen):
		self.screen = screen
		self.player_color = pygame.Color("darkorange")

	def main(self):
		world = World(screen)
		while True:
			screen.fill("white")

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			world.update()
			pygame.display.update()

if __name__ == "__main__":
	play = Main(screen)
	play.main()

