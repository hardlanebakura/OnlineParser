from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.common.exceptions as e
from selenium.webdriver.chrome.options import Options
from log_config import logging
from PIL import Image, ImageOps
import requests
from mongo_collections import DatabaseAtlas
from selenium_config import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.remote_connection import LOGGER
import json
from bson.json_util import dumps

#chrome_options = Options()

# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--window-size=1920,1080")
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--disable-crash-reporter")
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--disable-in-process-stack-traces")
# chrome_options.add_argument("--disable-logging")
# chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument("--log-level=3")
# chrome_options.add_argument("--output=/dev/null")

LOGGER.setLevel(logging.WARNING)

URL_HERO = "https://dotabuff.com/heroes/"
URL_ITEMS = "https://dotabuff.com/items"
URL_ITEMS_IMPACT = "https://dotabuff.com/items/impact"

def get_all_items(items_url):
    driver.get(items_url)
    list1 = []
    for i in range(1, 238):
        d = {}
        d["item_img"] = get_element("/html/body/div[2]/div[2]/div[3]/div[4]/section/article/table/tbody/tr[{}]/td[1]/div/a/img".format(i)).get_attribute("src")
        d["item_name"] = get_element("/html/body/div[2]/div[2]/div[3]/div[4]/section/article/table/tbody/tr[{}]/td[2]/a".format(i)).get_attribute("innerText")
        d["item_usage"] = get_element("/html/body/div[2]/div[2]/div[3]/div[4]/section/article/table/tbody/tr[{}]/td[3]".format(i)).get_attribute("innerText")
        d["item_usage_percentage"] = get_element("/html/body/div[2]/div[2]/div[3]/div[4]/section/article/table/tbody/tr[{}]/td[4]".format(i)).get_attribute("innerText")
        d["item_win_percentage"] = get_element("/html/body/div[2]/div[2]/div[3]/div[4]/section/article/table/tbody/tr[{}]/td[5]".format(i)).get_attribute("innerText")
        #DatabaseAtlas.insertOne("items", d)
        list1.append(d)
    logging.info(list1)

def get_hero_additional_info(hero_url):
    hero_names = [hero["localized_name"] for hero in DatabaseAtlas.findAll("heroes", {})]
    logging.info(hero_url)
    for i in range(len(hero_names)):
        driver.get((hero_url + "{}".format(hero_names[i].lower())).replace(" ", "-").replace("'", ""))
        logging.info((hero_url + "{}".format(hero_names[i].lower())).replace(" ", "-").replace("'", ""))
        driver.implicitly_wait(0.4)
        items_for_hero = {"hero_name":hero_names[i]}
        lanes_for_hero = []
        talent_tree = {"hero_name":hero_names[i]}
        talent_tree_levels = [25, 20, 15, 10]
        for lane_number_index in range(1, 4):
            lanes = {}
            lane = get_element_if_exists("/html/body/div[2]/div[2]/div[3]/div[4]/div[1]/div[1]/section[1]/article/table/tbody/tr[{}]/td[1]".format(lane_number_index))
            if lane != None:
                lane = lane.get_attribute("innerText")
                lanes["hero_name"] = hero_names[i]
                lanes["lane"] = lane
                lanes["presence"] = get_element("/html/body/div[2]/div[2]/div[3]/div[4]/div[1]/div[1]/section[1]/article/table/tbody/tr[{}]/td[2]".format(lane_number_index)).get_attribute("innerText")
                lanes["winrate"] = get_element("/html/body/div[2]/div[2]/div[3]/div[4]/div[1]/div[1]/section[1]/article/table/tbody/tr[{}]/td[3]".format(lane_number_index)).get_attribute("innerText")
                lanes["kda"] = get_element("/html/body/div[2]/div[2]/div[3]/div[4]/div[1]/div[1]/section[1]/article/table/tbody/tr[{}]/td[4]".format(lane_number_index)).get_attribute("innerText")
                lanes["gpm"] = get_element("/html/body/div[2]/div[2]/div[3]/div[4]/div[1]/div[1]/section[1]/article/table/tbody/tr[{}]/td[5]".format(lane_number_index)).get_attribute("innerText")
                lanes["xpm"] = get_element("/html/body/div[2]/div[2]/div[3]/div[4]/div[1]/div[1]/section[1]/article/table/tbody/tr[1]/td[6]".format(lane_number_index)).get_attribute("innerText")
                lanes_for_hero.append(lanes)
                DatabaseAtlas.insertOne("lanes_for_heroes", lanes)
        for section_control in range(1, 4):
            for j in range(1, 7):
                item_for_hero_element = get_element_if_exists("/html/body/div[2]/div[2]/div[3]/div[4]/div[1]/div[1]/section[{}]/article/div/div[4]/div/div/div[{}]/div[1]/a/img".format(section_control, j))
                if item_for_hero_element != None:
                    items_for_hero["item_{}".format(j)] = item_for_hero_element.get_attribute("src")
        for talent_tree_level in range(4):
            for talent_tree_option in range(2, 4):
                    if talent_tree_option == 2:
                        m = 4
                    else:
                        m = 3
                    #talent_tree["talent_level_{}_option_{}".format(talent_tree_levels[talent_tree_level], talent_tree_option - 1)] = get_element("/html/body/div[2]/div[2]/div[3]/div[4]/div[1]/div[2]/section[1]/article/table/tbody/tr[{}]/td[2]/div[1]/div[{}]".format(talent_tree_level + 1, talent_tree_option + 1)) \
                    #.get_attribute("innerText")
        list_of_talents_advantages = [element.get_attribute("innerText") for element in driver.find_elements(By.CLASS_NAME, "talent-win-rate-relative")]
        logging.info(list_of_talents_advantages)
        element_to_hover = get_element("/html/body/div[2]/div[2]/div[3]/div[3]/div[2]/div/nav/ul/li[5]/ul/li[4]/a")
        hover = ActionChains(driver).move_to_element(element_to_hover)
        list_of_talents = [item.get_attribute("innerText") for item in driver.find_elements(By.CLASS_NAME, "talent-name-inner")]
        for talent_tree_level in range(4):
            for talent_tree_option in range(2, 4):
                talent_tree["talent_level_{}_option_{}".format(talent_tree_levels[talent_tree_level], talent_tree_option - 1)] = list_of_talents[(talent_tree_level + 1) * 2 + talent_tree_option - 4]

        logging.info(items_for_hero)
        DatabaseAtlas.insertOne("items_for_heroes", items_for_hero)
        logging.info(talent_tree)
        DatabaseAtlas.insertOne("talent_trees", talent_tree)
        logging.info(lanes_for_hero)

