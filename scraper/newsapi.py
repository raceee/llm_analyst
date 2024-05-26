import requests
import yaml
import requests

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)
import requests

base_url = 'https://newsapi.org/v2/everything'
params = {
    'q': '',
    'apiKey': config['newsapi_key'],
    'pageSize': 50,  # Number of results per page
    'page': 5       # Page number to fetch
}

topics = ['natural resources', 'crypto', 'economy', 'politics', 'business']

def fetch_data(topic, page):
    params['q'] = topic
    params['page'] = page
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data for {topic} on page {page}")
        return None

def extract_articles(data):
    if data and data.get('status') == 'ok':
        articles = []
        for article in data.get('articles', []):
            article_info = {
                "source": article['source']['name'],
                "title": article['title'],
                "description": article['description']
            }
            articles.append(article_info)
        return articles
    return []

data = {}
for topic in topics:
    all_articles = []
    page = 1
    while True:
        raw_data = fetch_data(topic, page)
        if not raw_data or 'articles' not in raw_data or not raw_data['articles']:
            break
        articles = extract_articles(raw_data)
        all_articles.extend(articles)
        page += 1
    data[topic] = all_articles

formatted_output = []
for category, articles in data.items():
    formatted_output.append(f"Category: {category}")
    for article in articles:
        formatted_output.append(f"Source: {article['source']}")
        formatted_output.append(f"Title: {article['title']}")
        formatted_output.append(f"Description: {article['description']}\n")
formatted_string = "\n".join(formatted_output)

print(formatted_string)