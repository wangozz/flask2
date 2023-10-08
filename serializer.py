from models import Hero, HeroPower, Power

def response_serializer2(heroes: Hero):
    response = []
    for hero in heroes:
        hero_dict = {
            "id":hero.id,
            "name":hero.name,
            "super_name":hero.super_name,
        }
        response.append(hero_dict)
    return response

def response_serializer1(powers: Power):
    response = []
    for power in powers:
        power_dict = {
            "id":power.id,
            "name":power.name,
            "description":power.description,
        }
        response.append(power_dict)
    return response

def response_serializer(hero_powers: HeroPower):
    response = []
    for hero_power in hero_powers:
        heropower_dict = {
            "id":hero_power.id,
            "strength":hero_power.strength,
            "power_id":hero_power.power_id,
            "hero_id":hero_power.hero_id,
        }
        response.append(heropower_dict)
    return response