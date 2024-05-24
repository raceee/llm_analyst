import yaml
import requests

# load the configuration file
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

# Replace 'your_api_key' with your actual API key
url = f'https://newsapi.org/v2/top-headlines?sources=reuters,bbc-news,al-jazeera,cnn&apiKey={config["newsapi_key"]}'

response = requests.get(url)
data = response.json()

for article in data['articles']:
    print(f"Source: {article['source']['name']}")
    print(f"Title: {article['title']}")
    print(f"Description: {article['description']}\n")


'''
sources:
    the-hindu
    techradar
    rt
    reuters
    rbc
    ynet
    xinhua-net
    argaam
    la-nacion
    globo
'''
