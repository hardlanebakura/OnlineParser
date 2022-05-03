from selenium import webdriver
from selenium.webdriver.common.by import By
from heroes_api import *
import selenium.common.exceptions as e
from selenium.webdriver.chrome.options import Options
from mongo_collections import DatabaseAtlas
from log_config import logging
import math

chrome_options = Options()
#chrome_options.add_extension("C://Users/dESKTOP I5/AppData/Local/Google/Chrome/User Data/Default/Extensions/gighmmpiobklfepjocnamgkkbiglidom/4.37.0_0.crx")
chrome_options.add_argument("--headless")

URL_HEROES = "https://dotabuff.com/players/174788237/heroes"

def get_element(element):
    try:
        selected_element = driver.find_element(By.XPATH, element)
    except e.NoSuchElementException:
        raise ValueError("Expected XPATH input")
    return selected_element

def get_heroes(heroes_url):
    driver.get(heroes_url)
    driver.implicitly_wait(0.4)
    list1 = []
    for i in range(1, 121):
        d = {}
        d["hero_name"] = get_element("/html/body/div[2]/div[2]/div[3]/div[4]/section/article/table/tbody/tr[{}]/td[2]/a".format(i)).get_attribute("innerText")
        d["matches"] = get_element("/html/body/div[2]/div[2]/div[3]/div[4]/section/article/table/tbody/tr[{}]/td[3]".format(i)).get_attribute("innerText")
        d["win"] = get_element("/html/body/div[2]/div[2]/div[3]/div[4]/section/article/table/tbody/tr[{}]/td[4]".format(i)).get_attribute("innerText")
        DatabaseAtlas.insertOne("hero_win", d)
        list1.append(d)
    return list1

#driver = webdriver.Chrome("chromedriver_2.exe")

#get_heroes

list1 = DatabaseAtlas.findAll("hero_win", {})

list2 = ["Shadow Demon", "Hoodwink", "Skywrath Mage", "Death Prophet", "Io", "Rubick", "Meepo", "Broodmother", "Lycan", "Shadow Shaman", "Jakiro", "Lina", "Lion", "Bane", "Visage", "Viper", "Clinkz", "Outworld Devourer"]

heroes_to_win_with = []
for hero in list1:
    if float(hero["win"].split("%")[0]) < 60 and hero["hero_name"] not in list2:
        hero["matches_won"] = round(int(hero["matches"]) * (float(hero["win"].split("%")[0])/100))
        hero["new_winrate"] = float(hero["win"].split("%")[0])/100
        new_total_matches = int(hero["matches"])
        hero["new_total_wins"] = hero["matches_won"]
        hero["w"] = 0
        while hero["new_winrate"] < 0.6:
            new_total_matches += 1
            hero["w"] += 1
            hero["new_total_wins"] += 1
            hero["new_winrate"] = hero["new_total_wins"] / new_total_matches
        hero["new_winrate"] = str(round(hero["new_winrate"], 2) * 100) + "%"
        heroes_to_win_with.append(hero)


logging.info(heroes_to_win_with)
logging.info(len(heroes_to_win_with))
logging.info(sum(item["w"] for item in heroes_to_win_with))

#for item in DatabaseAtlas.findAll("hero_win", {}):
    #logging.info(item)

#DatabaseAtlas.dropCol("hero_win")

#driver.quit()
logging.info(len(list2))




