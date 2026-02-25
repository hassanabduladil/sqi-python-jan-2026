import requests
from bs4 import BeautifulSoup
from collections import Counter

url = 'https://quotes.toscrape.com'

response = requests.get(url).text

soup = BeautifulSoup(response, 'html.parser')

quotes = soup.select('div.quote')
print(len(quotes))


authors = [author.get_text() for author in soup.select("small.author")]
unique_authors = set(authors)
print(f"Unique Authors: {len(unique_authors)}")

author_counts = Counter(authors)
top_author, count = author_counts.most_common(1)[0]
print(f"Author with most quotes: {top_author} ({count} quotes)")

quote_texts = [q.get_text().lower() for q in soup.select("span.text")]
is_count = sum(1 for char in quote_texts if 'is' in char)
print(is_count)


tags = [tag.get_text() for tag in soup.select("a.tag")]
tag_counts = Counter(tags)

for tag, count in tag_counts.items():
    print(f"{tag}: {count}")