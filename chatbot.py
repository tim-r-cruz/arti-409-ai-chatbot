"""
ARTI 409 — Simple AI Chatbot
A minimal command-line chatbot powered by Anthropic's Claude API.

This file is intentionally small and heavily commented. The point of this
repository is to practice using GitHub Desktop, so the app itself stays simple.

Run it with:   python chatbot.py
Type 'quit' (or 'exit') to end the conversation.
"""

import os
import sys

import anthropic
from dotenv import load_dotenv

# Load variables from a local .env file (your API key lives there).
# .env is listed in .gitignore, so your secret key is NEVER committed to GitHub.
load_dotenv()

# The model we'll talk to. Claude Opus 4.8 is Anthropic's most capable model.
# For faster, cheaper testing you can switch this to "claude-haiku-4-5".
MODEL = "claude-opus-4-8"

# A "system prompt" sets the chatbot's personality and instructions.
SYSTEM_PROMPT = (
    "You are a friendly, encouraging teaching assistant for ARTI 409, "
    "a college class about artificial intelligence. Keep your answers clear "
    "and concise, and explain technical ideas in plain language."
)


def main() -> None:
    # Make sure the API key is available before we start.
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ERROR: No API key found.")
        print("Copy .env.example to a new file named .env, then paste your")
        print("Anthropic API key into it. Get a key at https://console.anthropic.com/")
        sys.exit(1)

    # The client automatically reads ANTHROPIC_API_KEY from the environment.
    client = anthropic.Anthropic()

    # We keep the whole conversation in this list so the chatbot remembers
    # what was said earlier in the chat.
    conversation = []

    print("=" * 60)
    print("  ARTI 409 AI Chatbot   (type 'quit' to exit)")
    print("=" * 60)

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() in ("quit", "exit"):
            print("\nGoodbye! 👋")
            break

        if not user_input:
            continue

        # Add the user's message to the running history.
        conversation.append({"role": "user", "content": user_input})

        # Stream Claude's reply so it appears word-by-word, like a real chat.
        print("\nClaude: ", end="", flush=True)
        reply_text = ""
        with client.messages.stream(
            model=MODEL,
            max_tokens=1024,
            system=SYSTEM_PROMPT,
            messages=conversation,
        ) as stream:
            for text in stream.text_stream:
                print(text, end="", flush=True)
                reply_text += text
        print()  # newline after the streamed reply

        # Add Claude's reply to the history so it has context next turn.
        conversation.append({"role": "assistant", "content": reply_text})


if __name__ == "__main__":
    main()
