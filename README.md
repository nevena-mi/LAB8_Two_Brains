# LAB8 – Two Brains, Zero Single Point of Failure

## Overview

This project implements a **multi-provider AI news summarization workflow** that demonstrates how different AI models can collaborate within a single application. The workflow retrieves the latest technology news, generates concise summaries using **OpenAI**, performs sentiment analysis using **Cohere**, and reports token usage for the OpenAI requests.

The project was developed as part of the **"Two Brains, Zero Single Point of Failure"** lab, focusing on building a reliable workflow where data moves through clearly separated stages.

---

## Workflow

```
News API
    │
    ▼
Fetch technology news articles
    │
    ▼
OpenAI
Generate article summaries
    │
    ▼
Cohere
Analyze sentiment
    │
    ▼
Display results
    │
    ▼
Usage / Cost Summary
```

---

## Project Structure

```
LAB8_TWO_BRAINS/
│
├── .env
├── .gitignore
├── requirements.txt
├── config.py
├── news_api.py
├── llm_providers.py
├── summarizer.py
├── test_summarizer.py
├── main.py
├── lab_proof.md
└── README.md
```

---

## Components

### `config.py`

* Loads environment variables.
* Validates API keys and configuration.
* Centralizes project settings.

---

### `news_api.py`

* Connects to NewsAPI.
* Retrieves the latest technology news.
* Displays article metadata.

---

### `llm_providers.py`

Provides access to two LLM providers.

**OpenAI**

* Generates article summaries.
* Tracks prompt and completion token usage.

**Cohere**

* Performs sentiment analysis.

---

### `summarizer.py`

Coordinates the complete processing pipeline.

For every article it:

1. Fetches the article content.
2. Generates a summary with OpenAI.
3. Performs sentiment analysis with Cohere.
4. Stores the results.
5. Calculates total token usage.

---

### `test_summarizer.py`

Contains unit tests using mocked provider responses.

Tests verify:

* article summarization output
* sentiment integration
* token aggregation

---

### `main.py`

Application entry point.

Running

```bash
python main.py
```

will:

1. fetch technology news,
2. summarize each article,
3. analyze sentiment,
4. display the results,
5. print a usage summary.

---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file containing:

```text
OPENAI_API_KEY=<your_openai_key>
COHERE_API_KEY=<your_cohere_key>
NEWS_API_KEY=<your_newsapi_key>

ENVIRONMENT=development
MAX_RETRIES=3
REQUEST_TIMEOUT=30
DAILY_BUDGET=5.00
```

Do **not** commit this file.

---

## Running the Project

Validate configuration:

```bash
python config.py
```

Fetch news:

```bash
python news_api.py
```

Test LLM providers:

```bash
python llm_providers.py
```

Run the complete workflow:

```bash
python main.py
```

Run unit tests:

```bash
pytest test_summarizer.py -v
```

---

## Current Features

* Multi-provider AI workflow
* Technology news retrieval
* OpenAI summarization
* Cohere sentiment analysis
* Token usage tracking
* Unit testing with mocked providers
* Modular architecture

---

## Planned Improvements

Future enhancements include:

* asynchronous processing of multiple articles
* provider fallback mechanism
* estimated cost calculation in USD
* configurable news categories
* result export to Markdown or JSON
* logging and monitoring

---

## Learning Objectives

This project demonstrates:

* modular Python application design
* API integration
* environment configuration
* multi-provider LLM workflows
* prompt engineering
* unit testing with mocking
* workflow validation
* cost and token tracking

---

## Status

✅ Configuration validated

✅ News API integrated

✅ OpenAI integrated

✅ Cohere integrated

✅ Multi-provider summarization workflow completed

✅ Unit tests passing

⏳ Asynchronous processing planned as a future enhancement
