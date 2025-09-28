"""
This module contains the core AI agent logic.
"""

import os
from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider


# Load environment variables from .env file
load_dotenv()


class AIAgent:
    """
    The main AI agent class that initializes and runs the conversation loop.
    """

    def __init__(self):
        """
        Initializes the AI agent with a model and provider.
        """
        llm_provider = OpenAIProvider(
            api_key=os.getenv("LLM_API_KEY"),
            base_url=os.getenv("LLM_BASE_URL"),
        )
        
        model = OpenAIChatModel(
            model_name=os.getenv("LLM_CHOICE"),
            provider=llm_provider,
        )

        self.agent = Agent(model=model)

    async def chat(self, user_input: str) -> str:
        """
        Runs a single chat interaction with the agent.

        Args:
            user_input (str): The message from the user.

        Returns:
            str: The agent's response.
        """
        # Reason: The .run() method executes the agent's logic,
        # processing the input and generating a response.
        result = await self.agent.run(user_input)
        return result.output
