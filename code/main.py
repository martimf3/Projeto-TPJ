import pygame, sys
from settings import * 
from level import Level
from overworld import Overworld
from ui import UI

class Game:
	def __init__(self):

		# game attributes
		self.max_level = 2
		self.max_health = 100
		self.cur_health = 100
		self.coins = 0
		
		# audio 
		self.level_bg_music = pygame.mixer.Sound('audio/level_music.wav')
		self.overworld_bg_music = pygame.mixer.Sound('audio/overworld_music.wav')

		# overworld creation

		self.overworld = Overworld(0,self.create_level, screen)
		self.status = 'overworld'
		self.overworld_bg_music.play(loops = -1)

		# user interface 
		self.ui = UI(screen)

	def create_level(self,current_level):
		self.level = Level(current_level,screen,self.create_overworld, self.create_level,self.change_health)
		self.status = 'level'
		self.overworld_bg_music.stop()
		self.level_bg_music.play(loops = -1)

	def create_overworld(self,current_level):
		self.overworld = Overworld(current_level,self.create_level,screen)
		self.status = 'overworld'
		self.overworld_bg_music.play(loops = -1)
		self.level_bg_music.stop()

	def change_health(self,amount):
		self.cur_health += amount
		if self.cur_health > 100:
			self.cur_health = 100

	def check_game_over(self):
		if self.cur_health <= 0:
			self.cur_health = 100
			self.coins = 0
			self.max_level = 0
			self.overworld = Overworld(0,self.create_level,screen)
			self.status = 'overworld'
			self.level = Level(self.current_level)
			self.level_bg_music.stop()
			self.overworld_bg_music.play(loops = -1)

	def run(self):
		if self.status == 'overworld':
			self.overworld.Draw(screen)
			self.overworld.Update()
		else:
			self.level.run()
			self.ui.show_health(self.cur_health,self.max_health)
			self.check_game_over()

# Pygame setup
pygame.init()
pygame.display.set_caption("Scraggle: Get the Diamond to Win!")
game_icon = pygame.image.load('graphics/ui/icon.png')
pygame.display.set_icon(game_icon)
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
game = Game()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
	game.run()
	
	pygame.display.update()
	
	clock.tick(60)