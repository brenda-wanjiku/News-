from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_sources, get_articles


#Views 
@main.route('/')
def index():
    news_source = get_sources()
    title = 'News-app'

    general = news_source.get('general')
    business = get_sources('business')
    technology = get_sources('technology')
    entertainment = get_sources('entertainment')
    science = get_sources('science')
    sports = get_sources('sports')

    return render_template('index.html', title = title, general = general, business = business, technology = technology, sports = sports, entertainment = entertainment, science = science )

@main.route('/source/<category>')
def categorized_sources(category):
    sources = get_sources(category)
    title = f'{sources[0].category}'

    return render_template('', title = title, sources = sources)


@main.route('source/<id>')
def source_articles(id):
    news_list = get_articles(id)
    title = f'{id}'

    return render_template('', news_list = news_list, title = title)


@main.route('/source/<title>')
def article(article_title):
    article_list = get_articles(id)
    title = f'{news_list.title}'

    return render_template('', title = title )