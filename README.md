# Chat Bot (Flask + OpenRouter)

A simple web-based chatbot using Flask (Python backend) and HTML/JS frontend. It connects to the OpenRouter API to generate responses.

## Features
- Conversational AI using OpenRouter API
- Modern chat UI with Markdown support for bot replies
- Typing indicator and smooth UX
- CORS enabled for easy frontend-backend communication
- Easy deployment (single Python file backend)

## Requirements
- Python 3.8+
- pip
- OpenRouter API key

## Setup

1. **Clone the repository:**
   
2. **Create a virtual environment (optional but recommended):**
   ```sh
   python -m venv env
   env\Scripts\activate  # On Windows
   # Or
   source env/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   - Create a `.env` file in the project root:
     ```env
     OPENROUTER_API_KEY=your_openrouter_api_key_here
     ```

5. **Run the application:**
   ```sh
   python app.py
   ```
   The app will be available at [http://localhost:5000](http://localhost:5000)

## Deployment
- For production, use a WSGI server like Waitress or Gunicorn instead of Flask's built-in server.
- Make sure to set `threaded=True` and disable debug mode in `app.py`.

## File Structure
```
├── app.py           # Flask backend
├── index.html       # Frontend UI
├── requirements.txt # Python dependencies
└── .env             # Environment variables (not committed)

```

![image](https://github.com/user-attachments/assets/6be04dcf-8498-40ba-bf62-9c723b8ed393)



