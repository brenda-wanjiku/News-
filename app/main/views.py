from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_sources


#Views 
@main.route('/')
def index():

    title = 'News-app'
    general = get_sources('general')
    business = get_sources('business')
    technology = get_sources('technology')
    entertainment = get_sources('entertainment')
    science = get_sources('science')
    sports = get_sources('sports')

    return render_template('index.html', title = title, general = general, business = business, technology = technology, sports = sports, entertainment = entertainment, science = science )