# Install Gemini SDK
!pip install -q google-generativeai

import google.generativeai as genai
import os
from google.colab import files

# ==============================
# 🔑 STEP 1: Enter your API Key (DO NOT share it publicly!)
# ==============================
api_key = input("AIzaSyBqx_BmTlxnmTHXA1q0g1u5pmBUiD27qN8 ").strip()
genai.configure(api_key=api_key)

# ==============================
# ⚡ STEP 2: Create Model
# ==============================
MODEL = "gemini-2.0-flash"
chat_model = genai.GenerativeModel(MODEL)
chat = chat_model.start_chat(history=[])

# ==============================
# 💬 STEP 3: Chat Function
# ==============================
def chatbot_response(user_input, image_path=None):
    parts = []
    if image_path:  # If user provided an image
        with open(image_path, "rb") as f:
            img_data = f.read()
        parts.append({"mime_type": "image/jpeg", "data": img_data})
    parts.append(user_input)

    response = chat.send_message(parts)
    return response.text
