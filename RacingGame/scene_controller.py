class SceneController:
    def __init__(self, player_car, scene):
        self.player_car = player_car
        self.scene = scene
        self.images = [(scene.background_grass_image,(0,0)),
                       (player_car.img, (0,0)),
                       (scene.track_image, (0,0)), 
                       (scene.finish_image, scene.finish_pos), 
                       (scene.track_border_image, (0,0)) ]

    def set_scene(self, scene):
        self.scene = scene
        self.set_images(scene)

    def set_player_car(self, player_car):
        self.player_car = player_car

    def set_images(self, scene):
        self.images =   [(scene.background_grass_image,(0,0)),
                       (self.player_car.img, (0,0)),
                       (scene.track_image, (0,0)), 
                       (scene.finish_image, scene.finish_pos), 
                       (scene.track_border_image, (0,0)) ]