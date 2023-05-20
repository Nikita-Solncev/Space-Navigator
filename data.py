import json
from models import System, Planet


def load_data(file):
    with open(file, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    return data


def create_planet_objects(data):
    planets = []
    for system in data["systems"]:
        for planet in system["planets"]:
            planets.append(
                Planet(
                    id=planet["id"],
                    system_id=system["id"],
                    name=planet["name"],
                    description=planet["description"],
                    image=planet["image"],
                    distance=planet["distance"],
                )
            )

    return planets


def create_system_objects(data, planets):
    systems = []
    for system in data["systems"]:
        systems.append(
            System(
                id=system["id"],
                name=system["name"],
                description=system["description"],
                image=system["image"],
                planets=[
                    planet
                    for planet in planets
                    if planet.system_id == system["id"]
                ],
            )
        )

    return systems


def load_systems_and_planets():
    data = load_data("data.json")
    planets = create_planet_objects(data)
    systems = create_system_objects(data, planets)

    return systems, planets
