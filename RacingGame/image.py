import pygame
import utils

class Image:
    def __init__(self, path, alpha=False, scale=False, scale_val=1.0):
        self.path = path
        self.surface = pygame.image.load(path).convert_alpha() if alpha else pygame.image.load(path)
        self.surface = utils.scale_image(self.surface, scale_val) if scale else self.surface

    def __call__(self):
        return self.surface