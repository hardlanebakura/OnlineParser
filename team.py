import re
import json
import itertools

class Team(object):

    new_id = itertools.count()
    def __init__(self, team_info):
        self.id = next(Team.new_id) + 1
        self.name = team_info["name"]
        self.rank_points = team_info["rank_points"]
        self.team_logo = team_info["logo"]
        self.prize_winning = team_info["prize_winning"]
        self.winrate = team_info["winrate"]
        self.wins = team_info["wins"]
        self.draws = team_info["draws"]
        self.losses = team_info["losses"]
        self.current_streak = team_info["current_streak"]
        self.recent_matches = []

        for recent_match_index in range(1, 4):
            if "recent_match_{}".format(recent_match_index) in team_info:
                self.recent_matches.append(team_info["recent_match_{}".format(recent_match_index)])

        self.players = team_info["players"]

    def __repr__(self):
        r = dict(self.__dict__)
        return self.name + ":" + str(r)