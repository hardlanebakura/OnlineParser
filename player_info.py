import requests
from log_config import logging
from mongo_collections import DatabaseAtlas
from operator import itemgetter
from data import data
from subsidiary_functions import *
from player import Player
from find_match_stats import fms
from collections import OrderedDict
import math

def get_player_winrate(player):

    # for bugged matched in matchonse 'hero_id' will be 0, this must be accounted for
    matches_by_player = [match for match in player["matches"] if match["hero_id"] != 0]

    won_matches = 0
    lost_matches = 0

    for match in matches_by_player:
        match["player_slot"] = data["player_slots"][match["player_slot"]]
        match["hero_name"] = DatabaseAtlas.find("heroes", {"id": match["hero_id"]})["localized_name"]
        # logging.info(match)
        # player radiant
        if match["player_slot"] < 6:
            if match["radiant_win"] == True:
                won_matches += 1
            else:
                lost_matches += 1

        # player dire
        else:
            if match["radiant_win"] == True:
                lost_matches += 1
            else:
                won_matches += 1

    winrate = str(round((won_matches / len(matches_by_player)) * 100, 2)) + "%"

    player["won_matches"] = won_matches
    player["lost_matches"] = lost_matches
    player["winrate"] = winrate

    return player

def get_player_regions(player):

    logging.info(player)
    if not isinstance(player, dict):
        raise TypeError("Expected dict input")
    for region_id in list(player):
        for region in data["regions"]:
            if region_id == data["regions"][region]["region"]:
                player[data["regions"][region]["alt"]] = player[data["regions"][region]["region"]]
                del player[data["regions"][region]["region"]]
                get_winrate(player[data["regions"][region]["alt"]])
    player = dict(sorted(player.items(), key=lambda i: (i[1]["games"]) , reverse = True))
    logging.info(player)
    return player

def get_player_gamemodes(player):

    if not isinstance(player, dict):
        raise TypeError("Expected dict input")
    for gamemode_id in list(player):
        for gamemode in data["gamemodes"]:
            if int(gamemode_id) == gamemode:
                player[data["gamemode_alts"][data["gamemodes"][int(gamemode_id)]]] = player[gamemode_id]
                del player[gamemode_id]
                get_winrate(player[data["gamemode_alts"][data["gamemodes"][int(gamemode_id)]]])

    #merging All Pick with All Draft
    if "All Draft" in player:
        if "All Pick" in player:
            player["All Pick"]["games"] = player["All Pick"]["games"] + player["All Draft"]["games"]
            player["All Pick"]["win"] = player["All Pick"]["win"] + player["All Draft"]["win"]
            player["All Pick"]["winrate"] = str(round(((player["All Pick"]["win"] / player["All Pick"]["games"]) * 100), 2)) + "%"
            del player["All Draft"]
        else :
            player["All Pick"] = {}
            player["All Pick"]["games"] = player["All Draft"]["games"]
            player["All Pick"]["win"] = player["All Draft"]["win"]
            player["All Pick"]["winrate"] = str(round(((player["All Pick"]["win"] / player["All Pick"]["games"]) * 100), 2)) + "%"
            del player["All Draft"]

    player = dict(sorted(player.items(), key=lambda i: (i[1]["games"]), reverse=True))
    return player

def get_lane_roles(player):

    if not isinstance(player, dict):
        raise TypeError("Expected dict input")
    for role_id in list(player):
        for role in data["roles"]:
            if int(role_id) == role:
                player[data["roles"][int(role_id)]["lane"]] = player[role_id]
                del player[role_id]
                player[data["roles"][int(role_id)]["lane"]]["winrate"] = str(round((player[data["roles"][int(role_id)]["lane"]]["win"] / player[data["roles"][int(role_id)]["lane"]]["games"] * 100), 2)) + "%"

    return player

def get_radiant_dire(player):

    for side_id in list(player):
        if int(side_id) == 0:
            player["Radiant"] = player[side_id]
            get_winrate(player["Radiant"])
            del player[side_id]
        else:
            player["Dire"] = player[side_id]
            get_winrate(player["Dire"])
            del player[side_id]

    player = dict(sorted(player.items(), key=lambda i: (i[1]["games"]), reverse=True))
    logging.info(player)
    logging.info(type(player))
    return player

def get_recent_matches_by_player(player):

    if not isinstance(player, list):
        raise TypeError("Expected list input")

    for recent_match in player:
        if recent_match["player_slot"] in range(5):
            if recent_match["radiant_win"] == True:
                recent_match["result"] = "Won Match"
            else:
                recent_match["result"] = "Lost Match"
        else:
            if recent_match["radiant_win"] == True:
                recent_match["result"] = "Lost Match"
            else:
                recent_match["result"] = "Won Match"
        recent_match["duration"] = str(math.floor(recent_match["duration"] / 60)) + ":" + str(recent_match["duration"] % 60)
        if int(recent_match["duration"].split(":")[1]) < 10:
            recent_match["duration"] = recent_match["duration"].split(":")[0] + "0" + recent_match["duration"].split(":")[1]
        recent_match["game_mode"] = get_gamemode(recent_match["game_mode"])
        recent_match["hero"] = DatabaseAtlas.find("heroes", {"id" : recent_match["hero_id"]})["localized_name"]
        recent_match["start_time"] = get_time(recent_match["start_time"])

    logging.info(player)
    logging.info(type(player))
    return player

def get_heroes_player(player):

    if not isinstance(player, list):
        raise TypeError("Expected list input")
    for hero in list(player):
        hero["hero"] = DatabaseAtlas.find("heroes", {"id": int(hero["hero_id"])})["localized_name"]
        if hero["games"] != 0:
            hero["winrate"] = str(round(((hero["win"] / hero["games"]) * 100), 2)) + "%"
            if hero["with_games"] > 0:
                hero["with_winrate"] = str(round(((hero["with_win"] / hero["with_games"]) * 100), 2)) + "%"
            if hero["against_games"] > 0:
                hero["against_winrate"] = str(round(((hero["against_win"] / hero["against_games"]) * 100), 2)) + "%"

    return player

def get_medal_player(player):
    if not isinstance(player, int):
        raise TypeError("Expected int input")
    if player < 1:
        raise ValueError("Expected greater than zero")
    logging.info(data["medals"])

    for mmr_requirement in data["medals"]:
        if (player > int(mmr_requirement)) == False:
            logging.info(list(data["medals"].values())[list(data["medals"].values()).index(data["medals"][mmr_requirement]) - 1])
            logging.info(list(data["medals"].values()).index(data["medals"][mmr_requirement]))
            return list(data["medals"].values())[list(data["medals"].values()).index(data["medals"][mmr_requirement]) - 1]

    return "Immortal"

#https://api.steampowered.com/IEconItems_570/GetPlayerItems/v0001/?language=en&key=A2EA604E9B9CB5CF0B75454D22E968DA&steamid=76561198118149906
#https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?key=A2EA604E9B9CB5CF0B75454D22E968DA&account_id=157884178?game_mode=1?num_results=700
#https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/?match_id=6533969552&key=A2EA604E9B9CB5CF0B75454D22E968DA
#https://sr.dotabuff.com/players/850522220
#http://cdn.dota2.com/apps/dota2/images/abilities/drow_ranger_frost_arrows_lg.png
#--proxy-headers


