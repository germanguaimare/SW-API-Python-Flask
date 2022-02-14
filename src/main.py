"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Characters, Planets, Favorites, Vehicles


app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/users', methods=['GET'])
def getUsers():
    allUsers = User.query.all()
    allUsers = list(map(lambda x: x.serialize(), allUsers))
    return jsonify(allUsers), 200

@app.route('/users/favorites', methods=['GET'])
def getFavorites():
    allFavorites = Favorites.query.all()
    allFavorites = list(map(lambda x: x.serialize(), allFavorites))
    return jsonify(allFavorites), 200

@app.route('/people', methods=['GET'])
def get_people():
    allpeople = Characters.query.all()
    allpeople = list(map(lambda x: x.serialize(), allpeople))
    return jsonify(allpeople), 200

@app.route('/people/<int:char_id>', methods=['GET'])
def get_character(char_id):
    myChar = Characters.query.get(char_id)
    return jsonify(myChar.serialize()), 200

@app.route('/planets', methods=['GET'])
def get_allplanets():
    allplanets = Planets.query.all()
    allplanets = list(map(lambda x: x.serialize(), allplanets))
    return jsonify(allplanets), 200

@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    myPlanet = Planets.query.get(planet_id)
    return jsonify(myPlanet.serialize()), 200

@app.route('/vehicles', methods=['GET'])
def get_vehicles():
    allvehicles = Vehicles.query.all()
    allvehicles = list(map(lambda x: x.serialize(), allvehicles))
    return jsonify(allvehicles), 200

@app.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def add_favPlanet(planet_id):
    body = request.get_json()
    exists = Planets.query.get(planet_id) is not None
    if exists == True:
        user = body["user_id"]
        favPlanet = planet_id
        newFavPlanet = Favorites(
            userId = user,
            planetId = favPlanet
        )
        db.session.add(newFavPlanet)
        db.session.commit()
        return "Planeta favorito agregado", 200
    else:
        return "Ocurrió un error", 400

@app.route('/favorite/people/<int:people_id>', methods=['POST'])
def add_favChar(people_id):
    body = request.get_json()
    exists = Characters.query.get(people_id) is not None
    if exists == True:
        user = body["user_id"]
        favChar = people_id
        newFavChar = Favorites(
            userId = user,
            charId = favChar
        )
        db.session.add(newFavChar)
        db.session.commit()
        return "Personaje favorito agregado", 200
    else:
        return "Ocurrió un error", 400

@app.route('/favorite/vehicles/<int:vehicle_id>', methods=['POST'])
def add_favVehicle(vehicle_id):
    body = request.get_json()
    exists = Vehicles.query.get(vehicle_id) is not None
    if exists == True:
        user = body["user_id"]
        favVehicle = vehicle_id
        newFavVehicle = Favorites(
            userId = user,
            vehicleId = favVehicle
        )
        db.session.add(newFavVehicle)
        db.session.commit()
        return "Vehículo favorito agregado", 200
    else:
        return "Ocurrió un error", 400


@app.route('/favorite/planet/<int:planet_id>', methods=['DELETE'])
def del_favPlanet(planet_id):
    allFavorites = Favorites.query.all()
    allFavorites = list(map(lambda x: x.serialize(), allFavorites))
    for x in range(len(allFavorites)):
        if allFavorites[x]["Planet ID"] == planet_id:
            idToDelete = allFavorites[x]["ID of this Favorite"]
            Favorites.query.filter_by(id = idToDelete).delete()
            db.session.commit()
            return ("Borré el favorito " + str(allFavorites[x]["ID of this Favorite"]))

@app.route('/favorite/people/<int:people_id>', methods=['DELETE'])
def del_favPeople(people_id):
    allFavorites = Favorites.query.all()
    allFavorites = list(map(lambda x: x.serialize(), allFavorites))
    for x in range(len(allFavorites)):
        if allFavorites[x]["Character ID"] == people_id:
            idToDelete = allFavorites[x]["ID of this Favorite"]
            Favorites.query.filter_by(id = idToDelete).delete()
            db.session.commit()
            return ("Borré el favorito " + str(allFavorites[x]["ID of this Favorite"]))
        





    """
    body = request.get_json()
    user = body["user_id"]
    allFavorites = Favorites.query.all()
    allFavorites = list(map(lambda x: x.serialize(), allFavorites))
    allFavorites = jsonify(allFavorites)
    for i in allFavorites:
        print (i)

        if allFavorites[i]["Planet ID"] == planet_id and allFavorites[i]["Favorite of User"]:
            idToDelete = allFavorites[i]["ID of this Favorite"]
            print ("\n\n", idToDelete)
            return json.dumps(ideToDelete)
            break

   ## return json.dumps(idToDelete)

    exists = Favorites.query.get(planet_id) is not None
    if exists:
        favPlanet = Favorites.query.get(planet_id).get(id)
        db.session.delete(favPlanet)
        db.session.commit()
        return "Planeta favorito eliminado", 200
    else:
        return "Ocurrió un error", 400
"""
# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)

