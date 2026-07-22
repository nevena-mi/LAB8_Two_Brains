from news_api import fetch_tech_news
from summarizer import summarize_article, print_cost_summary


def run_application():
    """
    Main workflow:
    1. Fetch news articles
    2. Summarize articles
    3. Analyze sentiment
    4. Display results
    """

    print("\n=== News Summarizer ===\n")

    print("Fetching technology news...")

    articles = fetch_tech_news(page_size=2)

    results = []

    for article in articles:

        print("\n--------------------------------")
        print(f"Processing: {article['title']}")

        result = summarize_article(article)

        results.append(result)

        print("\nSummary:")
        print(result["summary"])

        print("\nSentiment:")
        print(result["sentiment"])


    print_cost_summary(results)


if __name__ == "__main__":
    run_application()