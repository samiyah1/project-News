import urllib.request,json
from .models import Sources,Articles



api_key = None
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_SOURCE_URL']

def get_sources(category):
    get_sources_url = base_url.format(category,api_key)
    with urllib.request.urlopen(get_sources_url)as url
        get_news = url.read()
        get_news_response = json.loads(get_news)

        news_results = None
        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_sources(news_results_list)
    return news_results

def process_sources(sources_list):
    news_results = []
    for news_object in sources_list:
        id = news_object.get('id')
        name = news_object.get('name')
        description = news_object.get('description')
        url = news_object.get('url')
        category = news_object.get('category')
        language = news_object.get('language')
        country = news_object.get('country')
    

