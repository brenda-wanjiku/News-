from app import app
import urllib.request, json 
from .models import Source

#Getting api key
api_key = None

#Getting the base url
categorized_base_url = None

def configure_requests(app):
    global api_key, categorized_base_url
    api_key = app.config['NEWS_API_KEY']


def get_categorized_new(category):
    get_news_url = categorized_base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        print(get_news_data)
        get_news_response = json.loads(get_news_data)
        
    return get_news_response


    