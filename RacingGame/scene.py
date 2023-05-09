import pygame
from utils import scale_image

class Scene:
    def __init__(self, scene_path, *finish_pos):
        scale_track = 1.0
        scale_finish = 1.0
        self.is_checkpoint = False
        
        self.rounds = 0
        self.track_image = scale_image(pygame.image.load("{0}/track.png".format(scene_path)), scale_track)
        self.icon = pygame.image.load("{0}/icon.png".format(scene_path))
        self.track_border_image =  scale_image(pygame.image.load("{0}/track-border.png".format(scene_path)), scale_track)
        self.finish_image =  scale_image(pygame.image.load("{0}/finish.png".format(scene_path)), scale_finish)
        self.track_mask = pygame.mask.from_surface(self.track_border_image)
        self.finish_mask = pygame.mask.from_surface(self.finish_image)
        self.finish_pos = (finish_pos[0], finish_pos[1])
        self.checkpoint_image = scale_image(pygame.image.load("{0}/checkpoint.png".format(scene_path)), scale_track)
        self.checkpoint_mask = pygame.mask.from_surface(self.checkpoint_image)
        self.background_grass_image = scale_image(pygame.image.load("{0}/terrain.jpg".format(scene_path)), 3.0)