from flask import Flask, render_template, request, redirect, url_for, session, jsonify, Blueprint, abort
from jinja2 import TemplateNotFound
from log_config import logging
from mongo_collections import DatabaseAtlas
from heroes_api import *
from subsidiary_functions import get_files
from find_player import find_player
import requests
from find_match_stats import fms

search_results_page = Blueprint('search_results', __name__,
                        template_folder='Templates', static_folder='static', url_prefix="/search_results")

def get_search_results(search):
    searched_match = fms(int(search))
    searched_player = find_player(int(search))
    #32 bits id
    searched_player_64_id = find_player(int(search) + 6561197960265728)
    #64 bits id
    logging.info(searched_player)
    logging.info(searched_player_64_id)
    if searched_player != None or searched_player_64_id != None:
        return redirect("/players/{}".format(search))
    if searched_match != None:
        #match exists
        logging.info(searched_match)
        return redirect("/match/{}".format(search))
    else:
        #match does not exist
        return "Neither player nor match with that id was found, please try different id"

@search_results_page.route("/")
def search_results():
    # if request.method == "POST":
    #     search_value = request.form.get("search_submit")
    #     return redirect("/search_results?search={}".format(search_value))

    search_result = get_search_results(request.args.get("search"))
    #searched_match = None
    return search_result

    #return render_template("search_results.html", searched_match = searched_match)