from dataclasses import dataclass


@dataclass
class System:
    id: int
    name: str
    description: str
    image: str
    planets: list
    

@dataclass
class Planet:
    id: int
    system_id: int
    name: str
    description: str
    image: str
    distance: str