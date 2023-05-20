from flask import Flask, render_template, abort
from data import load_solar_systems_and_planets 

app = Flask(__name__)

solar_systems, planets = load_solar_systems_and_planets()


@app.route("/home")
def home():
    return render_template("home.html", solar_systems=solar_systems)


@app.route("/solar_system/<int:solar_system_id>")
def system(solar_system_id):
    for solar_system in solar_systems:
        if solar_system.id == solar_system_id:
            return render_template(
                "system.html",
                solar_system=solar_system,
                planets=solar_system.planets
            )
    abort(404)


@app.route("/planet/<int:planet_id>")
def planet(planet_id):
    for planet in planets:
        if planet.id == planet_id:
            return render_template("planet.html", planet=planet, planets=planets)
    abort(404)


if __name__ == "__main__":
    app.run(port=5012, debug=True)
