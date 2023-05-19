import json
from models import SolarSystem, Planet


def load_data(file):
    with open(file, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    return data


def create_planet_objects(data):
    planets = []
    for solar_system in data["solar_systems"]:
        for planet in solar_system["planets"]:
            planets.append(
                Planet(
                    id=planet["id"],
                    solar_system_id=solar_system["id"],
                    name=planet["name"],
                    description=planet["description"],
                    image=planet["image"],
                    distance=planet["distance"],
                )
            )

    return planets


def create_solar_system_objects(data, planets):
    solar_systems = []
    for solar_system in data["solar_systems"]:
        solar_systems.append(
            SolarSystem(
                id=solar_system["id"],
                name=solar_system["name"],
                description=solar_system["description"],
                image=solar_system["image"],
                planets=[
                    planet
                    for planet in planets
                    if planet.solar_system_id == solar_system["id"]
                ],
            )
        )

    return solar_systems


def load_solar_systems_and_planets():
    data = load_data("data.json")
    planets = create_planet_objects(data)
    solar_systems = create_solar_system_objects(data, planets)

    return solar_systems, planets
