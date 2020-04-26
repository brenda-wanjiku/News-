import os 

class Config:
    SOURCE_NEWS_BASE_URL = 'http://newsapi.org/v2/sources?&apiKey={}'
    NEWS_API_KEY = os.environ.get('API_KEY')
 


class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}