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
import time
from selenium_config import *

start_time = time.time()

#chrome_options.add_extension("C://Users/dESKTOP I5/AppData/Local/Google/Chrome/User Data/Default/Extensions/gighmmpiobklfepjocnamgkkbiglidom/4.37.0_0.crx")

driver = config_driver()

heroes = [item for item in DatabaseAtlas.findAll("heroes", {})]

URL_HERO = "https://dota2.fandom.com/wiki/"

def get_hero(hero_url, hero):
    driver.get(hero_url)
    d = hero.copy()
    attribute_values = []
    driver.implicitly_wait(0.4)
    for i in range(4,7):
        attribute_values.append(get_element_text("/html/body/div[4]/div[3]/div[3]/main/div[3]/div/div/table[1]/tbody/tr[1]/th/div[2]/div[{}]".format(i)))
    d["strength"] = attribute_values[0]
    d["agility"] = attribute_values[1]
    d["intelligence"] = attribute_values[2]
    d["starting_armor"] = get_element_text("/html/body/div[4]/div[3]/div[3]/main/div[3]/div/div/table[1]/tbody/tr[3]/td/table/tbody/tr[7]/td[2]")
    d["starting_ms"] = get_element_text("/html/body/div[4]/div[3]/div[3]/main/div[3]/div/div/table[1]/tbody/tr[3]/td/table/tbody/tr[17]/td[2]")
    d["starting_damage"] = get_element_text("/html/body/div[4]/div[3]/div[3]/main/div[3]/div/div/table[1]/tbody/tr[3]/td/table/tbody/tr[11]/td[2]")
    d["attack_range"] = get_element_text("/html/body/div[4]/div[3]/div[3]/main/div[3]/div/div/table[1]/tbody/tr[3]/td/table/tbody/tr[13]/td[2]")
    d["attack_speed"] = get_element_text("/html/body/div[4]/div[3]/div[3]/main/div[3]/div/div/table[1]/tbody/tr[3]/td/table/tbody/tr[14]/td[2]")
    d["attack_animation"] = get_element_text("/html/body/div[4]/div[3]/div[3]/main/div[3]/div/div/table[1]/tbody/tr[3]/td/table/tbody/tr[15]/td[2]/span[1]")
    d["attack_backswing"] = get_element_text("/html/body/div[4]/div[3]/div[3]/main/div[3]/div/div/table[1]/tbody/tr[3]/td/table/tbody/tr[15]/td[2]/span[2]")
    d["attack_animation"] = d["attack_animation"] + " + " + d["attack_backswing"]
    isPresent = driver.find_elements(By.XPATH, "/html/body/div[4]/div[3]/div[3]/main/div[3]/div/div/table[1]/tbody/tr[3]/td/table/tbody/tr[16]/td[2]/span")
    if isPresent:
        d["attack_projectile_speed"] = get_element("/html/body/div[4]/div[3]/div[3]/main/div[3]/div/div/table[1]/tbody/tr[3]/td/table/tbody/tr[16]/td[2]/span")
    else: 
        d["attack_projectile_speed"] = get_element("/html/body/div[4]/div[3]/div[3]/main/div[3]/div/div/table[1]/tbody/tr[3]/td/table/tbody/tr[16]/td[2]").get_attribute("innerText")

    #hero avatar

    hero_name = get_element_text("/html/body/div[4]/div[3]/div[3]/main/div[2]/div[2]/div[1]/h1")
    l = get_element("/html/body/div[4]/div[3]/div[3]/main/div[3]/div/div/table[1]/tbody/tr[1]/th/div[1]/a/img")
    #l.screenshot("static/images/hero_avatars/{}.png".format(hero_name))
    return d

def image_cropping(hero_name):
    img = Image.open("static/images/hero_avatars/{}.png".format(hero_name))
    height, width = img.size
    border = (0, 0, 0, 30)
    img1 = ImageOps.crop(img, border)
    img1.save("static/images/hero_avatars/{}.png".format(hero_name))
    logging.info(img.size)
    logging.info(img.mode)

def list_dict_to_database(dict1):
    list_of_values = []
    for item in dict1:
        list(item.values())[0]["hero"] = [*item][0]
        list_of_values.append(list(item.values())[0])
    return list_of_values

def get_hero_counterpicks(hero_url, hero):
    driver.get(hero_url)
    driver.minimize_window()
    d = hero.copy()
    driver.implicitly_wait(0.4)
    all_counterpicks_for_hero = []
    for i in range(1, len(heroes)):
        counterpick = {}
        hero_name_element = get_element_text("/html/body/div[2]/div[2]/div[3]/div[4]/section[3]/article/table/tbody/tr[{}]/td[2]/a".format(i))
        hero_advantage_vs_hero = get_element_text("/html/body/div[2]/div[2]/div[3]/div[4]/section[3]/article/table/tbody/tr[{}]/td[3]".format(i))
        hero_win_percentage = get_element_text("/html/body/div[2]/div[2]/div[3]/div[4]/section[3]/article/table/tbody/tr[{}]/td[4]".format(i))
        counterpick[hero_name_element] = {"impact" : i, "advantage" : hero_advantage_vs_hero, "win_percentage" : 100 - float(hero_win_percentage.split("%")[0])}
        all_counterpicks_for_hero.append(counterpick)
    return all_counterpicks_for_hero

