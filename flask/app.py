from flask import Flask, render_template

app = Flask(__name__)

"""Information regarding the Pets in the System."""
pets = [
    {"id": 1, "name": "Nelly", "age": "5 weeks",
        "bio": "I am a tiny kitten rescued by the good people at Paws Rescue Center. I love squeaky toys and cuddles."},
    {"id": 2, "name": "Yuki", "age": "8 months",
     "bio": "I am a handsome gentle-cat. I like to dress up in bow ties."},
    {"id": 3, "name": "Basker", "age": "1 year",
     "bio": "I love barking. But, I love my friends more."},
    {"id": 4, "name": "Mr. Furrkins", "age": "5 years", "bio": "Probably napping."},
]


@app.route("/")
def home():
    return render_template("home.html", pets=pets)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/details/<int:pet_id>")
def pet_details(pet_id):
    """View function for Showing Details of Each Pet."""
    pet = next((pet for pet in pets if pet["id"] == pet_id), None)
    if pet is None:
        abort(404, description="No Pet was Found with the given ID")
    return render_template("details.html", pet=pet)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
