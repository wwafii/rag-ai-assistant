from flask import Flask, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load variabel dari file .env
load_dotenv()

app = Flask(__name__)

# Ambil API key dari environment variable
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

@app.route("/ask", methods=["POST"])
def ask_ai():
    data = request.json
    user_prompt = data.get("prompt", "")

    # Setup model dengan system instruction (persona) dalam bahasa Inggris
    model = genai.GenerativeModel(
        "gemini-2.0-flash",
        system_instruction=(
            "You are a polite and friendly AI who responds in language that is easy to understand for university students. "
            "Your focus is to help users grasp concepts in programming and AI."
        )
    )

    # Generate response
    response = model.generate_content(user_prompt)

    return jsonify({
        "response": response.text
    })

if __name__ == "__main__":
    app.run(debug=True)
