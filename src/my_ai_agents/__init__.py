from my_ai_agents.config import get_settings


def main() -> None:
    settings = get_settings()
    print(f"Hello from my-ai-agents! Running in {settings.ENVIRONMENT} mode.")

    if settings.DEBUG:
        print("Debug mode is ON")

    # Example of using the configuration
    print(
        f"Using OpenAI with max tokens: {settings.MAX_TOKENS}, temperature: {settings.TEMPERATURE}"
    )
