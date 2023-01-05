import pygame, sys
from settings import * 
from level import Level
from overworld import Overworld
from game_over import Game_Over
from victory_menu import Victory
from ui import UI

class Game:
	def __init__(self):

		# game attributes
		self.WHITE = (255, 255, 255)
		self.max_level = 2
		self.max_health = 100
		self.cur_health = 100
		self.coins = 0
		self.font = pygame.font.Font('graphics/ui/ARCADEPI.TTF', 20)
		self.credits = self.font.render("A GAME BY MARTIMF3 AND REED OLIVEIRA", True, self.WHITE)
		
		# audio 
		self.level_bg_music = pygame.mixer.Sound('audio/level_music.wav')
		self.overworld_bg_music = pygame.mixer.Sound('audio/overworld_music.wav')
		self.victory_music = pygame.mixer.Sound('audio/diamonds.wav')
		self.game_over_music = pygame.mixer.Sound('audio/youdied.wav')

		# overworld creation

		self.overworld = Overworld(0,self.create_level, screen)
		self.status = 'credits'
		self.overworld_bg_music.play(loops = -1)

		# user interface 
		self.ui = UI(screen)

	def create_level(self,current_level):
		self.level = Level(current_level,screen,self.create_game_over, self.create_victory,self.change_health)
		self.status = 'level'
		pygame.mixer.stop()
		self.level_bg_music.play(loops = -1)

	def create_overworld(self,current_level):
		self.status = 'overworld'
		self.overworld = Overworld(current_level,self.create_level,screen)
		pygame.mixer.stop()
		self.overworld_bg_music.play(loops = -1)
	
	def create_game_over(self,current_level):
		self.status = 'game_over'
		self.game_over = Game_Over(current_level,self.create_level,self.create_overworld,screen)
		pygame.mixer.stop()
		self.game_over_music.play()
		
	def create_victory(self,current_level):
		self.status = 'victory'
		self.victory = Victory(current_level,self.create_level,self.create_overworld,screen)
		pygame.mixer.stop()
		self.victory_music.play(loops = -1)

	def create_cut_scene(self):
		credits_rect = self.credits.get_rect(center=(screen_width/2, screen_height/2))
		screen.blit(self.credits, credits_rect)
		pygame.display.flip()
		pygame.time.wait(3000)
		self.status = 'overworld'
		self.run()

	def change_health(self,amount):
		self.cur_health += amount
		if self.cur_health > 100:
			self.cur_health = 100

	def check_game_over(self):
		if self.cur_health <= 0:
			self.cur_health = 100
			self.coins = 0
			self.max_level = 0
			self.create_game_over(0)

	def run(self):
		if self.status == 'overworld':
			self.overworld.Draw(screen)
			self.overworld.Update()
		elif self.status == 'level':
			self.level.run()
			self.ui.show_health(self.cur_health,self.max_health)
			self.check_game_over()
		elif self.status == 'credits':
			self.create_cut_scene()
		elif self.status == 'game_over':
			self.game_over.Draw(screen)
			self.game_over.Update()
		elif self.status == 'victory':
			self.victory.Draw(screen)
			self.victory.Update()


# Pygame setup
pygame.init()
pygame.display.set_caption("Scraggle: Get the Diamond to Win! GAME OF THE YEAR EDITION")
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