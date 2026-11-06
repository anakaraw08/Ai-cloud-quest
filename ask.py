import sys
from dotenv import load_dotenv
from anthropic import Anthropic
from anthropic import AuthenticationError, APIError

load_dotenv()
client = Anthropic()  # reads ANTHROPIC_API_KEY from the environment

question = " ".join(sys.argv[1:]) or "Explain Docker in one sentence."
try:
    msg = client.messages.create(
        model="claude-haiku-5-5",
        max_tokens=200,
        messages=[{"role": "user", "content": question}],
        system="You are a patient cloud engineering tutor. Answer in under 80 words.",
    )
except AuthenticationError as e:
    print(f"Error occurred: {e}")
    sys.exit(1)
except APIError as e:
    print(f"Error occurred: {e}")
    sys.exit(1)

print(msg.content[0].text)
print("---")
print("input tokens:", msg.usage.input_tokens,
      "| output tokens:", msg.usage.output_tokens)
