from flask import Flask, render_template, abort
from models import SolarSystem, Planet
import json

with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

solar_systems = []
planets = []
for i in data["solar_systems"]:
    for j in i["planets"]:
        planets.append(
            Planet(
                id=j["id"],
                name=j["name"],
                description=j["description"],
                image=j["image"],
                distance=j["distance"],
            )
        )
    solar_systems.append(
        SolarSystem(
            id=i["id"],
            name=i["name"],
            description=i["description"],
            image=i["image"],
            planets=planets,
        )
    )


app = Flask(__name__)


@app.route("/home")
def home():
    return render_template("home.html", solar_systems=solar_systems)


@app.route("/solar_system/<int:solar_system_id>")
def system(solar_system_id):
    for solar_system in solar_systems:
        if solar_system.id == solar_system_id:
            solar_systems_planets = []
            for planet in planets:
                if str(planet.id)[0] == str(solar_system_id):
                    solar_systems_planets.append(planet)
            return render_template(
                "system.html",
                solar_system=solar_system,
                planets=solar_systems_planets,
                planet=planet,
            )
    abort(404)


@app.route("/planet/<int:planet_id>")
def planet(planet_id):
    for planet in planets:
        if planet.id == planet_id:
            return render_template("planet.html", planet=planet)
    abort(404)


if __name__ == "__main__":
    print(solar_systems)
    print(planets)
    app.run(port=5012, debug=True)
