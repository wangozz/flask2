
from flask import Flask
from flask_restful import Api, Resource, reqparse
from models import db, Hero, HeroPower, Power
from flask_migrate import Migrate
from flask import request, app, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
from serializer import response_serializer2, response_serializer1, response_serializer



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)


class Index(Resource):
    def get(self):
        response = {
            "index": "Welcome to my Superheroes Api"
        }
        return make_response(jsonify(response))
api.add_resource(Index, '/')

class HeroesList(Resource):
    def get(self):
        heroes = Hero.query.all()
        response = response_serializer2(heroes)
        return make_response(jsonify(response), 200)

api.add_resource(HeroesList, '/heroes')

class HeroesId(Resource):
    def get(self, id):
        hero = Hero.query.filter_by(id=id).first()
        if hero:
            powers = [{"id": power.id, "name": power.name, "description": power.description} for power in hero.powers]
            response = {
                "id":hero.id,
                "name":hero.name,
                "super_name":hero.super_name,
                "powers": powers
            }
            return make_response(jsonify(response), 200 )
        else: 
            return make_response(jsonify({"error": "Hero not found"}), 404 ) 

api.add_resource(HeroesId, '/heroes/<int:id>')

class PowersList(Resource):
    def get(self):
        powers = Power.query.all()
        response = response_serializer1(powers)
        return make_response(jsonify(response), 200)

api.add_resource(PowersList, '/powers')

class PowersId(Resource):
    def get(self, id):
        power = Power.query.filter_by(id=id).first()
        if power:
            response = {
                "id":power.id,
                "name":power.name,
                "description":power.description,
            }
            return make_response(jsonify(response), 200 )
        else: 
            
            return (make_response(jsonify({"error": "Hero not found"}), 404 ))
    
    def patch(self, id):
        try:
            power = Power.query.filter_by(id=id).first()
            if power:
                for attr in request.get_json():
                    setattr(power, attr, request.get_json()[attr])
            db.session.add(power)
            db.session.commit()

            power_dict = {
                "id":power.id,
                "name":power.name,
                "description":power.description,
            }

            response = make_response(jsonify(power_dict), 200)

            return response
        except ValueError as e:
            response = make_response({"errors": e.args}, 200)

            return response 


api.add_resource(PowersId, '/powers/<int:id>')

class HeroPowerList(Resource):
    def get(self):
        hero_powers = HeroPower.query.all()
        response = response_serializer(hero_powers)
        return make_response(jsonify(response), 200)
    
    def post(self):
        try:
            data = request.get_json()
            hero_powers = HeroPower(
                strength = data["strength"],
                power_id = data["power_id"],
                hero_id = data["hero_id"]
            )
            db.session.add(hero_powers)
            db.session.commit()
            hero= Hero.query.filter_by(id=data["hero_id"]).first()
            powers = [{"id": power.id, "name": power.name, "description": power.description} for power in hero.powers]
            hero_dict = {
                "id":hero.id,
                "name":hero.name,
                "super_name":hero.super_name,
                "powers":powers
            }

            response = make_response(jsonify(hero_dict), 201)
            return response
        except ValueError as e:
            response = make_response(jsonify({"errors": str(e)}), 404 )
            return response

api.add_resource(HeroPowerList, '/hero_powers')


if __name__ == '__main__':
    app.run(port=5555)