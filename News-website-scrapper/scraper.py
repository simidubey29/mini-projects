import requests
import json
import os
from bs4 import BeautifulSoup

URL = "https://www.moneycontrol.com/"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

news_data = []

response = requests.get(URL, headers=HEADERS)

soup = BeautifulSoup(response.text, "lxml")

links = soup.find_all("a")

seen = set()

for link in links:

    title = link.get("title")
    href = link.get("href")

    if title and href:

        if href not in seen:

            seen.add(href)

            news_data.append({
                "title": title,
                "url": href
            })

os.makedirs("data", exist_ok=True)

with open("data/news.json", "w", encoding="utf-8") as f:

    json.dump(
        news_data,
        f,
        indent=4,
        ensure_ascii=False
    )

print(f"Saved {len(news_data)} articles")