def get_items_impact(url_items_impact):
    driver.get(url_items_impact)
    for i in range(1, 309):
        d = {}
        d["item_img"] = get_element("/html/body/div[2]/div[2]/div[3]/div[4]/section/article/table/tbody/tr[{}]/td[1]/div/a/img".format(i)).get_attribute("src")
        d["item_name"] = get_text_if_exists("/html/body/div[2]/div[2]/div[3]/div[4]/section/article/table/tbody/tr[{}]/td[2]/a".format(i))
        d["kda"] = get_element_text("/html/body/div[2]/div[2]/div[3]/div[4]/section/article/table/tbody/tr[{}]/td[3]".format(i))
        d["item_kills"] = get_element_text("/html/body/div[2]/div[2]/div[3]/div[4]/section/article/table/tbody/tr[{}]/td[4]".format(i))
        d["item_deaths"] = get_element_text("/html/body/div[2]/div[2]/div[3]/div[4]/section/article/table/tbody/tr[{}]/td[5]".format(i))
        d["item_assists"] = get_element_text("/html/body/div[2]/div[2]/div[3]/div[4]/section/article/table/tbody/tr[{}]/td[6]".format(i))
        logging.info(d)
        DatabaseAtlas.insertOne("items_impacts", d)

#get_all_items(URL_ITEMS)
#get_hero_additional_info(URL_HERO)
#driver.quit()
hero_names = [hero["localized_name"] for hero in DatabaseAtlas.findAll("heroes", {})]

items = [item for item in DatabaseAtlas.findAll("items", {})]
logging.info(hero_names.index("Nature's Prophet"))
logging.info(hero_names[64])

talent_trees = [item for item in DatabaseAtlas.findAll("talent_trees", {})]
items_for_heroes = [item for item in DatabaseAtlas.findAll("items_for_heroes", {})]
logging.info(talent_trees)
logging.info(items_for_heroes)
#get_items_impact(URL_ITEMS_IMPACT)
#MONGODB_CONNECTION mongodb+srv://h3h4h2000:Aftmt111@cluster0.y5kq1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority

#store database info to json
def store_db_to_json_file(*columns):
    data = {}
    for column in columns:
        db_info_list = [item for item in DatabaseAtlas.findAll(column, {})]
        filename = "data/" + column.split("_")[0] + ".json"
        with open(filename, "w") as file:
            json.dump((db_info_list), file, indent = 4)
        # filename = "data/" + column.split("_")[0] + ".json"
        # logging.info(json.dumps(db_info_list))
        # with open(filename, "w") as file:
        #     json.dump(json.dumps(db_info_list), file)

    return 1

#store_db_to_json_file("items_for_heroes", "talent_trees", "lanes_for_heroes")

d = [{"name":"Peter", "loves":"pancakes"}, {"name":"Joseph", "has":"chair"}]
logging.info(json.dumps(d))

#DatabaseAtlas.dropCol("items")