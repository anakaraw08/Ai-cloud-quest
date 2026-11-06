import os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("ANTHROPIC_API_KEY")
print("Key loaded:", key is not None)
print("Starts with:", key[:7] if key else None)