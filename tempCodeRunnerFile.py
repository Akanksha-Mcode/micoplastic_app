mport requests

# 🔑 Your Gemini API key
API_KEY = "AIzaSyBqx_BmTlxnmTHXA1q0g1u5pmBUiD27qN8"

# Gemini endpoint
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

def chat_with_gemini(user_input):
    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts": [
                    {"text": user_input}
                ]
            }
        ]
    }

    response = requests.post(API_URL, headers=headers, json=data)

    if response.status_code == 200:
        reply = response.json()["candidates"][0]["content"]["parts"][0]["text"]
        return reply
    else:
        return f"Error: {response.status_code}, {response.text}"


if __name__ == "__main__":
    print("🤖 Gemini Chatbot (type 'exit' to quit)\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye 👋")
            break