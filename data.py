import json
from log_config import logging
import yaml
import requests


data = {

    "player_slots" : {

        0: 1,
        1: 2,
        2: 3,
        3: 4,
        4: 5,
        128: 6,
        129: 7,
        130: 8,
        131: 9,
        132: 10

    },

    "lobby_types": {

        -1: "Invalid",
        0: "Public matchmaking",
        1: "Practice",
        2: "Tournament",
        3: "Tutorial",
        4: "Co - op with bots",
        5: "Team match",
        6: "Solo Queue matchmaking"

},

    "regions" : {
	"unspecified": {
		"region":"0",
		"latitude":"0",
		"longitude":"0",
		"display_name":"#dota_region_automatic",
		"alt":"Unspecified",
		"day_determinism_offset":"0"
	},

	"USWest": {
		"region":"1",
		"code":"eat",
		"matchgroup":"0",
		"latitude":"47.6052",
		"longitude":"-122.1700",
		"display_name":"#dota_region_us_west",
		"alt":"US West",
		"leaderboard_division":"americas",
		"weekendtourney_division":"north_america",
		"day_determinism_offset":"-21600"
	},

	"USEast": {
		"code":"iad",
		"region":"2",
		"matchgroup":"1",
		"latitude":"39.00622",
		"longitude":"-77.428599",
		"display_name":"#dota_region_us_east",
		"alt": "US East",
		"leaderboard_division":"americas",
		"weekendtourney_division":"north_america",
		"day_determinism_offset":"-21600"
	},
    "Europe":{
		"code":"fra",
		"region":"3",
		"matchgroup":"2",
		"latitude":"52.523405",
		"longitude":"13.4114",
		"display_name":"#dota_region_europe",
		"alt":"EU West",
		"leaderboard_division":"europe",
		"weekendtourney_division":"europe",
		"day_determinism_offset":"3600"
	},
    "Singapore": {
		"code":"sgp",
		"region":"5",
		"matchgroup":"3",
		"latitude":"1.283333",
		"longitude":"103.833333",
		"display_name":"#dota_region_singapore",
		"alt":"SE Asia",
		"leaderboard_division":"se_asia",
		"weekendtourney_division":"se_asia",
		"day_determinism_offset":"28800"
	},
    "Dubai":
	{
		"code":"dxb",
		"region":"6",
		"matchgroup":"13",
		"latitude":"25.25",
		"longitude":"55.3",
		"display_name":"#dota_region_dubai",
		"alt":"Dubai",
		"leaderboard_division":"se_asia",
		"day_determinism_offset":"14400"
	},
    "PerfectWorldTelecom": {
		"code":"pwt",
		"matchgroup":"11",
		"region":"12",
		"latitude":"31.2",
		"longitude":"121.5",
		"display_name":"#dota_region_pw_telecom_shanghai",
		"alt":"China TC Shanghai",
		"leaderboard_division":"china",
		"weekendtourney_division":"china",
		"day_determinism_offset":"28800"
	}, "PerfectWorldTelecomGuangdong":
	{
		"code":"pwg",
		"matchgroup":"17",
		"region":"17",
		"latitude":"23.1",
		"longitude":"113.3",
		"display_name":"#dota_region_pw_telecom_guangdong",
		"alt":"China TC Guandong",
		"leaderboard_division":"china",
		"weekendtourney_division":"china",
		"day_determinism_offset":"28800"
	}, "PerfectWorldTelecomZhejiang": {
		"code":"pwz",
		"matchgroup":"18",
		"region":"18",
		"latitude":"29.2",
		"longitude":"120.5",
		"display_name":"#dota_region_pw_telecom_zhejiang",
		"alt":"China TC Zhejiang",
		"leaderboard_division":"china",
		"weekendtourney_division":"china",
		"day_determinism_offset":"28800",
	}, "PerfectWorldTelecomWuhan":
	{
		"code":"pww",
		"matchgroup":"20",
		"region":"20",
		"latitude":"30.4",
		"longitude":"114.2",
		"display_name":"#dota_region_pw_telecom_wuhan",
		"alt":"China TC Wuhan",
		"leaderboard_division":"china",
		"weekendtourney_division":"china",
		"day_determinism_offset":"28800"
	}, "PerfectWorldUnicom":
	{
		"code":"pwu",
		"matchgroup":"12",
		"region":"13",
		"latitude":"39.913889",
		"longitude":"116.391667",
		"display_name":"#dota_region_pw_unicom",
		"alt":"China UC",
		"leaderboard_division":"china",
		"weekendtourney_division":"china",
		"day_determinism_offset":"28800",
	}, "PerfectWorldUnicomTianjin":
	{
		"code":"pwj",
		"matchgroup":"25",
		"region":"25",
		"latitude":"38.34",
		"longitude":"116.43",
		"display_name":"#dota_region_pw_unicom_tianjin",
		"alt":"China UC 2",
		"leaderboard_division":"china",
		"weekendtourney_division":"china",
		"day_determinism_offset":"28800"
	}, "Stockholm":
	{
		"code":"sto",
		"region":"8",
		"matchgroup":"7",
		"latitude":"55.75",
		"longitude":"37.616667",
		"display_name":"#dota_region_stockholm",
		"alt":"Russia",
		"leaderboard_division":"europe",
		"weekendtourney_division":"europe",
		"day_determinism_offset":"3600"
	}, "Brazil":
	{
		"code":"gru",
		"region":"10",
		"matchgroup":"5",
		"latitude":"-23.532891",
		"longitude":"-46.642251",
		"display_name":"#dota_region_brazil",
		"alt":"Brazil",
		"leaderboard_division":"americas",
		"weekendtourney_division":"south_america",
		"day_determinism_offset":"-10800"
	}, "Austria":
	{
		"code":"vie",
		"region":"9",
		"matchgroup":"8",
		"latitude":"48.1200",
		"longitude":"16.2200",
		"display_name":"#dota_region_austria",
		"alt":"EU East",
		"leaderboard_division":"europe",
		"weekendtourney_division":"europe",
		"day_determinism_offset":"3600"
	}, "Australia":
	{
		"code":"syd",
		"region":"7",
		"matchgroup":"9",
		"latitude":"-33.859972",
		"longitude":"151.211111",
		"display_name":"#dota_region_australia",
		"alt":"Australia",
		"leaderboard_division":"se_asia",
		"weekendtourney_division":"se_asia",
		"day_determinism_offset":"36000"
	}, "SouthAfrica":
	{
		"code":"jnb",
		"region":"11",
		"matchgroup":"10",
		"latitude":"-33.925278",
		"longitude":"18.423889",
		"display_name":"#dota_region_southafrica",
		"alt":"South Africa",
		"leaderboard_division":"europe",
		"day_determinism_offset":"7200"
	}, "Chile":
	{
		"code":"scl",
		"region":"14",
		"matchgroup":"14",
		"latitude":"-33.6682982",
		"longitude":"-70.363372",
		"display_name":"#dota_region_chile",
		"alt":"Chile",
		"leaderboard_division":"americas",
		"weekendtourney_division":"south_america",
		"day_determinism_offset":"-21600"
	}, "Peru":
	{
		"code":"lim",
		"region":"15",
		"matchgroup":"15",
		"latitude":"-12.0553442",
		"longitude":"-77.0451853",
		"display_name":"#dota_region_peru",
		"alt":"Peru",
		"leaderboard_division":"americas",
		"weekendtourney_division":"south_america",
		"day_determinism_offset":"-21600"
	}, "Argentina":
	{
		"code":"ar",
		"region":"38",
		"matchgroup":"6",
		"latitude":"-34.6037",
		"longitude":"-58.3816",
		"display_name":"#dota_region_argentina",
		"alt":"Argentina",
		"leaderboard_division":"americas",
		"weekendtourney_division":"south_america",
		"day_determinism_offset":"-21600"
	}, "India":
	{
		"code":"bom",
		"region":"16",
		"matchgroup":"16",
		"latitude":"18.58",
		"longitude":"72.49",
		"display_name":"#dota_region_india",
		"alt":"India",
		"leaderboard_division":"se_asia",
		"day_determinism_offset":"19800"
	}, "Japan":
	{
		"code":"tyo",
		"region":"19",
		"matchgroup":"19",
		"latitude":"35.7",
		"longitude":"139.7",
		"display_name":"#dota_region_japan",
		"alt":"Japan",
		"leaderboard_division":"se_asia",
		"day_determinism_offset":"32400"
	}, "Taiwan":
	{
		"code":"gtpe",
		"region":"37",
		"matchgroup":"21",
		"latitude":"25.4",
		"longitude":"121.31",
		"display_name":"#dota_region_taiwan",
		"alt":"Taiwan",
		"leaderboard_division":"se_asia",
		"day_determinism_offset":"28800"
	}
},

    "roles": {
        0: {
        "lane":"Unknown"
        },
        1: {
        "lane":"Safelane"
        },
        2: {
        "lane":"Midlane"
        },
        3: {
        "lane":"Offlane"
        },
        4: {
        "lane":"Jungle"
         },

    },

	"gamemode_alts": {
		"DOTA_GAMEMODE_NONE": "Unspecified",
		"DOTA_GAMEMODE_AP": "All Pick",
		"DOTA_GAMEMODE_CM": "Captains Mode",
		"DOTA_GAMEMODE_RD": "Random Draft",
		"DOTA_GAMEMODE_SD": "Single Draft",
		"DOTA_GAMEMODE_AR": "All Random",
		"DOTA_GAMEMODE_INTRO": "Intro",
		"DOTA_GAMEMODE_HW": "HW",
		"DOTA_GAMEMODE_REVERSE_CM": "RCM",
		"DOTA_GAMEMODE_XMAS": "Christmas",
		"DOTA_GAMEMODE_TUTORIAL": "Tutorial Match",
		"DOTA_GAMEMODE_MO": "MO",
		"DOTA_GAMEMODE_LP": "LP",
		"DOTA_GAMEMODE_POOL1": "POOL1",
		"DOTA_GAMEMODE_FH": "FH",
		"DOTA_GAMEMODE_CUSTOM": "Custom Match",
		"DOTA_GAMEMODE_CD": "Captains Draft",
		"DOTA_GAMEMODE_BD": "BD",
		"DOTA_GAMEMODE_ABILITY_DRAFT": "Ability Draft",
		"DOTA_GAMEMODE_EVENT": "Event Match",
		"DOTA_GAMEMODE_ARDM": "ARDM",
		"DOTA_GAMEMODE_1V1MID": "1v1 Mid",
		"DOTA_GAMEMODE_ALL_DRAFT": "All Draft",
	}
    
}

