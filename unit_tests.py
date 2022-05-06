import unittest
from find_player import *
from find_match_stats import *
from subsidiary_functions import *

class TestModule(unittest.TestCase):

    def test_players_type_inputs(self):
        '''function should fail on wrong type inputs'''
        self.assertRaisesRegex(TypeError, "Expected int input", find_player, "a")
        self.assertRaisesRegex(TypeError, "Expected dict input", get_player_regions, "a")
        self.assertRaisesRegex(TypeError, "Expected dict input", get_player_gamemodes, "a")
        self.assertRaisesRegex(TypeError, "Expected dict input", get_lane_roles, "a")
        self.assertRaisesRegex(TypeError, "Expected list input", get_recent_matches_by_player, "a")
        self.assertRaisesRegex(TypeError, "Expected list input", get_heroes_player, "a")
        self.assertRaisesRegex(TypeError, "Expected int input", get_medal_player, "a")

    def test_match_type_inputs(self):
        '''function should fail on wrong type inputs'''
        self.assertRaisesRegex(TypeError, "Expected int input", find_gamemode, "a")
        self.assertRaisesRegex(TypeError, "Expected int input", fms, "a")

    def test_subsidiary_functions_type_inputs(self):
        '''function should fail on wrong type inputs'''
        self.assertRaisesRegex(TypeError, "Expected dict input", delete_keys, "a", "a")
        self.assertRaisesRegex(TypeError, "Expected list input", delete_keys, {"a":"a"}, "a")
        self.assertRaisesRegex(TypeError, "Expected dict input", key_comes_first, "a", "a")
        self.assertRaisesRegex(TypeError, "Expected string input", key_comes_first, {"a":"a"}, ["a"])
        self.assertRaisesRegex(TypeError, "Expected int input", get_time, "a")

    def test_players_regions_inputs(self):
        '''function checks for equality of test inputs'''
        self.assertIn("SE Asia", get_player_regions({'2': {'games': 3, 'win': 0}, '3': {'games': 85, 'win': 46}, '5': {'games': 1, 'win': 1}, '8': {'games': 4441, 'win': 2215}, '9': {'games': 40, 'win': 20}}))
        self.assertIn("EU West", get_player_regions({'2': {'games': 11, 'win': 2}, '3': {'games': 91, 'win': 55}, '5': {'games': 1, 'win': 1}, '8': {'games': 104, 'win': 51}, '9': {'games': 17, 'win': 10}}))
        self.assertIn("China UC", get_player_regions({'0': {'games': 52, 'win': 25}, '5': {'games': 816, 'win': 446}, '7': {'games': 416, 'win': 195}, '12': {'games': 317, 'win': 133}, '13': {'games': 137, 'win': 73},
        '17': {'games': 94, 'win': 36}, '18': {'games': 468, 'win': 218}, '20': {'games': 108, 'win':44}}))
        self.assertIn("China TC Zhejiang", get_player_regions({'0': {'games': 52, 'win': 25}, '5': {'games': 816, 'win': 446}, '7': {'games': 416, 'win': 195}, '12': {'games': 317, 'win': 133}, '13': {'games': 137, 'win': 73},
        '17': {'games': 94, 'win': 36}, '18': {'games': 468, 'win': 218}, '20': {'games': 108, 'win':44}}))
        self.assertIn("China TC Shanghai", get_player_regions({'0': {'games': 52, 'win': 25}, '5': {'games': 816, 'win': 446}, '7': {'games': 416, 'win': 195}, '12': {'games': 317, 'win': 133}, '13': {'games': 137, 'win': 73},
        '17': {'games': 94, 'win': 36}, '18': {'games': 468, 'win': 218}, '20': {'games': 108, 'win':44}}))
        self.assertEqual({'SE Asia': {'games': 816, 'win': 446, 'winrate': '54.66%'}, 'China TC Zhejiang': {'games': 468, 'win': 218, 'winrate': '46.58%'}, 'Australia': {'games': 416, 'win': 195, 'winrate': '46.88%'},
        'China TC Shanghai': {'games': 317, 'win': 133, 'winrate': '41.96%'}, 'China UC': {'games': 137, 'win': 73, 'winrate': '53.28%'}, 'China TC Wuhan': {'games': 108, 'win': 44, 'winrate': '40.74%'},
        'China TC Guandong': {'games': 94, 'win': 36, 'winrate': '38.3%'}, 'Unspecified': {'games': 52, 'win': 25, 'winrate': '48.08%'}},
        get_player_regions({'0': {'games': 52, 'win': 25}, '5': {'games': 816, 'win': 446}, '7': {'games': 416, 'win': 195}, '12': {'games': 317, 'win': 133}, '13': {'games': 137, 'win': 73}, '17': {'games': 94, 'win': 36}, '18': {'games': 468, 'win': 218},'20': {'games': 108, 'win': 44}}))
        self.assertNotEqual({'EU West': {'games': 3899, 'win': 1955, 'winrate': '50.14%'}, 'Unspecified': {'games': 195, 'win': 97, 'winrate': '49.74%'}, 'US East': {'games': 101, 'win': 43, 'winrate': '42.57%'}, 'EU East': {'games': 24, 'win': 14, 'winrate': '58.33%'}, 'Russia': {'games': 13, 'win': 6, 'winrate': '46.15%'}, 'US West': {'games': 1, 'win': 1, 'winrate': '100.0%'},
        'SE Asia': {'games': 1, 'win': 0, 'winrate': '0.0%'}}, get_player_regions({'0': {'games': 52, 'win': 25}, '5': {'games': 816, 'win': 446}, '7': {'games': 416, 'win': 195}, '12': {'games': 317, 'win': 133}, '13': {'games': 137, 'win': 73},
        '17': {'games': 94, 'win': 36}, '18': {'games': 468, 'win': 218}, '20': {'games': 108, 'win':44}}))
        self.assertNotEqual({'Russia': {'games': 1535, 'win': 850, 'winrate': '55.37%'}, 'EU West': {'games': 408, 'win': 200, 'winrate': '49.02%'}, 'EU East': {'games': 166, 'win': 86, 'winrate': '51.81%'}, 'Unspecified': {'games': 78, 'win': 37, 'winrate': '47.44%'}},
        {'0': {'games': 78, 'win': 37}, '3': {'games': 408, 'win': 200},
        '8': {'games': 1535, 'win': 850}, '9': {'games': 166, 'win': 86}})
        self.assertEqual({'EU West': {'games': 3899, 'win': 1955, 'winrate': '50.14%'}, 'Unspecified': {'games': 195, 'win': 97, 'winrate': '49.74%'}, 'US East': {'games': 101, 'win': 43, 'winrate': '42.57%'}, 'EU East': {'games': 24, 'win': 14, 'winrate': '58.33%'}, 'Russia': {'games': 13, 'win': 6, 'winrate': '46.15%'}, 'US West': {'games': 1, 'win': 1, 'winrate': '100.0%'}, 'SE Asia': {'games': 1, 'win': 0, 'winrate': '0.0%'}},
        get_player_regions({'0': {'games': 195, 'win': 97}, '1': {'games': 1, 'win': 1}, '2': {'games': 101, 'win': 43}, '3': {'games': 3899, 'win': 1955}, '5': {'games': 1, 'win': 0}, '8': {'games': 13, 'win': 6}, '9': {'games': 24, 'win': 14}}))

    def test_players_gamemodes_inputs(self):
        '''function checks for equality of test inputs'''
        self.assertIn("All Pick", get_player_gamemodes({'1': {'games': 23, 'win': 7}, '2': {'games': 6, 'win': 3}, '3': {'games': 7, 'win': 2}, '4': {'games': 389, 'win': 195}, '5': {'games': 206, 'win': 115}, '22': {'games': 1556, 'win': 851}}))
        self.assertEqual({'All Pick': {'games': 1579, 'win': 858, 'winrate': '54.34%'}, 'Single Draft': {'games': 389, 'win': 195, 'winrate': '50.13%'}, 'All Random': {'games': 206, 'win': 115, 'winrate': '55.83%'}, 'Random Draft': {'games': 7, 'win': 2, 'winrate': '28.57%'}, 'Captains Mode': {'games': 6, 'win': 3, 'winrate': '50.0%'}},
        get_player_gamemodes({'1': {'games': 23, 'win': 7}, '2': {'games': 6, 'win': 3}, '3': {'games': 7, 'win': 2}, '4': {'games': 389, 'win': 195}, '5': {'games': 206, 'win': 115}, '22': {'games': 1556, 'win': 851}}))
        self.assertIn("All Pick", get_player_gamemodes({'2': {'games': 14, 'win': 8}, '4': {'games': 125, 'win': 57}, '22': {'games': 4431, 'win': 2217}}))
        self.assertEqual({'All Pick': {'games': 4431, 'win': 2217, 'winrate': '50.03%'}, 'Single Draft': {'games': 125, 'win': 57, 'winrate': '45.6%'}, 'Captains Mode': {'games': 14, 'win': 8, 'winrate': '57.14%'}},
        get_player_gamemodes({'2': {'games': 14, 'win': 8}, '4': {'games': 125, 'win': 57}, '22': {'games': 4431, 'win': 2217}}))
        self.assertIn("Random Draft", get_player_gamemodes({'1': {'games': 1135, 'win': 585}, '2': {'games': 268, 'win': 129}, '3': {'games': 214, 'win': 116},
        '4': {'games': 103, 'win': 52}, '5': {'games': 30, 'win': 14}, '12': {'games': 13, 'win': 5}, '16': {'games': 78, 'win': 33}, '22': {'games': 2393, 'win': 1182}}))
        self.assertEqual({'All Pick': {'games': 3528, 'win': 1767, 'winrate': '50.09%'}, 'Captains Mode': {'games': 268, 'win': 129, 'winrate': '48.13%'}, 'Random Draft': {'games': 214, 'win': 116, 'winrate': '54.21%'}, 'Single Draft': {'games': 103, 'win': 52, 'winrate': '50.49%'},
        'Captains Draft': {'games': 78, 'win': 33, 'winrate': '42.31%'}, 'All Random': {'games': 30, 'win': 14, 'winrate': '46.67%'}, 'LP': {'games': 13, 'win': 5, 'winrate': '38.46%'}},
        get_player_gamemodes({'1': {'games': 1135, 'win': 585}, '2': {'games': 268, 'win': 129},
       '3': {'games': 214, 'win': 116},'4': {'games': 103, 'win': 52}, '5': {'games': 30, 'win': 14}, '12': {'games': 13, 'win': 5}, '16': {'games': 78, 'win': 33}, '22': {'games': 2393, 'win': 1182}}))

    def test_players_medals_inputs(self):
        '''function checks for equality of test inputs'''
        self.assertRaisesRegex(ValueError, "Expected greater than zero", get_medal_player, -1)
        self.assertEqual("Archon 1", get_medal_player(2312))
        self.assertEqual("Herald 1", get_medal_player(100))
        self.assertEqual("Herald 1", get_medal_player(4))
        self.assertEqual("Immortal", get_medal_player(6000))
        self.assertEqual("Immortal", get_medal_player(6009))
        self.assertEqual("Divine 5", get_medal_player(5483))
        self.assertEqual("Guardian 4", get_medal_player(1234))
        self.assertEqual("Guardian 3", get_medal_player(1117))
        self.assertEqual("Legend 2", get_medal_player(3331))
        self.assertEqual("Guardian 1", get_medal_player(781))
        self.assertEqual("Crusader 3", get_medal_player(1901))

    def test_matches_gamemodes_inputs(self):
        '''function checks for equality of test inputs'''
        self.assertEqual("All Pick", find_gamemode(1))
        self.assertEqual("Captains Mode", find_gamemode(2))
        self.assertEqual("Random Draft", find_gamemode(3))
        self.assertEqual("Single Draft", find_gamemode(4))
        self.assertEqual("Captains Draft", find_gamemode(16))
        self.assertEqual("All Random", find_gamemode(5))

    def test_matches_inputs(self):
        '''function checks for equality of test inputs'''
        self.assertIn("winner", fms(6553666833))
        self.assertIn("engine", fms(6553666833))
        self.assertIn("leagueid", fms(6553666833))
        self.assertIn("players", fms(6553666833))
        self.assertIn("winner", fms(6553666833))
        self.assertIn("region", fms(6553666833))
        self.assertIn("replay_url", fms(6553666833))

    #def testExample1(self):
        #'''testing on the input data for example 1'''
        #self.assertEqual(get_users(1.0), 10.95)

if (__name__ == "__main__"):
    unittest.main()