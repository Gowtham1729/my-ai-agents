from autogen_core.models._model_client import ModelInfo
from autogen_ext.models.anthropic import AnthropicChatCompletionClient
from autogen_ext.models.openai import OpenAIChatCompletionClient

from my_ai_agents.config import get_settings

DEFAULT_MODEL_INFO: ModelInfo = ModelInfo(
    vision=True,
    function_calling=True,
    json_output=True,
    family="default",
    structured_output=True,
    multiple_system_messages=True,
)


def get_openai_model_client(
    model: str = "gpt-4.1-nano-2025-04-14", model_info: ModelInfo = DEFAULT_MODEL_INFO
) -> OpenAIChatCompletionClient:
    """
    Get an OpenAI model client configured with the settings.
    
    Args:
        model: The OpenAI model name to use
        model_info: Configuration for model capabilities

    Returns:
        OpenAIChatCompletionClient: Configured OpenAI model client
    """
    settings = get_settings()

    return OpenAIChatCompletionClient(
        model=model,
        api_key=settings.OPENAI_API_KEY,
        max_tokens=settings.MAX_TOKENS,
        temperature=settings.TEMPERATURE,
        model_info=model_info,
    )


def get_anthropic_model_client(
    model: str, model_info: ModelInfo = DEFAULT_MODEL_INFO
) -> AnthropicChatCompletionClient:
    """
    Get an Anthropic model client configured with the settings.
    
    Args:
        model: The Anthropic model name to use
        model_info: Configuration for model capabilities

    Returns:
        AnthropicChatCompletionClient: Configured Anthropic model client
    """
    settings = get_settings()

    return AnthropicChatCompletionClient(
        model=model,
        api_key=settings.ANTHROPIC_API_KEY,
        max_tokens=settings.MAX_TOKENS,
        temperature=settings.TEMPERATURE,
        model_info=model_info,
    )


def get_gemini_model_client(
    model: str, model_info: ModelInfo = DEFAULT_MODEL_INFO
) -> OpenAIChatCompletionClient:
    """
    Get a Gemini model client configured with the settings.
    
    Args:
        model: The Gemini model name to use
        model_info: Configuration for model capabilities

    Returns:
        OpenAIChatCompletionClient: Configured Gemini model client using OpenAI-compatible API
    """
    settings = get_settings()

    return OpenAIChatCompletionClient(
        model=model,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
        api_key=settings.GEMINI_API_KEY,
        max_tokens=settings.MAX_TOKENS,
        temperature=settings.TEMPERATURE,
        model_info=model_info,
    )
    
    
def get_local_models() -> list[str]:
    """
    Get a list of available local models.

    Returns:
        list[str]: List of available local models
    """
    settings = get_settings()
    return settings.AVAILABLE_LOCAL_LLM_MODELS


def get_local_model_client(model: str, model_info: ModelInfo = DEFAULT_MODEL_INFO) -> OpenAIChatCompletionClient:
    """
    Get a local model client configured with the settings.
    
    Args:
        model: The local model name to use
        model_info: Configuration for model capabilities

    Returns:
        OpenAIChatCompletionClient: Configured local model client using OpenAI-compatible API
    """
    settings = get_settings()

    return OpenAIChatCompletionClient(
        model=model,
        base_url=f"http://{settings.LM_STUDIO_HOST}:{settings.LM_STUDIO_PORT}/v1",
        api_key="sk-dummy-key",
        max_tokens=settings.MAX_TOKENS,
        temperature=settings.TEMPERATURE,
        model_info=model_info,
    )
