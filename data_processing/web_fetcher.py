import requests

from bs4 import BeautifulSoup

url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url)
except requests.exceptions.RequestException:
    print("Something went wrong, check the url or your internet connection")
else:
    status_code = response.status_code

    if status_code == 200:
        soup = BeautifulSoup(response.json())

        # JSON - JavaScript Object Notation

        with open("json.py", "w", encoding="utf-8") as f:
            f.write(soup.prettify())

    else:
        print(f"Unexpected status code: {status_code}")