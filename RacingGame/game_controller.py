import pygame
import car
import time
import math
import scene

from utils import scale_image, blit_rotate_center
from datetime import datetime

class GameController:
    def __init__(self, player_car, images):
        self.player_car = player_car
        self.scene = scene.Scene("scenes/test", *(130, 250))
        self.images = images
        self.start_time = 0
        self.delta_time = 0
        self.best_time = 0
        self.fps = 60
        self.round = 0
        self.font = pygame.font.SysFont('arial.ttf', 18)
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
        self.draw_time()
        pygame.display.update()
    
    def set_best_time_and_round(self):
        if 0 == self.best_time:
            self.best_time = self.delta_time
        
        if self.best_time > self.delta_time:
            self.best_time = self.delta_time

        self.round = self.round + 1

    def draw_time(self):
        cur_time_img = self.font.render("{:.3f}".format(self.delta_time), True, pygame.color.Color(255, 255, 255))
        best_time_img = self.font.render("Best Time: {:.3f}    Round: {:.0f}".format(self.best_time, self.round), True, pygame.color.Color(255, 255, 255))
        self.win.blit(cur_time_img, (500,10))
        self.win.blit(best_time_img, (600, 10))
    
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
    
    def set_scene(self, scene, images):
        self.scene = scene
        self.images = images
        self.win_width, self.win_height = self.scene.track_image.get_size()
        
    def run(self):
        run = True
        
        self.start_time = time.time()
        current_time = time.time()

        round = 0
        total_time=0
        
        while run:
            current_time = time.time()
            self.delta_time = current_time - self.start_time
            self.clock.tick(self.fps)
            
            self.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
            if self.player_car.collide(self.scene.track_mask) != None:
                self.player_car.bounce()
            #if(round !=2):
            if self.player_car.collide(self.scene.checkpoint_mask) != None:
                self.scene.is_checkpoint = True
                
            if self.scene.is_checkpoint == True:
                finish_poi_collide = self.player_car.collide(self.scene.finish_mask, *(self.scene.finish_pos))
                if finish_poi_collide != None:
                    self.set_best_time_and_round()
                    total_time += self.delta_time

                    print("TIME :", self.delta_time)
                    
                    self.scene.is_checkpoint = False
                    round = round+1
                    print("ROUND : " ,round)
                    print(finish_poi_collide)

                    self.start_time = time.time()
            self.move_player()
    
 