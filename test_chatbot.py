"""Tiny smoke tests for the ARTI 409 chatbot. No API key needed."""

import chatbot


def test_model_is_a_known_claude_model():
    # If someone fat-fingers the model name, this fails before it reaches main.
    assert chatbot.MODEL in {"claude-opus-4-8", "claude-haiku-4-5"}


def test_system_prompt_mentions_the_course():
    # The assistant should know it's helping with ARTI 409.
    assert "ARTI 409" in chatbot.SYSTEM_PROMPT
