class SolarSystem:
    def __init__(self, id, name, description, image, planets):
        self.id = id
        self.name = name
        self.description = description
        self.image = image
        self.planets = planets


class Planet:
    def __init__(self, id, name, description, image, distance):
        self.id = id
        self.name = name
        self.description = description
        self.image = image
        self.distance = distance