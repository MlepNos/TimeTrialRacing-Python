import image_collection
import image
import button

class ButtonCollection:

    def __init__(self, img_collection, screen_x, screen_y):
        img_collection = image_collection.ImageCollection()
        self.dict = {}
        self.screen_x = screen_x
        self.screen_y = screen_y

        for key in img_collection.dict:
            temp_button = button.Button(0, 0, img_collection.dict[key], 1)
            self.dict.update({key, temp_button})

    
    def set_btn_pos(self, btn, x, y):
        btn.rect.x = x
        btn.rect.y = y