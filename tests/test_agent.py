
import pytest
import asyncio
from unittest.mock import AsyncMock, MagicMock
from agent import AIAgent

@pytest.fixture
def mock_env(monkeypatch):
    """
    Mocks environment variables for testing.
    """
    monkeypatch.setenv("LLM_API_KEY", "test_key")
    monkeypatch.setenv("LLM_BASE_URL", "http://localhost:11434/v1")
    monkeypatch.setenv("LLM_CHOICE", "test_model")

def test_ai_agent_initialization(mock_env):
    """
    Tests if the AIAgent class can be initialized.
    """
    try:
        agent = AIAgent()
        assert agent is not None, "Agent should not be None"
        assert hasattr(agent, 'agent'), "AIAgent should have a 'agent' attribute"
    except Exception as e:
        pytest.fail(f"AIAgent initialization failed: {e}")

@pytest.mark.asyncio
async def test_chat_loop(mock_env):
    """
    Tests the conversation loop, mocking the agent's run method.
    """
    agent_instance = AIAgent()

    # Mock the underlying pydantic-ai Agent's .run() method
    mock_run_result = MagicMock()
    mock_run_result.output = "Mocked response"
    agent_instance.agent.run = AsyncMock(return_value=mock_run_result)

    # Test the chat method
    user_input = "Hello, agent!"
    response = await agent_instance.chat(user_input)

    # Assertions
    agent_instance.agent.run.assert_called_once_with(user_input)
    assert response == "Mocked response"
