import os 

class Config:
    CATEGORIZED_SOURCE_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&sortBy=popularity&apiKey={}'
    NEWS_API_BASE_URL = ''
    NEWS_API_KEY = os.environ.get('API_KEY')


class ProdConfig(Config):
    pass

class DevConfig(Config):
    Debug = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}