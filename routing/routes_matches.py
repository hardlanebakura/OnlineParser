from flask import Flask, render_template, request, redirect, url_for, session, jsonify, Blueprint, abort
from jinja2 import TemplateNotFound
from log_config import logging
from player_info import *
from find_match_stats import fms
import json

match_page = Blueprint('match', __name__,
                        template_folder='Templates', static_folder='static', url_prefix="/match")
def search():
    if request.method == "POST":
        search_value = request.form.get("search_input")
        return redirect("/search_results?search={}".format(search_value))

@match_page.route("/<int:matchid>")
def match(matchid):
    search()
    match = fms(matchid)
    items_file = open("data/all_items.json")
    items = json.load(items_file)
    abilities = data["abilities"]
    talent_tree_codes = data["talent_trees_code"]
    logging.info(talent_tree_codes)
    return render_template("match.html", match = match, items = items, abilities = abilities, talent_tree_codes = talent_tree_codes)