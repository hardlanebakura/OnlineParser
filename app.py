from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from config import config1
from routing.routes import *
from routing.routes_players import *
from routing.routes_matches import *
from routing.routes_heroes import *
from routing.routes_items import *
from routing.routes_blog import *
from routing.routes_dotapicker import *
from routing.routes_search_results import *
from routing.routes_esports import *
from data import data

app = Flask(__name__, template_folder = "Templates", static_folder = "static")

#Configuring application
config1(app.config, app.jinja_env)

app.register_blueprint(index_page)
app.register_blueprint(players_pages)
app.register_blueprint(match_page)
app.register_blueprint(heroes_pages)
app.register_blueprint(items_pages)
app.register_blueprint(blog_pages)
app.register_blueprint(dotapicker_page)
app.register_blueprint(search_results_page)
app.register_blueprint(esports_pages)

if (__name__ == "__main__"):
    app.run(debug=True)

