# Use BeautifulSoup to scrape the website at https://news.ycombinator.com/news
# and get the various titles and their links

from bs4 import BeautifulSoup
import requests

yc_page = requests.get(url="https://news.ycombinator.com/news").text
soup = BeautifulSoup(yc_page, "html.parser")

articles = soup.select(selector=".storylink")
article_names = []
article_links = []
article_scores = []
index = 0
max_score = 0
for article in articles:
    article_name = article.string
    article_names.append(article_name)

    article_link = article.get("href")
    article_links.append(article_link)

    score = soup.select_one(selector=f"#score_{article.parent.parent.get('id')}")
    score = int(score.string.split(" ")[0]) if score is not None else 0
    article_scores.append(score)

    if score > max_score:
        max_score = score
        index = len(article_scores) - 1

print(article_names[index])
print(article_links[index])
print(article_scores[index])

