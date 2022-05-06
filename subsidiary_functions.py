from data import data
from log_config import logging
from mongo_collections import DatabaseAtlas
from datetime import datetime, date
import time
import os

def get_gamemode(gamemode_id):
    if not isinstance(gamemode_id, int):
        raise TypeError("Expected int input")
    if gamemode_id != 22:
        return data["gamemode_alts"][data["gamemodes"][int(gamemode_id)]]
    else:
        return "All Pick"

def delete_keys(dict1, indexes_to_remove):
    if not (isinstance(dict1, dict)):
        raise TypeError("Expected dict input")
    if not isinstance(indexes_to_remove, list):
        raise TypeError("Expected list input")
    list1 = list(dict1.items())
    list2 = []
    for i in range(len(list1)):
        if i not in indexes_to_remove:
            list2.append(list1[i])
    dict1 = dict(list2)
    return dict1

def key_comes_first(dict1, key):
    if not (isinstance(dict1, dict)):
        raise TypeError("Expected dict input")
    if not isinstance(key, str):
        raise TypeError("Expected string input")
    list1 = list(dict1.items())
    for item in list1:
        if item[0] == key:
            chosen_index = list1.index(item)
            value = item
            list1.pop(chosen_index)
            list1.insert(0, value)
    dict1 = dict(list1)
    logging.info(dict1)
    return dict1

def get_winrate(player_dict):
    if not isinstance(player_dict, dict):
        raise TypeError("Expected dict input")
    player_dict["winrate"] = str(round(((player_dict["win"] / player_dict["games"]) * 100), 2)) + "%"
    return player_dict

def get_time(seconds, interval = "default"):
    if not isinstance(seconds, int):
        raise TypeError("Expected int input")
    result = time.strftime(str(datetime.now() - datetime.fromisoformat(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(seconds)))))
    #logging.info(result)
    #logging.info(seconds)
    #logging.info(type(seconds))

    #more than a day
    if "days" in result or "day" in result:
        days = int(result.split(" ")[0])
        hms = list(result.split(", ")[1].split(":"))
        #logging.info(hms)
        #logging.info(hms[0])
        hours = int(hms[0])
        minutes = int(hms[1])
        seconds = int(hms[2].split(".")[0])
        total_seconds = days * 86400 + hours * 3600 + minutes * 60 + seconds * 1

    #less than a day
    else:
        hms = list(result.split(":"))
        hours = int(hms[0])
        minutes = int(hms[1])
        seconds = int(hms[2].split(".")[0])
        total_seconds = hours * 3600 + minutes * 60 + seconds * 1
    #logging.info(total_seconds)

    def years():
        return divmod(total_seconds, 31536000)  # Seconds in a year=31536000.

    def months(seconds=None):
        return divmod(total_seconds, 2592000)

    def days(seconds=None):
        return (divmod(seconds if seconds != None else total_seconds, 86400)) # Seconds in a day = 86400

    def hours(seconds=None):
        return divmod(seconds if seconds != None else total_seconds, 3600)  # Seconds in an hour = 3600

    def minutes(seconds=None):
        return divmod(seconds if seconds != None else total_seconds, 60)  # Seconds in a minute = 60

    def seconds(seconds=None):
        if seconds != None:
            return divmod(seconds, 1)
        return total_seconds

    if int(months()[0]) != 0:
        #logging.debug(int(months()[0]))
        #logging.debug(int(days()[0]))
        days_v = int(days()[0]) - int(months()[0]) * 30
    else:
        days_v = int(days()[0])

    def totalDuration():
        y = years()
        mo = months(y[0])
        d = days(y[1])  # Use remainder to calculate next variable
        h = hours(d[1])
        mi = minutes(h[1])
        s = seconds(mi[1])
        d = days_v
        #logging.info(days_v)
        #logging.info(mo)
        return "Time between dates: {} years, {} months, {} days, {} hours, {} minutes and {} seconds".format(int(y[0]), int(mo[0]), days_v, int(h[0]), int(mi[0]),
                                                                                                   int(s[0]))


    return {
        'years': int(years()[0]),
        'months': int(months()[0]),
        'days':  days_v,
        'hours': int(hours()[0]),
        'minutes': int(minutes()[0]),
        'seconds': int(seconds()),
        'default': totalDuration()
    } [interval]

def get_files(target_dir):
    item_list = os.listdir(target_dir)

    file_list = list()
    for item in item_list:
        item_dir = os.path.join(target_dir,item)
        if os.path.isdir(item_dir):
            file_list += get_files(item_dir)
        else:
            file_list.append(item_dir)
    return file_list


