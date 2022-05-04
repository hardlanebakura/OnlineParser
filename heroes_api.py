import requests
from log_config import logging
from mongo_collections import DatabaseAtlas
from operator import itemgetter

response_heroes = requests.get("https://api.opendota.com/api/heroes").json()
response_heroes = sorted(response_heroes, key=itemgetter("localized_name"))
hero_names = [item["localized_name"] for item in DatabaseAtlas.findFields("heroes", {}, "localized_name")]
hero_popularities = DatabaseAtlas.findAll("hero_popularities", {})
hero_kdas = DatabaseAtlas.findAll("hero_kdas", {})

def add_hero_name(dict1):
    for hero in response_heroes:
        if hero["id"] == int(dict1["hero_id"]):
            dict1["hero"] = hero["localized_name"]
    return dict1

def find_best_allies(hero):
    return

def find_best_counterpick(enemy_heroes):
    hero_matchups_versus_enemy_heroes = []
    for hero in hero_names:
        d = {"hero":hero, "matchups":[]}
        for enemy_hero in enemy_heroes:
            hero_vs_enemy_heroes = DatabaseAtlas.findAll("counterpicks", {"hero":hero, "counterpick_for":enemy_hero})
            #if not matchup vs self
            if len(hero_vs_enemy_heroes) > 0:
                hero_vs_enemy_heroes = hero_vs_enemy_heroes[0]
                dict1 = {"versus":hero_vs_enemy_heroes["counterpick_for"], "impact":hero_vs_enemy_heroes["impact"], "advantage":hero_vs_enemy_heroes["advantage"]}
                d["matchups"].append(dict1)
        d["total"] = round(sum([float(item["advantage"][:-1]) for item in d["matchups"]]), 3)
        hero_matchups_versus_enemy_heroes.append(d)
    hero_matchups_versus_enemy_heroes = sorted(hero_matchups_versus_enemy_heroes, key = itemgetter("total"))
    logging.info(hero_matchups_versus_enemy_heroes)
    return hero_matchups_versus_enemy_heroes


def find_match_stats(match_id, me):
    response_match = requests.get("https://api.opendota.com/api/matches/{}".format(match_id)).json()
    match_heroes = [player["hero_id"] for player in response_match["players"]]
    heroes = []
    for hero in match_heroes:
        player = DatabaseAtlas.find("heroes", {"id" : hero})
        heroes.append(player["localized_name"])

    my_hero = heroes[me]
    radiant_heroes = heroes[:5]
    dire_heroes = heroes[-5:]
    counterpicks_for_radiant_heroes = []
    counterpicks_for_dire_heroes = []
    for hero in radiant_heroes:
        counterpicks_for_radiant_heroes.append([item for item in DatabaseAtlas.findAll("counterpicks", {"counterpick_for": hero})])
    for hero in dire_heroes:
        counterpicks_for_dire_heroes.append([item for item in DatabaseAtlas.findAll("counterpicks", {"counterpick_for": hero})])
    logging.info(radiant_heroes)
    logging.info(dire_heroes)
    logging.info("My hero: " + my_hero)
    my_hero_info = []
    #I am radiant
    for counterpicks_for_one_hero in counterpicks_for_dire_heroes:
        for counterpick in counterpicks_for_one_hero:
            if counterpick["hero"] == my_hero and counterpick["counterpick_for"] in dire_heroes:
                my_hero_info.append(counterpick)

    #I am dire
    for counterpicks_for_one_hero in counterpicks_for_radiant_heroes:
        for counterpick in counterpicks_for_one_hero:
            if counterpick["hero"] == my_hero and counterpick["counterpick_for"] in radiant_heroes:
                my_hero_info.append(counterpick)

    if me < 5:
        my_hero_info = my_hero_info[:5]
        find_best_counterpick(dire_heroes)
    else:
        my_hero_info = my_hero_info[-5:]
        find_best_counterpick(radiant_heroes)
    my_hero_info = sorted(my_hero_info, key = itemgetter("advantage"))
    logging.info(my_hero_info)

    match_winner = response_match["radiant_win"]
    if match_winner == True:
        match_winner = "Radiant"
    else:
        match_winner = "Dire"
    logging.info("Winner: " + match_winner)

#logging.info(response_heroes)

def popularity_and_winrate():
    popularities = sorted(hero_popularities, key = lambda d: float(d["hero_popularity"].split("%")[0]), reverse = True)
    kdas = sorted(hero_kdas, key = lambda d: float(d["hero_kda"].split("%")[0]), reverse = True)
    for i in range(len(kdas)):
        popularities[i]["rank"] = i + 1
        kdas[i]["rank"] = i + 1
    return popularities, kdas

def get_hero_info(hero):
    for response_hero in response_heroes:
        if response_hero["localized_name"] == hero:
            return response_hero

hero_popularities = popularity_and_winrate()[0]
hero_kdas = popularity_and_winrate()[1]
counterpicks = DatabaseAtlas.findAll("counterpicks", {})
