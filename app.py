from flask import Flask, render_template, abort
from data import load_systems_and_planets 

app = Flask(__name__)

systems, planets = load_systems_and_planets()


@app.route("/home")
def home():
    return render_template("home.html", systems=systems)


@app.route("/system/<int:system_id>")
def system(system_id):
    for system in systems:
        if system.id == system_id:
            return render_template(
                "system.html",
                system=system,
                planets=system.planets
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
