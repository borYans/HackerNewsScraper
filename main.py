from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
hacker_news_page = response.text

article_titles = []
article_links = []
soup = BeautifulSoup(hacker_news_page, "html.parser")
first_title_tags = soup.find_all(name="span", class_="titleline")

for article_title in first_title_tags:
    title = article_title.find(name="a")
    article_titles.append(title.text)
    article_links.append(title.get("href"))

article_upvotes_comperhension = [int(score.text.split()[0]) for score in soup.findAll(name="span", class_="score")]

print(article_titles)
print(article_links)
print(article_upvotes_comperhension)

largest_upvote = max(article_upvotes_comperhension)
index_of_largest_upvote = article_upvotes_comperhension.index(largest_upvote)

print(f"Largest upvote article title: {article_titles[index_of_largest_upvote]}")
print(f"Largest upvote article link: {article_links[index_of_largest_upvote]}")
print(f"Largest upvote article score: {largest_upvote}")
