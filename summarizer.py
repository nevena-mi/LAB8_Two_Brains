from news_api import fetch_tech_news
from llm_providers import test_openai, test_cohere


def analyze_sentiment_with_cohere(text):
    """
    Analyze sentiment using Cohere.
    """

    response = test_cohere(
        f"""
        Analyze the sentiment of this news article.
        Return only one word: Positive, Negative, or Neutral.

        Text:
        {text}
        """
    )

    return response["response"]


def summarize_article(article):
    """
    Generate summary with OpenAI and sentiment with Cohere.
    """

    content = article.get("description") or article.get("title")

    summary_result = test_openai(
        f"""
        Summarize this technology news article in 2-3 sentences:

        {content}
        """
    )

    sentiment_result = analyze_sentiment_with_cohere(content)

    return {
        "title": article["title"],
        "summary": summary_result["response"],
        "sentiment": sentiment_result,
        "usage": {
            "input_tokens": summary_result["input_tokens"],
            "output_tokens": summary_result["output_tokens"]
        }
    }


def print_cost_summary(results):
    """
    Display token usage.
    """

    total_input = 0
    total_output = 0

    for result in results:
        total_input += result["usage"]["input_tokens"]
        total_output += result["usage"]["output_tokens"]

    print("\n=== Cost Summary ===")
    print(f"Input tokens: {total_input}")
    print(f"Output tokens: {total_output}")


if __name__ == "__main__":

    print("Fetching news articles...")

    articles = fetch_tech_news(page_size=2)

    results = []

    for article in articles:
        print(f"\nProcessing: {article['title']}")

        result = summarize_article(article)

        results.append(result)

        print("\nSummary:")
        print(result["summary"])

        print("\nSentiment:")
        print(result["sentiment"])


    print_cost_summary(results)