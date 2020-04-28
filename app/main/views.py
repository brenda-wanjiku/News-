from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_sources, get_articles



#Views 
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    general = get_sources('general')
    business = get_sources('business')
    technology = get_sources('technology')
    entertainment = get_sources('entertainment')
    sports = get_sources('sports')

    title = 'The Street’s News'
    

    return render_template('index.html', title = title, general = general, business = business, technology= technology, entertainment = entertainment, sports = sports  )


@main.route('/source/<id>')
def articles(id):
    '''
    View source page function that returns articles from a particular source
    Utilizes the articles_base url API endpoint
    '''
    news_articles = get_articles(id)

    title = f'{id}'

    return render_template('source.html', title = title, news_articles = news_articles)
