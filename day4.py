import json

def build_request(question, max_words=50):
    return {
        "question": question,
        "max_words": max_words,
        "tags": ["learning", "cloud"],
    }

req = build_request("What is Docker?")
print(req["question"])
print(json.dumps(req, indent=2))

def count_words(text):
    words = len(text.split())
    chars = len(text)
    return {"words": words, "chars": chars}
result = count_words("Docker packages apps into containers")
print(json.dumps(result, indent=2))

raw = '{"answer": "A container tool", "tokens": 12}'
data = json.loads(raw)
print(data["answer"], "used", data["tokens"], "tokens")