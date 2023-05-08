import pygame
import car
import time

import math
import scene

from utils import scale_image, blit_rotate_center
from datetime import datetime

class GameController:
    def __init__(self, player_car, scene, images):
        self.player_car = player_car
        self.scene = scene
        self.images = images
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.win_width, self.win_height = self.scene.track_image.get_size()
        self.win = pygame.display.set_mode((self.win_width, self.win_height))
        pygame.display.set_caption("Racing Game!")

    # Draw all images, car and update display
    #----------------------------------------
    def draw(self):
        
        for img, pos in self.images:
            self.win.blit(img, pos)
        
        self.player_car.draw(self.win)
        pygame.display.update()
    def move_player(self):
        keys = pygame.key.get_pressed()
        moved = False
        #if keys[pygame.K_9]:
             #self.player_car.reset(180, 200)

        if keys[pygame.K_a]:
            self.player_car.rotate(left=True)
        if keys[pygame.K_d]:
            self.player_car.rotate(right=True)
        if keys[pygame.K_w]:
            moved = True
            self.player_car.move_forward()
        if keys[pygame.K_s]:
            moved = True
            self.player_car.move_backward()
        if not moved:
            self.player_car.reduce_speed()
    
        
    def run(self,scene):
        run = True
        
        
        start_time = time.time()
        print(start_time)
        round = 0
        total_time=0
        while run:
            self.clock.tick(self.fps)
            
            self.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
            if self.player_car.collide(scene.track_mask) != None:
                self.player_car.bounce()
#if(round !=2):
            if self.player_car.collide(scene.checkpoint_mask) != None:
                scene.is_checkpoint = True
                
            if scene.is_checkpoint == True:
                finish_poi_collide = self.player_car.collide(scene.finish_mask, *(scene.finish_pos))
                if finish_poi_collide != None:
                        
                    round_time = time.time() - start_time
                    total_time= round_time + total_time
                    print("TIME :", round_time)
                    
                    scene.is_checkpoint = False
                    round = round+1
                    print("ROUND : " ,round)
                    print(finish_poi_collide)

            self.move_player()
    
 