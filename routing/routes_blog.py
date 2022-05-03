from flask import Flask, render_template, request, redirect, url_for, session, jsonify, Blueprint, abort
from jinja2 import TemplateNotFound
from log_config import logging
from mongo_collections import DatabaseAtlas

blog_pages = Blueprint('blog', __name__,
                        template_folder='Templates', static_folder='static', url_prefix="/blogs")

def search():
    if request.method == "POST":
        search_value = request.form.get("search_input")
        return redirect("/search_results?search={}".format(search_value))

@blog_pages.route("/")
def blogs():
    search()
    return render_template("blogs.html")

@blog_pages.route("/<int:blog_id>")
def blog(blog_id):
    search()
    render_template("blogs_{}.html".format(blog_id))