def scrape_hero_statistics():
    for hero in heroes:
        d = hero.copy()
        d["search_name"] = hero["localized_name"].replace(" ", "_")
        url_hero = URL_HERO + d["search_name"]
        driver = webdriver.Chrome("chromedriver_2.exe")
        d = get_hero(url_hero, d)
        logging.info(d)
        #image_cropping(hero["localized_name"])
        DatabaseAtlas.insertOne("heroes_statistics", d)

#scrape_hero_statistics()

#DatabaseAtlas.dropCol("heroes_statistics")

heroes_statistics = []
for item in DatabaseAtlas.findAll("heroes_statistics", {}):
    logging.info(item["localized_name"])
    heroes_statistics.append(item)

for hero in heroes:
    d = hero.copy()
    d["search_name"] = hero["localized_name"].replace(" ", "_")

all_ms = [{"name" :hero["localized_name"], "ms" : hero["starting_ms"]} for hero in heroes_statistics]
logging.info(all_ms)

URL_COUNTERPICKS = "https://www.dotabuff.com/heroes/"

driver = webdriver.Chrome("chromedriver_2.exe")

all_counterpicks = []

def scrape_counterpicks():
    for i in range(len(heroes)):
        d = heroes[i].copy()
        url_counterpicks = URL_COUNTERPICKS + d["localized_name"].lower().replace(" ", "-").replace("'", "") + "/counters"
        d = get_hero_counterpicks(url_counterpicks, d)
        all_counterpicks.append({heroes[i]["localized_name"] : d})
        logging.info(d)
        dict1 = list_dict_to_database(d)
        for item in dict1:
            item["counterpick_for"] = heroes[i]["localized_name"]
            logging.info(item)
            DatabaseAtlas.insertOne("counterpicks", item)

#scrape_counterpicks()

def scrape_winrates():
    for i in range(len(heroes)):
        d = heroes[i].copy()

def scrape_popularities():
    URL_POPULARITIES = "https://dotabuff.com/heroes/played"
    driver.get(URL_POPULARITIES)
    hero_popularities = []
    for i in range(1, len(heroes) + 1):
        hero_popularity = {}
        hero_popularity["hero_name"] = get_element("/html/body/div[2]/div[2]/div[3]/div[4]/section/article/table/tbody/tr[{}]/td[2]/a".format(i)).get_attribute("innerText")
        hero_popularity["hero_popularity"] = get_element("/html/body/div[2]/div[2]/div[3]/div[4]/section/article/table/tbody/tr[{}]/td[4]".format(i)).get_attribute("innerText")
        hero_popularity["hero_winrate"] = get_element("/html/body/div[2]/div[2]/div[3]/div[4]/section/article/table/tbody/tr[{}]/td[5]".format(i)).get_attribute("innerText")
        DatabaseAtlas.insertOne("hero_popularities", hero_popularity)
        hero_popularities.append(hero_popularity)
    logging.info(hero_popularities)
    return hero_popularities

def scrape_kdas():
    URL_KDAS = "https://www.dotabuff.com/heroes/impact"
    driver.get(URL_KDAS)
    hero_kdas = []
    for i in range(1, len(heroes) + 1):
        hero_kda = {}
        hero_kda["hero_name"] = get_element("/html/body/div[2]/div[2]/div[3]/div[4]/section/article/table/tbody/tr[{}]/td[2]/a".format(i)).get_attribute("innerText")
        hero_kda["hero_kda"] = get_element("/html/body/div[2]/div[2]/div[3]/div[4]/section/article/table/tbody/tr[{}]/td[3]".format(i)).get_attribute("innerText")
        hero_kda["hero_kills_per_match"] = get_element("/html/body/div[2]/div[2]/div[3]/div[4]/section/article/table/tbody/tr[{}]/td[4]".format(i)).get_attribute("innerText")
        hero_kda["hero_deaths_per_match"] = get_element("/html/body/div[2]/div[2]/div[3]/div[4]/section/article/table/tbody/tr[{}]/td[5]".format(i)).get_attribute("innerText")
        hero_kda["hero_assists_per_match"] = get_element("/html/body/div[2]/div[2]/div[3]/div[4]/section/article/table/tbody/tr[{}]/td[6]".format(i)).get_attribute("innerText")
        DatabaseAtlas.insertOne("hero_kdas", hero_kda)
        hero_kdas.append(hero_kda)
    logging.info(hero_kdas)
    return hero_kdas

#scrape_popularities()
#scrape_kdas()

driver.quit()

#for item in heroes_statistics:
    #logging.info(item)

logging.info("{}".format(round(time.time() - start_time, 3)) + " seconds")

