from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_sources, get_articles



#Views 
@main.route('/')
def index():
    sources = get_sources('general')
    title = 'News-app'
    

    return render_template('index.html', title = title, sources = sources )


@main.route('/source/<category>')
def categorized_sources(category):
    title = f'{sources[0].category}'

    return render_template('', title = title)



@main.route('/source/<id>')



@main.route('/source/<title>')
def article(article_title):
    article_list = get_articles(id)
    title = f'{news_list.title}'

    return render_template('', title = title )