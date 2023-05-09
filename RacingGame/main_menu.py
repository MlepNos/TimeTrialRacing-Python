import pygame
import button
import image
import image_collection
import time
import math
import car
import game_controller
import scene
import scene_collection
import scene_controller

from utils import scale_image, blit_rotate_center


pygame.init()
player_car = car.PlayerCar(7, 4, scale_image(pygame.image.load("images/red-car.png"), 0.6))
test_scene = scene.Scene("scenes/test", *(130, 250))
new_map_scene = scene.Scene("scenes/new_map", *(688, 300))
new_map_3_scene = scene.Scene("scenes/new_map_3", *(765, 300))
sc = scene_controller.SceneController(player_car, test_scene)
gc = game_controller.GameController(player_car, sc.images)

class MainMenu():
  def __init__(self, play_func, settings_func, exit_func, scene):
    # Not necessary, can be executed multiple times
    # Returns errors if something goes wrong
    #---------------------------------------
    pygame.init()

    # Load button and car images
    #---------------------------
    self.button_img_collection = image_collection.ImageCollection("images", "button", 1)
    self.car_img_collection = image_collection.ImageCollection("images", "car", 1)

    # Background image
    #-----------------
    bg_img = self.button_img_collection.dict["button_bg"]()
    centre_x = bg_img.get_width() / 2
    centre_y = bg_img.get_height() / 2

    # Create button instances
    #------------------------
    self.resume_button = button.Button(centre_x, centre_y - 100, self.button_img_collection.dict["button_resume"](), 1)
    self.options_button = button.Button(centre_x, centre_y, self.button_img_collection.dict["button_options"](), 1)
    self.quit_button = button.Button(centre_x, centre_y + 100, self.button_img_collection.dict["button_quit"](), 1)
    self.video_button = button.Button(centre_x, centre_y - 100, self.button_img_collection.dict["button_video"](), 1)
    self.audio_button = button.Button(centre_x, centre_y, self.button_img_collection.dict["button_audio"](), 1)
    self.keys_button = button.Button(centre_x, centre_y + 100, self.button_img_collection.dict["button_keys"](), 1)
    self.back_button = button.Button(centre_x, centre_y + 200, self.button_img_collection.dict["button_back"](), 1)

    # Create buttons for map selection in scene menu
    #-----------------------------------------------
    self.scene_col = scene_collection.SceneCollection("scenes")

    self.map_one_button = button.Button(centre_x, centre_y, new_map_scene.icon, 1.0)
    self.map_two_button = button.Button(centre_x - 100, centre_y, new_map_3_scene.icon, 1.0)
    self.map_three_button = button.Button(centre_x + 100, centre_y, test_scene.icon, 1.0)

    # Create buttons for car selection in car menu
    #---------------------------------------------
    self.red_car = button.Button(centre_x - 200, centre_y - 100, self.car_img_collection.dict["red-car"](), 1)
    self.white_car = button.Button(centre_x - 100, centre_y - 100, self.car_img_collection.dict["white-car"](), 1)
    self.purple_car = button.Button(centre_x, centre_y - 100, self.car_img_collection.dict["purple-car"](), 1)
    self.grey_car = button.Button(centre_x + 100, centre_y - 100, self.car_img_collection.dict["grey-car"](), 1)
    self.green_car = button.Button(centre_x + 200, centre_y - 100, self.car_img_collection.dict["green-car"](), 1)

    # Initialize members and callbacks
    #---------------------------------
    self.play_func = play_func
    self.settings_func = settings_func
    self.exit_func = exit_func
    self.pause_key = pygame.K_SPACE
    self.screen_width = bg_img.get_width()
    self.screen_height = bg_img.get_height()
    self.scene = scene
    self.game_paused = False
    self.menu_state = "main"
    
    self.font = pygame.font.SysFont('Raleway', 72, bold=True, italic=False)
    self.text_col = (255, 255, 255)

    self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
    pygame.display.set_caption("Main Menu")

  def draw_text(self, text, x, y):
    img = self.font.render(text, True, self.text_col)
    self.screen.blit(img, (x, y))
  
  def draw_option_screen(self):
    self.video_button.draw(self.screen)
    self.audio_button.draw(self.screen)
    self.keys_button.draw(self.screen)
    self.back_button.draw(self.screen)
  
  def draw_main_menu_screen(self):
    self.resume_button.draw(self.screen)
    self.options_button.draw(self.screen)
    self.quit_button.draw(self.screen)

  def draw_scene_menu(self):
    self.map_one_button.draw(self.screen)
    self.map_two_button.draw(self.screen)
    self.map_three_button.draw(self.screen)

  def draw_car_scene_menu(self):
    self.red_car.draw(self.screen)
    self.white_car.draw(self.screen)
    self.purple_car.draw(self.screen)
    self.grey_car.draw(self.screen)
    self.green_car.draw(self.screen)
    

  def run(self):
    run = True
    while run:

      self.screen.fill((120, 78, 91))   # Menu background color
      self.screen.blit(self.button_img_collection.dict["button_bg"].surface, (0, 0))

      if self.game_paused == False:
        if self.menu_state == "main":
          self.draw_main_menu_screen()

          # Handle the button clicks
          #-------------------------
          if self.resume_button.is_clicked():
            self.game_paused = False
            self.menu_state = "cars"
          if self.options_button.is_clicked():
            self.menu_state = "options"
          if self.quit_button.is_clicked():
            run = False
        
        if self.menu_state == "cars":
          self.draw_car_scene_menu()

          if self.red_car.is_clicked():
            self.menu_state = "scenes"
            player_car.img = scale_image(pygame.image.load("images/red-car.png"), 0.6)
          if self.white_car.is_clicked():
            self.menu_state = "scenes"
            player_car.img = scale_image(pygame.image.load("images/white-car.png"), 0.6)
          if self.purple_car.is_clicked():
            self.menu_state = "scenes"
            player_car.img = scale_image(pygame.image.load("images/purple-car.png"), 0.6)  
          if self.grey_car.is_clicked():
            self.menu_state = "scenes"
            player_car.img = scale_image(pygame.image.load("images/grey-car.png"), 0.6)
          if self.green_car.is_clicked():
            self.menu_state = "scenes"
            player_car.img = scale_image(pygame.image.load("images/green-car.png"), 0.6)

        if self.menu_state == "scenes":
          self.draw_scene_menu()
          if self.map_one_button.is_clicked():
            self.menu_state = "main"
            player_car.x = 725
            player_car.y = 300
            player_car.angle = 0
            player_car.vel = 0
            gc.round = 0
            sc.set_scene(new_map_scene)
            gc.set_scene(new_map_scene, sc.images)
            gc.run()
          if self.map_two_button.is_clicked():
            self.menu_state = "main"
            player_car.x = 800
            player_car.y = 300
            player_car.angle = 0
            player_car.vel = 0
            gc.round = 0
            sc.set_scene(new_map_3_scene)
            gc.set_scene(new_map_3_scene, sc.images)
            gc.run()
          if self.map_three_button.is_clicked():
            self.menu_state = "main"
            player_car.x = 180
            player_car.y = 250
            player_car.angle = 0
            player_car.vel = 0
            gc.round = 0
            sc.set_scene(test_scene)
            gc.set_scene(test_scene, sc.images)
            gc.run()

        if self.menu_state == "options":
          self.draw_option_screen()

          # Handle the button clicks
          #-------------------------
          if self.video_button.is_clicked():
            print("Video Settings")
          if self.audio_button.is_clicked():
            print("Audio Settings")
          if self.keys_button.is_clicked():
            print("Change Key Bindings")
          if self.back_button.is_clicked():
            self.menu_state = "main"
            print("Back clicked")
      else:
        self.draw_text("Press SPACE to resume", 160, 250)

      #event handler
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
            self.game_paused = True
        if event.type == pygame.QUIT:
          self.menu_state = "main"
          

      pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
  menu = MainMenu(gc.run, 0, 0, test_scene)
  menu.run()