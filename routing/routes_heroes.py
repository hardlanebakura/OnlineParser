from flask import Flask, render_template, request, redirect, url_for, session, jsonify, Blueprint, abort
from jinja2 import TemplateNotFound
from log_config import logging
from subsidiary_functions import get_files
from mongo_collections import DatabaseAtlas
from heroes_api import *
from data import data
import os
import fnmatch

heroes_pages = Blueprint('heroes', __name__,
                        template_folder='templates', static_folder='static', url_prefix="/heroes")

def search():
    if request.method == "POST":
        search_value = request.form.get("search_input")
        return redirect("/search_results?search={}".format(search_value))

@heroes_pages.route("/")
def heroes():
    search()
    heroes_n = len(fnmatch.filter(os.listdir("static/images/hero_avatars"), '*.png'))
    heroes = [item.split("\\")[-1] for item in get_files("static/images/hero_avatars")]
    m = [item for item in DatabaseAtlas.findAll("heroes", {})]
    logging.info(os.getenv("MONGODB_CONNECTION"))
    return render_template("heroes/heroes.html", heroes_n = heroes_n, heroes = heroes, hero_popularities = hero_popularities, m = m)

@heroes_pages.route("/winrate")
def heroes_winrate():
    heroes = []
    hero_winrates = sorted([item for item in DatabaseAtlas.findAll("hero_popularities", {})], key = itemgetter("hero_winrate"), reverse = True)

    for i in range(len(hero_kdas)):
        heroes.append({})
        heroes[i]["name"] = hero_winrates[i]["hero_name"]
        heroes[i]["winrate"] = hero_winrates[i]["hero_winrate"]
        heroes[i]["popularity"] = hero_winrates[i]["hero_popularity"]
        heroes[i]["kda"] = DatabaseAtlas.find("hero_kdas", {"hero_name":heroes[i]["name"]})["hero_kda"]
    logging.info(hero_kdas)
    logging.info(hero_winrates)
    return render_template("heroes/heroes_winrate.html", heroes = heroes)

@heroes_pages.route("/meta")
def heroes_meta():
    heroes = [item for item in DatabaseAtlas.findAll("meta_heroes", {})]
    return render_template("heroes/heroes_meta.html", heroes = heroes, hero_popularities = hero_popularities)

@heroes_pages.route("/impact")
def heroes_impact():
    heroes = []
    for i in range(len(hero_kdas)):
        heroes.append({})
        heroes[i]["name"] = hero_kdas[i]["hero_name"]
        heroes[i]["kda"] = hero_kdas[i]["hero_kda"]
        heroes[i]["kills"] = hero_kdas[i]["hero_kills_per_match"]
        heroes[i]["deaths"] = hero_kdas[i]["hero_deaths_per_match"]
        heroes[i]["assists"] = hero_kdas[i]["hero_assists_per_match"]
        logging.info(hero_kdas)
    return render_template("heroes/heroes_impact.html", heroes = heroes)

@heroes_pages.route("/<string:hero>")
def hero(hero):

    search()
    counterpicks_for_hero = DatabaseAtlas.findAll("counterpicks", {"counterpick_for": hero})
    hero_statistics = DatabaseAtlas.find("heroes_statistics", {"localized_name":hero})
    items_for_hero = DatabaseAtlas.findAll("items_for_heroes", {"hero_name":hero})[0]
    lanes_for_hero = DatabaseAtlas.findAll("lanes_for_heroes", {"hero_name":hero})
    talents_for_hero = data["talent_trees"][hero_names.index(hero)]
    logging.info(data["talent_trees"])
    return render_template("heroes/hero.html", hero = get_hero_info(hero), hero_popularities = hero_popularities, hero_kdas = hero_kdas, counterpicks_for_hero = counterpicks_for_hero, hero_statistics = hero_statistics,
                           items_for_hero = items_for_hero, lanes_for_hero = lanes_for_hero, talents_for_hero = talents_for_hero)

@heroes_pages.route("/<string:hero>/counterpicks")
def counterpicks_for_hero(hero):
    search()
    counterpicks = DatabaseAtlas.findAll("counterpicks", {"counterpick_for":hero})
    return render_template("heroes/counterpicks.html", hero = get_hero_info(hero), hero_popularities = hero_popularities, hero_kdas = hero_kdas, counterpicks = counterpicks)