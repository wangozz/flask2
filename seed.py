from app import app
from models import db, Hero, HeroPower, Power
import random


power_list = [
  { "name": "super strength", "description": "gives the wielder super-human strengths" },
  { "name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed" },
  { "name": "super human senses", "description": "allows the wielder to use her senses at a super-human level" },
  { "name": "elasticity", "description": "can stretch the human body to extreme lengths" }
]

hero_list = [
  { "name": "Kamala Khan", "super_name": "Ms. Marvel" },
  { "name": "Doreen Green", "super_name": "Squirrel Girl" },
  { "name": "Gwen Stacy", "super_name": "Spider-Gwen" },
  { "name": "Janet Van Dyne", "super_name": "The Wasp" },
  { "name": "Wanda Maximoff", "super_name": "Scarlet Witch" },
  { "name": "Carol Danvers", "super_name": "Captain Marvel" },
  { "name": "Jean Grey", "super_name": "Dark Phoenix" },
  { "name": "Ororo Munroe", "super_name": "Storm" },
  { "name": "Kitty Pryde", "super_name": "Shadowcat" },
  { "name": "Elektra Natchios", "super_name": "Elektra" }
]


strength_list = ["Strong", "Weak", "Average"]

with app.app_context():
    Power.query.delete()
    Hero.query.delete()
    HeroPower.query.delete()

    heroes = []
    for hero in hero_list:
        ahero = Hero(name=hero["name"], super_name=hero["super_name"])
        heroes.append(ahero)
    db.session.add_all(heroes)

    powers = []
    for power in power_list:
        apower = Power(name=power["name"], description=power["description"])
        powers.append(apower)
    db.session.add_all(powers)

    strengths = []
    for strength in strength_list:
        astrength = HeroPower(
            strength=strength,
            hero_id=random.randint(1, len(heroes)),
            power_id=random.randint(1, len(powers)),
        )
        strengths.append(astrength)
    db.session.add_all(strengths) 

    db.session.commit()
