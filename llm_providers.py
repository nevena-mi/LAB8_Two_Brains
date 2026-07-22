from openai import OpenAI
import cohere

from config import OPENAI_API_KEY, COHERE_API_KEY


# -------------------------
# Initialize clients
# -------------------------

openai_client = OpenAI(
    api_key=OPENAI_API_KEY
)

cohere_client = cohere.ClientV2(
    api_key=COHERE_API_KEY
)


# -------------------------
# OpenAI provider
# -------------------------

def test_openai(prompt):
    """
    Send a prompt to OpenAI and return response + usage.
    """

    response = openai_client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return {
        "provider": "OpenAI",
        "response": response.choices[0].message.content,
        "input_tokens": response.usage.prompt_tokens,
        "output_tokens": response.usage.completion_tokens
    }


# -------------------------
# Cohere provider
# -------------------------

def test_cohere(prompt):
    """
    Send a prompt to Cohere and return response.
    """

    #print("Sending request to Cohere...")

    response = cohere_client.chat(
        model="command-r7b-12-2024",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    #print("Cohere response received")

    return {
        "provider": "Cohere",
        "response": response.message.content[0].text
    }


# -------------------------
# Cost tracking display
# -------------------------

def show_usage(result):

    print(f"\nProvider: {result['provider']}")

    if "input_tokens" in result:
        print(f"Input tokens: {result['input_tokens']}")
        print(f"Output tokens: {result['output_tokens']}")

    print("")


# -------------------------
# Checkpoint 3
# -------------------------

if __name__ == "__main__":

    test_prompt = """
    Explain in one sentence why automation workflows are useful.
    """

    print("\n=== Testing OpenAI ===")

    openai_result = test_openai(test_prompt)

    print(openai_result["response"])
    show_usage(openai_result)


    print("\n=== Testing Cohere ===")

    cohere_result = test_cohere(test_prompt)

    print(cohere_result["response"])
    show_usage(cohere_result)