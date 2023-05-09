import pygame_menu
import os
import image

class ImageCollection:
    def __init__(self, path, substring="", alpha=False, scale=False, scale_val=1.0):
        self.dict = {}
        self.load_images(path, substring, alpha, scale, scale_val)
    
    def load_images(self, path, substring="", alpha=0, scale=False, scale_val=1.0):
        directory = os.fsencode(path)

        for file in os.listdir(directory):
            file_name = os.fsdecode(file)
            img_path = path + "/" + file_name

            if file_name.endswith(".jpg") or file_name.endswith(".png"):
                # Add all files or specific files depending on the contains_str argument
                #-----------------------------------------------------------------------
                if substring == "" or (substring != "" and substring in file_name):
                    self.add_image(file_name, img_path, alpha, scale, scale_val)
                
    def add_image(self, file_name, img_path, alpha, scale, scale_val):
        # Remove extension for dictionary entry name and add image to dictionary
        #-----------------------------------------------------------------------
        dict_entry_name = file_name.removesuffix(".jpg").removesuffix(".png")
        self.dict.update({dict_entry_name: image.Image(img_path, alpha, scale, scale_val)})

    def convert_to_base_images(self):
        for key in self.dict:
            self.dict[key] = pygame_menu.BaseImage(self.dict[key].path)