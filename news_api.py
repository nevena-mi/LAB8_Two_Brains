import requests

from config import NEWS_API_KEY


BASE_URL = "https://newsapi.org/v2/top-headlines"


def fetch_tech_news(country="us", page_size=3):
    """
    Fetch the latest technology news articles.
    """

    params = {
        "country": country,
        "category": "technology",
        "pageSize": page_size,
        "apiKey": NEWS_API_KEY,
    }

    response = requests.get(BASE_URL, params=params)

    # Raise an error if request failed
    response.raise_for_status()

    data = response.json()

    if data["status"] != "ok":
        raise Exception(data)

    return data["articles"]


def display_articles(articles):
    """
    Print article titles, descriptions, sources, and URLs.
    """

    print("\nLatest Technology News\n")

    for i, article in enumerate(articles, start=1):

        print(f"{i}. {article['title']}")
        print(f"   Source: {article['source']['name']}")

        if article["description"]:
            print(f"   Description: {article['description']}")

        print(f"   URL: {article['url']}")
        print()


if __name__ == "__main__":

    try:
        articles = fetch_tech_news()

        display_articles(articles)

    except Exception as e:
        print("✗ Error fetching news:")
        print(e)