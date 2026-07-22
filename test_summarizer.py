# mocking OpenAI, Cohere, and News API responses

import pytest
from unittest.mock import patch

from summarizer import summarize_article, print_cost_summary


# Example article payload
mock_article = {
    "title": "AI improves healthcare workflows",
    "description": "A company released a new AI system for healthcare automation.",
    "url": "https://example.com",
    "source": {
        "name": "Example News"
    }
}


def test_summarize_article():
    """
    Test that an article is summarized and sentiment is added.
    """

    mock_openai_response = {
        "provider": "OpenAI",
        "response": "AI improves healthcare efficiency.",
        "input_tokens": 20,
        "output_tokens": 10
    }

    mock_cohere_response = {
        "provider": "Cohere",
        "response": "Positive"
    }


    with patch(
        "summarizer.test_openai",
        return_value=mock_openai_response
    ), patch(
        "summarizer.test_cohere",
        return_value=mock_cohere_response
    ):

        result = summarize_article(mock_article)


    assert result["title"] == "AI improves healthcare workflows"
    assert result["summary"] == "AI improves healthcare efficiency."
    assert result["sentiment"] == "Positive"

    assert result["usage"]["input_tokens"] == 20
    assert result["usage"]["output_tokens"] == 10



def test_cost_summary(capsys):
    """
    Test that token usage is calculated correctly.
    """

    results = [
        {
            "usage": {
                "input_tokens": 20,
                "output_tokens": 10
            }
        },
        {
            "usage": {
                "input_tokens": 30,
                "output_tokens": 15
            }
        }
    ]


    print_cost_summary(results)

    captured = capsys.readouterr()


    assert "Input tokens: 50" in captured.out
    assert "Output tokens: 25" in captured.out