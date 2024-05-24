import requests
import yaml

# Replace 'your_api_key' with your actual API key
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

url = f'https://newsapi.org/v2/sources?apiKey={config["newsapi_key"]}'

response = requests.get(url)
data = response.json()

# Check if the request was successful
if response.status_code == 200:
    sources = data['sources']
    for source in sources:
        print(f"Name: {source['name']}")
        print(f"ID: {source['id']}")
        print(f"Description: {source['description']}")
        print(f"Category: {source['category']}")
        print(f"Language: {source['language']}")
        print(f"Country: {source['country']}\n")
else:
    print(f"Failed to retrieve sources: {data['message']}")
