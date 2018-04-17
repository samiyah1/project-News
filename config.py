import os 


class Config:
    '''
    Parent config that will hold univeral configurations
    '''
    NEWS_SOURCES_URL = https://newsapi.org/v2/sources?category={}apiKey={}
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProductionConfig(Config):
    """
    Production configuration that 
    """
    pass

class DevelopmentConfig(Config):
    """
    """
    DEBUG = True
config_options = {
'development':DevelopmentConfig,
'production':ProductionConfig
}
