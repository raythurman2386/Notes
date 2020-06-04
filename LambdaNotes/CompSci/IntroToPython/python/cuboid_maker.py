class CuboidMaker:
    def __init__(self, length, width, height):
        super().__init__()
        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

    def surface_area(self):
        return 2 * (self.length * self.width + self.length * self.height + self.width * self.height)


class CubeMaker(CuboidMaker):
    def __init__(self, length, width, height):
        super().__init__(length, width, height)

    def cube_surface_area(self):
        return 6 * (self.length * self.width)


cuboid = CuboidMaker(4, 5, 5)
cube = CubeMaker(4, 4, 4)

print(cuboid.volume())
print(cuboid.surface_area())

print(cube.volume())
print(cube.cube_surface_area())
