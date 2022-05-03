from flask import Flask, render_template, request, redirect, url_for, session, jsonify, Blueprint, abort
from jinja2 import TemplateNotFound
from log_config import logging
from player_info import *
from find_player import *
from data import data

esports_pages = Blueprint('esports', __name__,
                        template_folder='Templates', static_folder='static', url_prefix="/esports")

esports_regions = data["esports_regions"]

def search():
    if request.method == "POST":
        search_value = request.form.get("search_input")
        return redirect("/search_results?search={}".format(search_value))

@esports_pages.route("/")
def esports():
    search()
    for item in data:
        logging.info(item)
    return render_template("esports.html", teams = esports_regions["Global"])

@esports_pages.route("/sea")
def esports_sea():
    search()
    return render_template("esports.html", teams = esports_regions["SEA"])

@esports_pages.route("/na")
def esports_na():
    search()
    return render_template("esports.html", teams = esports_regions["North America"])

@esports_pages.route("/sa")
def esports_sa():
    search()
    return render_template("esports.html", teams = esports_regions["South America"])

@esports_pages.route("/eu")
def esports_eu():
    search()
    return render_template("esports.html", teams = esports_regions["EU.png"])

@esports_pages.route("/east_eu")
def esports_east_eu():
    search()
    return render_template("esports.html", teams = esports_regions["East EU.png"])

@esports_pages.route("/cn")
def esports_cn():
    search()
    return render_template("esports.html", teams = esports_regions["China"])
