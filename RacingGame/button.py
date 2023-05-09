import pygame

#button class
class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		x = x - (width/2)
		self.rect.topleft = (x, y)
		self.clicked = False

	def is_clicked(self):
		action = False

		mouse_pos = pygame.mouse.get_pos()

		# Check mouseover and clicked conditions
		#---------------------------------------
		if self.rect.collidepoint(mouse_pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		return action

	def draw(self, surface):
		surface.blit(self.image, (self.rect.x, self.rect.y))