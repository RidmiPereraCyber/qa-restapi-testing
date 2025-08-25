from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Create database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///travel.db"

db = SQLAlchemy(app)

class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Destination = db.Column(db.String(50), nullable=False)
    Country = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Float, nullable = False)

    def to_dict(self):
        return {
            "id" : self.id,
            "destination" : self.Destination,
            "country" : self.Country,
            "rating" : self.rating
        }
    
with app.app_context():
    db.create_all()

# Create Routes
@app.route("/")
def home():
    return jsonify({"message":"Welcome to the travel API"})

@app.route("/destinations", methods=["GET"])
def get_destinations():
    destinations = Destination.query.all()

    return jsonify([destination.to_dict() for destination in destinations])

@app.route("/destinations/<int:destination_id>", methods=["GET"])
def get_destination(destination_id):
  # destination = Destination.query.get(destination_id)
    destination = db.session.get(Destination, destination_id)
    if destination:
        return jsonify(destination.to_dict())
    else:
        return jsonify({"error" : "Destination not found!"}),404
                        
@app.route("/destinations", methods=["POST"])
def add_destination():
    data = request.get_json()

    new_destination = Destination(Destination=data["destination"],
                                  Country=data["country"],
                                  rating=data["rating"])

    db.session.add(new_destination)
    db.session.commit()

    return jsonify(new_destination.to_dict()), 201
 
@app.route("/destinations/<int:destination_id>", methods=["PUT"])
def update_destination(destination_id):
    data = request.get_json()

 # destination = Destination.query.get(destination_id)
    destination = db.session.get(Destination, destination_id)
    if destination:
        destination.Destination = data.get("destination", destination.Destination)
        destination.Country = data.get("country", destination.Country)
        destination.rating = data.get("rating", destination.rating)

        db.session.commit()

        return jsonify(destination.to_dict())
    else:
        return jsonify({"error":"Destination not found"}), 404
    
@app.route("/destinations/<int:destination_id>", methods=["DELETE"])
def delete_destination(destination_id):
  # destination = Destination.query.get(destination_id)
    destination = db.session.get(Destination, destination_id)
    if destination:
        db.session.delete(destination)
        db.session.commit()

        return jsonify({"message":"Destination was deleted"})
    else:
        return jsonify({"error":"Destination not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)