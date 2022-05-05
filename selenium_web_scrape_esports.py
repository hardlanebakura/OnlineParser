from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.common.exceptions as e
from selenium.webdriver.chrome.options import Options
from log_config import logging
import time
from mongo_collections import DatabaseAtlas
from PIL import Image, ImageOps
from collections import OrderedDict
from operator import itemgetter
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_config import *
from team import Team
from selenium.webdriver.remote.remote_connection import LOGGER
import time
import re
import json

start_time = time.time()

LOGGER.setLevel(logging.WARNING)

driver = config_driver()

URL_ESPORTS = "https://www.gosugamers.net/dota2/rankings"

def get_style_if_exists(element):
    try:
        selected_element = driver.find_element(By.XPATH, element)
    except e.NoSuchElementException:
        logging.warning("Element does not exist")
        return None
    return selected_element.get_attribute("style")[23:]

#format ranking
def format_team_name(string1):
    team_points = re.sub("[^0-9]", "", string1)
    if len(team_points) > 3:
        team_name = string1[:-5]
    else:
        team_name = string1[:-4]
    return team_name, team_points

def scrape_esports_teams(esports_url):
    driver.get(esports_url + "?region=3")
    driver.maximize_window()
    esports_teams = []
    time.sleep(1)
    for i in range(1, 40):
        to_scroll_by = i * 23
        #scroll down the page
        driver.execute_script("window.scrollBy(0,{});".format(to_scroll_by))
        team_link = get_element("/html/body/div[2]/main/div[3]/div/div[1]/div/div[2]/div/div[1]/div/ul/li[{}]/a".format(i))
        team_link.click()
        #wait for the page load
        time.sleep(4)
        #scroll to the top of page
        driver.execute_script("window.scrollBy(0,{});".format(-to_scroll_by))
        team = {}
        logging.info(team_link.get_attribute("innerText"))
        team["regional_ranking"] = team_link.get_attribute("innerText").split(" ")[1]
        if team_link.get_attribute("innerText").split(" ")[-2] != "":
            team_name = " ".join([team_link.get_attribute("innerText").split(" ")[-2], team_link.get_attribute("innerText").split(" ")[-1]])
        else:
            team_name = team_link.get_attribute("innerText").split(" ")[-1]
        team["name"] = format_team_name(team_name)[0]
        team["rank_points"] = format_team_name(team_link.get_attribute("innerText").split(" ")[-1])[1]
        team["logo"] = get_style_if_exists("/html/body/div[2]/main/div[3]/div/div[1]/div/div[2]/div/div[2]/section[1]/div[2]/a[1]")
        team["prize_winning"] = get_element_text("/html/body/div[2]/main/div[3]/div/div[1]/div/div[2]/div/div[2]/section[1]/div[2]/div[2]/span")
        team["winrate"] = get_element_text("/html/body/div[2]/main/div[3]/div/div[1]/div/div[2]/div/div[2]/section[1]/div[3]/table/tbody/tr[1]/td[3]")
        team["wins"] = get_element_text("/html/body/div[2]/main/div[3]/div/div[1]/div/div[2]/div/div[2]/section[1]/div[3]/table/tbody/tr[2]/td[3]/span[1]")
        team["draws"] = get_element_text("/html/body/div[2]/main/div[3]/div/div[1]/div/div[2]/div/div[2]/section[1]/div[3]/table/tbody/tr[2]/td[3]/span[2]")
        team["losses"] = get_element_text("/html/body/div[2]/main/div[3]/div/div[1]/div/div[2]/div/div[2]/section[1]/div[3]/table/tbody/tr[2]/td[3]/span[3]")
        team["current_streak"] = get_element_text("/html/body/div[2]/main/div[3]/div/div[1]/div/div[2]/div/div[2]/section[1]/div[3]/table/tfoot/tr/td")
        team["recent_match_1"] = get_element_text("/html/body/div[2]/main/div[3]/div/div[1]/div/div[2]/div/div[2]/section[2]/div/div/div/div/ul/li[1]/a/span")
        team["players"] = []
        #for teams that have players in roster
        if get_element_if_exists("/html/body/div[2]/main/div[3]/div/div[1]/div/div[2]/div/div[2]/section[3]/div[5]/div/a") != None:
            for i in range(1, 6):
                player = get_element_text("/html/body/div[2]/main/div[3]/div/div[1]/div/div[2]/div/div[2]/section[3]/div[{}]/div/a/div[3]".format(i))
                img = get_style_if_exists("/html/body/div[2]/main/div[3]/div/div[1]/div/div[2]/div/div[2]/section[3]/div[{}]/div/a/div[1]".format(i))
                team["players"].append({"name": player, "country": "", "image": img})
        #for teams that have recent match
            for recent_index in range(1, 4):
                result = get_text_if_exists("/html/body/div[2]/main/div[3]/div/div[1]/div/div[2]/div/div[2]/section[2]/div/div/div/div/ul/li[{}]/a/span".format(recent_index))
                opponent = get_text_if_exists("/html/body/div[2]/main/div[3]/div/div[1]/div/div[2]/div/div[2]/section[2]/div/div/div/div/ul/li[{}]/a".format(recent_index))
                opponent_img = get_style_if_exists("/html/body/div[2]/main/div[3]/div/div[1]/div/div[2]/div/div[2]/section[2]/div/div/div/div/ul/li[{}]/a/div".format(recent_index))
                if result != None:
                    team["recent_match_{}".format(recent_index)] = {"result":result, "opponent":opponent.split(" ")[2][:-2], "opponent_img":opponent_img}

        logging.info(team)
        esports_teams.append(team)
    #formatting teams

    logging.info(esports_teams)
    #with open("data/eropean_esports", "w") as json_file:
        #json_file.write(esports_teams)
    for team in esports_teams:
        Team1 = Team(team)
        logging.info(Team1)
        DatabaseAtlas.insertOne("sa_teams", team)

def scrape_meta(meta_url):
    driver.get(meta_url)
    for i in range(1, 124):
        d = {}
        d["name"] = get_element_text("/html/body/div[2]/div[2]/div[3]/div[4]/section/footer/article/table/tbody/tr[{}]/td[2]".format(i))
        d["usage_herald"] = get_element_text("/html/body/div[2]/div[2]/div[3]/div[4]/section/footer/article/table/tbody/tr[{}]/td[3]".format(i))

URL_META = "https://www.dotabuff.com/heroes/meta"
scrape_meta(URL_META)

teams = [item for item in DatabaseAtlas.findAll("sa_teams", {})]
logging.info(item for item in DatabaseAtlas.findAll("sa_teams_1", {}))
#with open("data/sa_esports.json", "w") as json_file:
        #json.dump(teams, json_file, indent = 4)

print(DatabaseAtlas.db.list_collection_names())

#data_file = open("data/sa_esports.json")
#data = json.load(data_file)
#logging.info(data)

#driver.quit()

#scrape_esports_teams(URL_ESPORTS)
#teams = [item for item in DatabaseAtlas.findAll("eu_teams", {})]
#logging.info(teams)



logging.info("{}".format(round(time.time() - start_time, 3)) + " seconds")