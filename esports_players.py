import requests
from log_config import logging
from subsidiary_functions import delete_keys

response_players = requests.get("https://api.opendota.com/api/proPlayers").json()
response_teams = requests.get("https://api.opendota.com/api/teams").json()

team_names = [item["name"] for item in response_teams]

for team in response_teams:
    team["players"] = []

logging.info(response_teams[0])

for player in response_players:
    player = delete_keys(player, [2, 3, 7, 8, 9, 20, 21, 22])
    #logging.info(player)
    #if player["team_name"] in team_names:
        #response_teams["players"].append(player)
        #logging.info(response_teams["players"])

#logging.info(response_teams[0])

logging.info(len(response_players))
#logging.info(76561198135053965)
#logging.info(174788237 + 76561197960265728)

#for team in response_teams:
    #logging.info(team)

logging.info(len(response_teams))

#42735465



