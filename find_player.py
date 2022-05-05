import requests
from log_config import logging
from mongo_collections import DatabaseAtlas
from operator import itemgetter
from data import data
from player_info import *
from player import Player
import json
from timeit import timeit
import time

def find_player(player_id):

    if not (isinstance(player_id, int)):
        raise TypeError("Expected int input")

    player = requests.get("https://api.opendota.com/api/players/{}".format(player_id)).json()
    player_totals = requests.get("https://api.opendota.com/api/players/{}/totals".format(player_id)).json()
    player_counts = requests.get("https://api.opendota.com/api/players/{}/counts".format(player_id)).json()
    player_matches = requests.get("https://api.opendota.com/api/players/{}/matches".format(player_id)).json()
    player_heroes = requests.get("https://api.opendota.com/api/players/{}/heroes".format(player_id)).json()
    player_recent_matches = player_matches[:15]

    player["matches"] = player_matches
    player["totals"] = player_totals
    player["counts"] = player_counts

    logging.info(player["totals"])
    logging.info("1")

    logging.info(player["totals"][0])
    logging.info(player["totals"][0]["n"] == 0)
    #no player found
    if player["totals"][0]["n"] == 0:
        logging.info("There is no player with requested id")
        return None

    logging.info("1")
    get_player_winrate(player)
    player["regions"] = get_player_regions(player_counts["region"])
    player["gamemodes"] = get_player_gamemodes(player_counts["game_mode"])
    player["roles"] = get_lane_roles(player_counts["lane_role"])
    player["sides"] = get_radiant_dire(player_counts["is_radiant"])
    player["recent_matches"] = get_recent_matches_by_player(player_recent_matches)
    for hero in player_heroes:
        hero["last_played"] = get_time(hero["last_played"])
    player["heroes"] = get_heroes_player(player_heroes)
    player["medal"] = get_medal_player(player["mmr_estimate"]["estimate"])

    #for deployment
    player["avatar"] = player["profile"]["avatarfull"]
    player["name"] = player["profile"]["personaname"]

    logging.info("ASDASDASDASD")

    #logging.info(player)
    Player1 = Player(player)
    logging.info(Player1)
    #logging.info(player_heroes)

    logging.info("ASD")

    #return Player1
    #for deployment
    return player

