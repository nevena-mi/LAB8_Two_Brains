from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# API keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# Configuration
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
MAX_RETRIES = int(os.getenv("MAX_RETRIES", 3))
REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", 30))
DAILY_BUDGET = float(os.getenv("DAILY_BUDGET", 5.00))


def validate_config():
    """
    Check that all required API keys are present.
    """
    missing = []

    if not OPENAI_API_KEY:
        missing.append("OPENAI_API_KEY")

    if not COHERE_API_KEY:
        missing.append("COHERE_API_KEY")

    if not NEWS_API_KEY:
        missing.append("NEWS_API_KEY")

    if missing:
        print("✗ Missing environment variables:")
        for key in missing:
            print(f"  - {key}")
        return False

    print("✓ Configuration validated successfully")
    return True


if __name__ == "__main__":
    validate_config()