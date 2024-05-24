import yaml
import requests

# load the configuration file
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

# Replace 'your_api_key' with your actual API key
sources = 'the-hindu,techradar,rt,reuters,rbc,ynet,xinhua-net,argaam,la-nacion,globo'
query = 'economy OR finance OR business'
url = f'https://newsapi.org/v2/top-headlines?sources={sources}&apiKey={config["newsapi_key"]}' # in the last 10 mins or 10 hours??

response = requests.get(url)
data = response.json()

# Print the headlines and descriptions of the articles
if data['status'] == 'ok':
    for article in data['articles']:
        print(f"Source: {article['source']['name']}")
        print(f"Title: {article['title']}")
        print(f"Description: {article['description']}\n")
else:
    print(f"Failed to retrieve news: {data['message']}")


'''
sources:
    the-hindu,techradar,rt,reuters,rbc,ynet,xinhua-net,argaam,la-nacion,globo
'''
