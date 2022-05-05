import itertools
import json

class Player(object):

    new_id = itertools.count()
    def __init__(self, player_info):
        self.id = player_info["profile"]["account_id"]
        self.name = player_info["profile"]["personaname"]
        self.avatar = player_info["profile"]["avatarfull"]
        self.matches = player_info["matches"]
        #self.won_matches = player_info["won_matches"]
        #self.lost_matches = player_info["lost_matches"]
        #self.winrate = player_info["winrate"]
        self.totals = player_info["totals"]
        self.counts = player_info["counts"]
        self.gamemodes = player_info["gamemodes"]
        self.regions = player_info["regions"]
        self.roles = player_info["roles"]
        self.sides = player_info["sides"]
        self.recent_matches = player_info["recent_matches"]
        self.heroes = player_info["heroes"]
        self.mmr = player_info["mmr_estimate"]["estimate"]
        self.medal = player_info["medal"]

    def __repr__(self):
        return "Player " + str(self.id)

