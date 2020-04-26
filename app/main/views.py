from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_sources


#Views 
@main.route('/')
def index():
    news_source = get_sources()
    title = 'News-app'
    

    return render_template('index.html', title = title, news_source = news_source )

