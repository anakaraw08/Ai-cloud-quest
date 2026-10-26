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
count_words = '{"words": "5", "chars": 27}'
data = json.loads(count_words)
print(data["words"], "huh", data["chars"], "chars")

