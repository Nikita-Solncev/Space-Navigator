from dataclasses import dataclass


@dataclass
class SolarSystem:
    id: int
    name: str
    description: str
    image: str
    planets: list
    

@dataclass
class Planet:
    id: int
    solar_system_id: int
    name: str
    description: str
    image: str
    distance: float