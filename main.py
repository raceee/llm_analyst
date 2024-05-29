from scraper.newsapi import news_scrape
import requests
import yaml
import os

# read config.yaml file
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

api_key = config.get('oai')

def get_openai_completion(prompt, model="gpt-4-turbo", max_tokens=150):
    url = "https://api.openai.com/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
        "temperature": 0.7,
        "n": 1,
        "stop": None
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        completion = response.json()
        return completion['choices'][0]['message']['content'].strip()
    else:
        raise Exception(f"Request failed with status code {response.status_code}: {response.text}")


def main():
    news_string = news_scrape()
    prompt = f"""
                Here are some recent news articles:

                {news_string}

                Based on the above articles, what do you think is the most important investment opportunity?
                """

    completion = get_openai_completion(prompt)
    print(completion)

if __name__ == "__main__":
    main()

