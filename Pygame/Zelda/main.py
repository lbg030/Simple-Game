import pygame, sys
import settings

class Game:
	def __init__(self):
		  
		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((settings.WIDTH,settings.HEIGTH))
		self.clock = pygame.time.Clock()
	
	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			self.screen.fill('black')
			pygame.display.update()
			self.clock.tick(settings.FPS)

if __name__ == '__main__':
	game = Game()
	game.run()