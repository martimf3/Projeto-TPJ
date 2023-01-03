import sys
import pygame 
from game_data import levels
from support import import_folder
from decoration import Sky
from settings import screen_height, screen_width

class Node(pygame.sprite.Sprite):
	def __init__(self,pos,status,icon_speed,path):
		super().__init__()
		self.frames = import_folder(path)
		self.frame_index = 0
		self.image = self.frames[self.frame_index]
		if status == 'available':
			self.status = 'available'
		else:
			self.status = 'locked'
		self.rect = self.image.get_rect(center = pos)

		self.detection_zone = pygame.Rect(self.rect.centerx-(icon_speed/2),self.rect.centery-(icon_speed/2),icon_speed,icon_speed)

	def animate(self):
		self.frame_index += 0.15
		if self.frame_index >= len(self.frames):
			self.frame_index = 0
		self.image = self.frames[int(self.frame_index)]

	def update(self):
		if self.status == 'available':
			self.animate()
		else:
			tint_surf = self.image.copy()
			tint_surf.fill('black',None,pygame.BLEND_RGBA_MULT)
			self.image.blit(tint_surf,(0,0))

class Icon(pygame.sprite.Sprite):
	def __init__(self,pos):
		super().__init__()
		self.pos = pos
		self.image = pygame.image.load('graphics/overworld/hat.png').convert_alpha()
		self.rect = self.image.get_rect(center = pos)

	def update(self):
		self.rect.center = self.pos

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
		self.create_level = create_level
		self.first_level = first_level

		# Render the menu options
		self.title = self.font_title.render("NAME OF THE GAME", True, self.WHITE)
		self.option_1 = self.font.render(" START THE GAME ", True, self.WHITE)
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

		# Draw the menu options on the screen
		title_rect = self.title.get_rect(center=(screen_width/2, screen_height/2))
		screen.blit(self.title, title_rect)

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
			self.option_1 = self.font.render(" START THE GAME ", True, self.GREEN)
		else:
			self.option_1 = self.font.render(" START THE GAME ", True, self.WHITE)
			self.option_2 = self.font.render(" QUIT ", True, self.GREEN)
		

	def Update(self):
		# Check for user input
		keys = pygame.key.get_pressed()

		if keys[pygame.K_RETURN] and self.option == 0:
			self.create_level(self.first_level)
			print('enter pressed in 0')
		elif keys[pygame.K_RETURN] and self.option == 1:
			pygame.QUIT
			pygame.quit()
			sys.exit()
		elif keys[pygame.K_DOWN] and self.option == 0:
			self.option = 1
			self.arrow_x += 75
			self.arrow_y += 55
		elif keys[pygame.K_UP] and self.option == 1:
			self.option = 0
			self.arrow_x -= 75
			self.arrow_y += -55
		
		self.Change_Text_Color()