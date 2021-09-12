from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

class Voxel(Button):
    def __init__(self, position = (0, 0, 0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = 0.5,
            texture = "white_cube",
            color = color.color(107, 191, random.uniform(0.9, 1)),
            highlight_color = color.lime
        )
    def input(self, key):
        if self.hovered:
            if key == "right mouse down":
                voxel = Voxel((self.position + mouse.normal))
            elif key == "left mouse down":
                destroy(self)
                
            

window = Ursina()

player = FirstPersonController()


for z in range(40):
    for x in range(40):
        voxel = Voxel((x,0,z))

window.run()