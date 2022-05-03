from flask import Flask, render_template, request, redirect, url_for, session, jsonify, Blueprint, abort
from jinja2 import TemplateNotFound
from log_config import logging

index_page = Blueprint('index', __name__,
                        template_folder='Templates', static_folder='static')

@index_page.route('/', defaults={'page': 'index'}, methods = ["GET", "POST"])
def show(page):
    try:
        if request.method == "POST":
            #index page searching
            if request.form.get("index_submit") == "SUBMIT":
                search_value = request.form.get("index_search_input")
                return redirect("/search_results?search={}".format(search_value))
            #base menu search
            logging.info(request.form)
            if request.form.get("search_submit") == "SUBMIT":
                search_value = request.form.get("search_input")
                return redirect("/search_results?search={}".format(search_value))
            return redirect("/search_results?")
        return render_template("index.html")
    except TemplateNotFound:
        abort(404)

