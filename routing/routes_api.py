from flask import Flask, render_template, request, redirect, url_for, session, jsonify, Blueprint, abort
from jinja2 import TemplateNotFound
from log_config import logging
from mongo_collections import DatabaseAtlas
from operator import itemgetter
from data import data
from mongo_collections import DatabaseAtlas
from find_match_stats import fms
from find_player import find_player

api_pages = Blueprint('api', __name__,
                        template_folder='Templates', static_folder='static', url_prefix="/api")

@api_pages.route("/")
def index():
    d = {
            "heroes":"/heroes",
            "hero":"/heroes/<hero_name>",
            "items":"/items",
            "esports":"/esports",
            "esports teams":"/esports/<team_name>",
            "match":"/match/<id>",
            "player":"/player/<id>"
        }
    return jsonify("all_available_pages", d)

@api_pages.route("/heroes/")
def heroes():
    heroes = DatabaseAtlas.findAll("heroes_statistics", {})
    logging.info(heroes)
    return jsonify("all_heroes", heroes)

@api_pages.route("/heroes/<string:hero>")
def hero(hero):
    hero = DatabaseAtlas.find("heroes_statistics", {"search_name":hero})
    return { hero["search_name"] : hero }

@api_pages.route("/items")
def items():
    items = [item for item in DatabaseAtlas.findAll("items", {})]
    return jsonify("all_items", items)

@api_pages.route("/esports")
def esports():
    return jsonify(data["esports_regions"]["Global"])

@api_pages.route("/esports/<string:team>")
def esports_team(team):
    for region in data["esports_regions"]:
        for esports_team in data["esports_regions"][region]:
            if esports_team["name"] == team:
                return esports_team

'''this page will be slow because it needs to make a call to the online API and change the response'''
@api_pages.route("/matches/<int:id>")
def match(id):
    match = fms(id)
    return match

'''this page will be slow because it needs to make a call to the online API and change the response'''
@api_pages.route("/players/<int:id>")
def player(id):
    player = find_player(id)
    logging.info(player)
    if player != None:
        return player.__dict__
    else:
        return "Incorrect id number"