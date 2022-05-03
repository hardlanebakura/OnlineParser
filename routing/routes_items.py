from flask import Flask, render_template, request, redirect, url_for, session, jsonify, Blueprint, abort
from jinja2 import TemplateNotFound
from log_config import logging
from mongo_collections import DatabaseAtlas
from operator import itemgetter

items_pages = Blueprint('items', __name__,
                        template_folder='Templates', static_folder='static', url_prefix="/items")

def search():
    if request.method == "POST":
        search_value = request.form.get("search_input")
        return redirect("/search_results?search={}".format(search_value))

@items_pages.route("/")
def items():
    search()
    items = [item for item in DatabaseAtlas.findAll("items", {})]
    return render_template("items.html", items = items)

@items_pages.route("/winrate")
def items_winrate():
    search()
    items = [item for item in DatabaseAtlas.findAll("items", {})]
    items = sorted(items, key = itemgetter("item_win_percentage"), reverse = True)
    return render_template("items.html", items=items)

@items_pages.route("/impact")
def items_impact():
    search()
    items = [item for item in DatabaseAtlas.findAll("items_impacts", {})]
    return render_template("items_impacts.html", items = items)

@items_pages.route("/economy")
def items_economy():
    search()
    items = [item for item in DatabaseAtlas.findAll("items", {})]
    return render_template("items.html", items = items)