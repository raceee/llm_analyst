from scraper.newsapi import news_scrape
import requests
import yaml
import os

# Read config.yaml file
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

def split_text(text, delimiter="\n"):
    lines = text.split(delimiter)
    halfway = len(lines) // 2
    return delimiter.join(lines[:halfway]), delimiter.join(lines[halfway:])

def main():
    news_string = news_scrape()
    
    part1, part2 = split_text(news_string)
    
    prompt1 = f"""
                Here are some recent news articles (part 1):

                {part1}

                Based on the above articles, what do you think is the most important investment opportunity?
                """
    
    prompt2 = f"""
                Here are some recent news articles (part 2):

                {part2}

                Based on the above articles, what do you think is the most important investment opportunity?
                """

    completion1 = get_openai_completion(prompt1)
    completion2 = get_openai_completion(prompt2)
    
    print("Response for part 1:")
    print(completion1)
    print("\nResponse for part 2:")
    print(completion2)

if __name__ == "__main__":
    main()
