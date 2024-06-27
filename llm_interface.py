import os
from anthropic import Anthropic

def get_response(user_input):
    client = Anthropic(
        api_key=os.environ.get("ANTHROPIC_API_KEY"),
    )
    message = client.messages.create(
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": user_input,
            }
        ],
        model="claude-3-opus-20240229",
    )
    return message.content
