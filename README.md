# rag-ai-assistant

A Flask-based AI assistant leveraging Retrieval-Augmented Generation (RAG) to help university students understand programming and AI concepts easily.

## Overview

This project implements a simple AI assistant web service using Flask and Google Generative AI SDK. The assistant uses Retrieval-Augmented Generation (RAG) techniques to provide informative and easy-to-understand answers focused on programming and AI topics for university students.

## Features

- REST API endpoint `/ask` accepting POST requests with JSON payload containing a prompt.
- Integration with Google Gemini model for generating AI responses.
- System instruction sets the AI persona to be polite, friendly, and easy to understand.
- API key securely loaded from environment variables using `.env` file.
- Easy to extend and customize for more complex RAG workflows.

## Tech Stack

- Python 3.12+
- Flask
- Google Generative AI Python SDK (`google-generativeai`)
- python-dotenv for environment variable management

## Getting Started

### Prerequisites

- Python 3.12 or higher
- Google API key with access to Gemini model

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/rag-ai-assistant.git
cd rag-ai-assistant
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your Google API key:

```
GOOGLE_API_KEY=your_actual_api_key_here
```

4. Run the Flask app:

```bash
python app.py
```

5. Send POST requests to `http://127.0.0.1:5000/ask` with JSON payload:

```json
{
  "prompt": "Explain what AI RAG is in brief."
}
```

### Example curl request

```bash
curl -X POST http://127.0.0.1:5000/ask \
-H "Content-Type: application/json" \
-d '{"prompt": "Explain what AI RAG is in brief."}'
```

## Project Structure

```
rag-ai-assistant/
├── app.py          # Main Flask application
├── .env            # Environment variables (API key)
├── requirements.txt
└── README.md
```