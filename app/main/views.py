from flask import render_template,request,url_for
from . import main
from ..requests import get_sources
from ..models import Sources

@main.route('/')
def index():
    business = get_sources('business')
    general = get_sources('general')

    title = Welcome to the news highlight website

    return render_template('index.html',title = title,business = business,general = general)
