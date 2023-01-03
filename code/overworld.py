import sys
import pygame 
from game_data import levels
from support import import_folder
from decoration import Sky
from settings import screen_height, screen_width

class Overworld:
	def __init__(self,first_level,create_level,screen):
		#  Define colors
		self.BLACK = (0, 0, 0)
		self.WHITE = (255, 255, 255)
		self.GREEN = (0, 255, 0)
		# Load fonts
		self.font = pygame.font.Font('graphics/ui/ARCADEPI.TTF', 20)
		self.font_title = pygame.font.Font('graphics/ui/ARCADEPI.TTF', 50)
		self.arrow_image = pygame.image.load('graphics/ui/arrow.png')
		self.title_card = pygame.image.load("graphics/ui/title-card.png")
		self.create_level = create_level
		self.first_level = first_level

		# Render the menu options

		self.option_1 = self.font.render(" NEW GAME ", True, self.WHITE)
		self.option_2 = self.font.render(" QUIT ", True, self.WHITE)
		self.text_y = 420
		self.arrow_y = self.text_y - 20
		self.option = 0
		self.arrow_x = 420
		self.timer = 20
		self.alpha = 255

	# Main menu function
	def Draw(self, screen):
	# Run the main menu until the user quits or starts a game
		# Fill the screen with black
		screen.fill(pygame.Color(self.BLACK))

		# Draw the title card
		screen.blit(self.title_card, (0, 0))

		# Options

		option1_rect = self.option_1.get_rect(center=(screen_width/2, screen_height/2))
		screen.blit(self.option_1, (option1_rect.x,self.text_y))

		option2_rect = self.option_2.get_rect(center=(screen_width/2, screen_height/2))
		screen.blit(self.option_2, (option2_rect.x, self.text_y + 50))

		# Draw arrow
		screen.blit(self.arrow_image, (self.arrow_x,self.arrow_y))

		# Update the display
		pygame.display.update()


	def Change_Text_Color(self):
		if self.option == 0:
			self.option_2 = self.font.render(" QUIT ", True, self.WHITE)
			self.option_1 = self.font.render(" NEW GAME ", True, self.GREEN)
		else:
			self.option_1 = self.font.render(" NEW GAME ", True, self.WHITE)
			self.option_2 = self.font.render(" QUIT ", True, self.GREEN)
		

	def Update(self):
		# Check for user input
		keys = pygame.key.get_pressed()
		self.blip_sound = pygame.mixer.Sound('audio/effects/coin.wav')
		if keys[pygame.K_RETURN] and self.option == 0:
			self.create_level(self.first_level)
			self.blip_sound.play()
			print('enter pressed in 0')
		elif keys[pygame.K_RETURN] and self.option == 1:
			self.blip_sound.play()
			pygame.QUIT
			pygame.quit()
			sys.exit()
		elif keys[pygame.K_DOWN] and self.option == 0:
			self.blip_sound.play()
			self.option = 1
			self.arrow_x += 75
			self.arrow_y += 55
		elif keys[pygame.K_UP] and self.option == 1:
			self.blip_sound.play()
			self.option = 0
			self.arrow_x -= 75
			self.arrow_y += -55
		
		self.Change_Text_Color()