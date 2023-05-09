import scene
import os

class SceneCollection:
    def __init__(self, path):
        self.dict = {}
        self.load_scenes(path)
    
    def load_scenes(self, path):
        directory = os.fsencode(path)

        for subdir, dirs, files in os.walk(directory):
            for dir in dirs:
                dir_path = path + "/" + os.fsdecode(dir)
                self.dict.update({dir_path: scene.Scene(dir_path, *(0,0))})
            
