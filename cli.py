"""
This module provides a command-line interface for the AI agent.
"""

import asyncio
from agent import AIAgent


async def main():
    """
    The main entry point for the CLI application.
    """
    print("Welcome to the Pydantic AI Agent! Type 'exit' to quit.")
    ai_agent = AIAgent()

    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Exiting application. Goodbye!")
                break

            response = await ai_agent.chat(user_input)
            print(f"Agent: {response}")

        except KeyboardInterrupt:
            print("\nExiting application. Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Reason: asyncio.run() is the standard way to start an async Python application.
    asyncio.run(main())

