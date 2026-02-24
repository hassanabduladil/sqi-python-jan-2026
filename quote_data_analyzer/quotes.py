import requests
from bs4 import BeautifulSoup
import re

URL = "http://quotes.toscrape.com/"

def fetch_first_page(url):
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.text

def parse_quotes(html):
    soup = BeautifulSoup(html, "html.parser")
    quote_blocks = soup.find_all("div", class_="quote")

    quotes = []
    for block in quote_blocks:
        text_tag = block.find("span", class_="text")
        text = text_tag.get_text(strip=True) if text_tag else ""

        author_tag = block.find("small", class_="author")
        author = author_tag.get_text(strip=True) if author_tag else ""

        tag_links = block.find_all("a", class_="tag")
        tags = [t.get_text(strip=True) for t in tag_links]

        quotes.append({"text": text, "author": author, "tags": tags})
    return quotes

def contains_is(text):
    return True if re.search(r"\bis\b", text, flags=re.IGNORECASE) else False

def bubble_sort_by_count_then_tag(tag_counts):
    """
    Simple bubble sort to order tags by:
    - primary: count descending
    - secondary: tag ascending
    """
    items = tag_counts[:]
    n = len(items)
    for i in range(n):
        for j in range(0, n - i - 1):
            a = items[j]
            b = items[j + 1]
            if (a["count"] < b["count"]) or (a["count"] == b["count"] and a["tag"] > b["tag"]):
                items[j], items[j + 1] = items[j + 1], items[j]
    return items

def analyze(quotes):
    total_quotes = len(quotes)

    # unique authors
    authors_list = []
    for q in quotes:
        authors_list.append(q["author"])
    unique_authors = 0
    seen = []
    for a in authors_list:
        if a not in seen:
            seen.append(a)
            unique_authors += 1

    # author with most quotes
    most_author = ""
    most_count = 0
    for a in authors_list:
        cnt = 0
        for x in authors_list:
            if x == a:
                cnt += 1
        if cnt > most_count:
            most_count = cnt
            most_author = a

    # quotes containing "is"
    is_count = 0
    for q in quotes:
        if contains_is(q["text"]):
            is_count += 1

    # tags counts (across all quotes)
    tag_counts = []
    for q in quotes:
        for t in q["tags"]:
            found = False
            for item in tag_counts:
                if item["tag"] == t:
                    item["count"] += 1
                    found = True
                    break
            if not found:
                tag_counts.append({"tag": t, "count": 1})

    return {
        "total_quotes": total_quotes,
        "unique_authors": unique_authors,
        "most_common_author": most_author,
        "most_quotes_by_author": most_count,
        "is_count": is_count,
        "tags_counts": tag_counts,
        "quotes": quotes,
    }

def print_results(results):
    print("First page quotes analysis (http://quotes.toscrape.com/):")
    print("Total quotes on page:", results["total_quotes"])
    print("Unique authors on page:", results["unique_authors"])
    if results["most_common_author"]:
        print("Author with most quotes on page:", results["most_common_author"],
              "(", results["most_quotes_by_author"], "quotes )", sep="")
    else:
        print("No authors found.")
    print("Quotes containing the word 'is' (case-insensitive):", results["is_count"])
    print("Tags and frequencies on page:")
    sorted_tags = bubble_sort_by_count_then_tag(results["tags_counts"])
    for item in sorted_tags:
        print("  ", item["tag"] + ":", item["count"])

html = fetch_first_page(URL)
quotes = parse_quotes(html)
results = analyze(quotes)
print_results(results)
