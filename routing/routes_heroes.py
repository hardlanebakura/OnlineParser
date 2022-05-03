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
                        template_folder='Templates', static_folder='static', url_prefix="/heroes")

def search():
    if request.method == "POST":
        search_value = request.form.get("search_input")
        return redirect("/search_results?search={}".format(search_value))

@heroes_pages.route("/")
def heroes():
    search()
    heroes_n = len(fnmatch.filter(os.listdir("static/images/hero_avatars"), '*.png'))
    heroes = [item.split("\\")[-1] for item in get_files("static/images/hero_avatars")]
    logging.info(heroes)
    logging.info(DatabaseAtlas.findAll("heroes", {}))
    m = [item for item in DatabaseAtlas.findAll("heroes", {})]
    return render_template("heroes.html", heroes_n = heroes_n, heroes = heroes, hero_popularities = hero_popularities, m = m)

@heroes_pages.route("/<string:hero>")
def hero(hero):

    search()
    counterpicks_for_hero = DatabaseAtlas.findAll("counterpicks", {"counterpick_for": hero})
    hero_statistics = DatabaseAtlas.find("heroes_statistics", {"localized_name":hero})
    items_for_hero = DatabaseAtlas.findAll("items_for_heroes", {"hero_name":hero})[0]
    lanes_for_hero = DatabaseAtlas.findAll("lanes_for_heroes", {"hero_name":hero})
    talents_for_hero = data["talent_trees"][hero_names.index(hero)]
    logging.info(data["talent_trees"])
    return render_template("hero.html", hero = get_hero_info(hero), hero_popularities = hero_popularities, hero_kdas = hero_kdas, counterpicks_for_hero = counterpicks_for_hero, hero_statistics = hero_statistics,
                           items_for_hero = items_for_hero, lanes_for_hero = lanes_for_hero, talents_for_hero = talents_for_hero)

@heroes_pages.route("/<string:hero>/counterpicks")
def counterpicks_for_hero(hero):
    search()
    counterpicks = DatabaseAtlas.findAll("counterpicks", {"counterpick_for":hero})
    logging.info(counterpicks)
    return render_template("counterpicks.html", hero = get_hero_info(hero), hero_popularities = hero_popularities, hero_kdas = hero_kdas, counterpicks = counterpicks)