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
		self.title = self.font_title.render("SCRAGGLE", True, self.WHITE)
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
		
		#self.Cut_Scene(screen)

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
			self.option_1 = self.font.render(" NEW GAME ", True, self.GREEN)
		else:
			self.option_1 = self.font.render(" NEW GAME ", True, self.WHITE)
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
"""
	def Cut_Scene(self,screen):
		cut_scene_text = self.font.render("GAME MADE BY JOÃO E MARTIM", True, self.GREEN)
		cut_scene_text_rect = cut_scene_text.get_rect(center=(screen_width/2, screen_height/2))

		while self.alpha > 0:
			while self.timer > 0:
				self.timer -= 1
				if self.timer == 0:
					self.timer += 20
					# Reduce alpha each frame, but make sure it doesn't get below 0.
					self.alpha -= 4
					# Create a copy so that the original surface doesn't get modified.                
					txt_surf = cut_scene_text.copy()
					txt_surf.fill((255, 255, 255, self.alpha), special_flags=pygame.BLEND_RGBA_MULT)
					
					screen.blit(txt_surf, cut_scene_text_rect)
"""
	# Start the main menu

		# setup 
		#self.display_surface = surface 
		#self.max_level = max_level
		#self.current_level = start_level
		#self.create_level = create_level

		# movement logic
		#self.moving = False
		#self.move_direction = pygame.math.Vector2(0,0)
		#self.speed = 8

		# sprites 
		#self.setup_nodes()
		#self.setup_icon()
		#self.sky = Sky(8,'overworld')

		# time 
		#self.start_time = pygame.time.get_ticks()
		#self.allow_input = False
		#self.timer_length = 300
"""
	def setup_nodes(self):
		self.nodes = pygame.sprite.Group()

		for index, node_data in enumerate(levels.values()):
			if index <= self.max_level:
				node_sprite = Node(node_data['node_pos'],'available',self.speed,node_data['node_graphics'])
			else:
				node_sprite = Node(node_data['node_pos'],'locked',self.speed,node_data['node_graphics'])
			self.nodes.add(node_sprite)

	def draw_paths(self):
		if self.max_level > 0:
			points = [node['node_pos'] for index,node in enumerate(levels.values()) if index <= self.max_level]
			pygame.draw.lines(self.display_surface,'#a04f45',False,points,6)

	def setup_icon(self):
		self.icon = pygame.sprite.GroupSingle()
		icon_sprite = Icon(self.nodes.sprites()[self.current_level].rect.center)
		self.icon.add(icon_sprite)

	def input(self):
		keys = pygame.key.get_pressed()

		if not self.moving and self.allow_input:
			if keys[pygame.K_RIGHT] and self.current_level < self.max_level:
				self.move_direction = self.get_movement_data('next')
				self.current_level += 1
				self.moving = True
			elif keys[pygame.K_LEFT] and self.current_level > 0:
				self.move_direction = self.get_movement_data('previous')
				self.current_level -= 1
				self.moving = True
			elif keys[pygame.K_SPACE]:
				self.create_level(self.current_level)

	def get_movement_data(self,target):
		start = pygame.math.Vector2(self.nodes.sprites()[self.current_level].rect.center)
		
		if target == 'next': 
			end = pygame.math.Vector2(self.nodes.sprites()[self.current_level + 1].rect.center)
		else:
			end = pygame.math.Vector2(self.nodes.sprites()[self.current_level - 1].rect.center)

		return (end - start).normalize()

	def update_icon_pos(self):
		if self.moving and self.move_direction:
			self.icon.sprite.pos += self.move_direction * self.speed
			target_node = self.nodes.sprites()[self.current_level]
			if target_node.detection_zone.collidepoint(self.icon.sprite.pos):
				self.moving = False
				self.move_direction = pygame.math.Vector2(0,0)

	def input_timer(self):
		if not self.allow_input:
			current_time = pygame.time.get_ticks()
			if current_time - self.start_time >= self.timer_length:
				self.allow_input = True

	def run(self):
		self.input_timer()
		self.input()
		self.update_icon_pos()
		self.icon.update()
		self.nodes.update()

		self.sky.draw(self.display_surface)
		self.draw_paths()
		self.nodes.draw(self.display_surface)
		self.icon.draw(self.display_surface)
"""