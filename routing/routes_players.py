from flask import Flask, render_template, request, redirect, url_for, session, jsonify, Blueprint, abort
from jinja2 import TemplateNotFound
from log_config import logging
from player_info import *
from find_player import *
from types import SimpleNamespace

players_pages = Blueprint('players', __name__,
                        template_folder='Templates', static_folder='static', url_prefix="/players")

PLAYERS = [item["id"] for item in DatabaseAtlas.findAll("dota_players", {})]

def search():
    if request.method == "POST":
        search_value = request.form.get("search_input")
        return redirect("/search_results?search={}".format(search_value))

@players_pages.route("/")
def players():
    search()
    return render_template("players.html")

@players_pages.route("/<int:player_id>")
def player(player_id):
    search()
    #if player_id not in PLAYERS:
    player = find_player(player_id)
    #if DatabaseAtlas.find("dota_players", {"id":player_id}) == None:
        #DatabaseAtlas.insertOne("dota_players", player.__dict__)
    return render_template("player.html", player = player, player_dict = player.__dict__)
