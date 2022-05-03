import requests
from log_config import logging
from mongo_collections import DatabaseAtlas
from data import data
from operator import itemgetter
from subsidiary_functions import get_time

def find_gamemode(match_gamemode_id):
    if match_gamemode_id != 22:
        return data["gamemode_alts"][data["gamemodes"][match_gamemode_id]]
    else:
        return "All Pick"

def fms(match_id):
    #since match_id is larger than INT_MAX of 2^30 - 1 but Python will handle it as int
    if not isinstance(match_id, int):
        raise TypeError("Expected int input")
    try:
        response_match = requests.get("https://api.opendota.com/api/matches/{}".format(match_id)).json()
    except:
        logging.info("No match with selected ID")
        return None

    #some very old matches have bugged 'None' duration
    if "duration" not in response_match:
        return None
    if response_match["duration"] == None:
        return None
    match = response_match

    #match winner

    if response_match["radiant_win"] == True:
        match["winner"] = "Radiant"
    else:
        match["winner"] = "Dire"

    #logging.debug(match["players"])
    response_match["picks_bans"] = sorted(response_match["picks_bans"], key = itemgetter("order"))

    match["heroes"] = [DatabaseAtlas.find("heroes", {"id" : hero["hero_id"]})["localized_name"] for hero in response_match["players"]]
    match["banned_heroes"] = [{"hero":DatabaseAtlas.find("heroes", {"id" : hero["hero_id"]})["localized_name"], "team":hero["team"]} for hero in response_match["picks_bans"] if hero["is_pick"] == False]

    for hero in response_match["picks_bans"]:
        hero["hero"] = DatabaseAtlas.find("heroes", {"id" : hero["hero_id"]})["localized_name"]
        del hero["hero_id"]

    region = data["regions"]

    for region in data["regions"]:

        if "region" in response_match:
            if int(data["regions"][region]["region"]) == response_match["region"]:
                match["region"] = data["regions"][region]["alt"]
        else:
            match["region"] = data["regions"]["unspecified"]

    match["game_mode"] = find_gamemode(match["game_mode"])
    match["start_time"] = get_time(match["start_time"])

    #logging.info(match["picks_bans"])
    #for player in response_match["players"]:
        #logging.info(player)
    logging.info(match)
    logging.info(match["heroes"])
    return match


#fms(6524970162)