data_file = open("data/data.json")
json_data = json.load(data_file)
gamemodes = json_data["gamemodes"]
medals = json_data["medals"]
data["gamemodes"] = dict([(v, k) for k, v in gamemodes.items()])
data["medals"] = dict([(v, k) for k, v in medals.items()])

abilities_data_file = open("data/abilities.json")
abilities = json.load(abilities_data_file)
data["abilities"] = dict([(v, k) for k, v in abilities.items()])

items_for_heroes_data_file = open("data/items.json")
items_for_heroes = json.load(items_for_heroes_data_file)
data["items_for_heroes"] = items_for_heroes

lanes_for_heroes_data_file = open("data/data.json")
lanes_for_heroes = json.load(lanes_for_heroes_data_file)
data["lanes_for_heroes"] = lanes_for_heroes

talent_trees_data_file = open("data/talent.json")
talent_trees = json.load(talent_trees_data_file)
data["talent_trees"] = talent_trees

with open("data/talent_trees.yml", 'r') as talent_trees_code_file:
	talent_trees_code = yaml.safe_load(talent_trees_code_file)
	talent_trees_codes = {}

	for item in talent_trees_code:
		if len(talent_trees_code[item]) > 1 and talent_trees_code[item][0][:7] == "special":
			logging.info(talent_trees_code[item][1])
			talent_trees_codes[item] = talent_trees_code[item][1]

	data["talent_trees_code"] = talent_trees_codes

esports_regions = { "China":"cn", "Global":"global", "EU.png":"eu", "East EU.png":"east_eu", "North America":"na", "South America":"SA", "SEA":"SEA" }

data["esports_regions"] = {}
for esports_region in esports_regions:
	logging.info(esports_region)
	data_file = open("data/esports/{}_esports.json".format(esports_regions[esports_region]))
	data["esports_regions"][esports_region] = json.load(data_file)
	logging.info(data["esports_regions"])

def update_team_logos():
	response_teams = requests.get("https://api.opendota.com/api/teams").json()

	for item in data["esports_regions"]:
		for team in data["esports_regions"][item]:
			#teams with no logo
			if team["logo"] == "https://static.gosugamers.net/07/d9/d0/b63edb6b283f2c450e1fb650255dd2ff06d7bd856b2c89d08c102b668d.jpg":
				for response_team in response_teams:
					if response_team["name"] == team["name"]:
						team["logo"] = response_team["logo_url"]
				#logging.info(team["name"])
	for item in response_teams:
		logging.info(item)

update_team_logos()

