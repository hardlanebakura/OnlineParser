from flask import Flask, render_template, request, url_for, session, jsonify, Blueprint, abort
from jinja2 import TemplateNotFound
from log_config import logging
from mongo_collections import DatabaseAtlas
from heroes_api import *
from subsidiary_functions import get_files
import os
import fnmatch


dotapicker_page = Blueprint('dotapicker', __name__,
                        template_folder='Templates', static_folder='static', url_prefix="/dotapicker")

@dotapicker_page.route("/")
def dotapicker():
    heroes_n = len(fnmatch.filter(os.listdir("static/images/hero_avatars"), '*.png'))
    heroes = [item.split("\\")[-1] for item in get_files("static/images/hero_avatars")]
    return render_template("dotapicker.html", response_heroes = response_heroes, counterpicks = counterpicks, heroes_n = heroes_n, heroes = heroes)
