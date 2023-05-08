import pygame
import time
import math
import car
import game_controller
import scene
import scene_controller
from utils import scale_image, blit_rotate_center

player_car = car.PlayerCar(7, 4, scale_image(pygame.image.load("images/red-car.png"), 0.6))
test_scene = scene.Scene("scenes/test", *(130, 250))
sc = scene_controller.SceneController(player_car, test_scene)
gc = game_controller.GameController(player_car, test_scene, sc.images)

gc.run(test_scene)