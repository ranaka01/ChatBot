# Chat Bot

A simple web-based chatbot using Flask (Python backend) and HTML/JS frontend. It connects to the OpenRouter API to generate responses.

## Features
- Modern chat UI (Bootstrap, FontAwesome)
- Markdown support for bot replies
- Uses OpenRouter API for AI responses
- Environment variable support for API keys

## Setup

1. **Clone the repository**
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up your `.env` file**
   - Create a `.env` file in the project root:
     ```env
     OPENROUTER_API_KEY=your_openrouter_api_key_here
     ```
4. **Run the Flask app**
   ```bash
   python app.py
   ```
5. **Open your browser**
   - Go to `http://localhost:5000`

## File Structure
- `app.py` — Flask backend
- `index.html` — Frontend UI
- `requirements.txt` — Python dependencies
- `.env` — API key (not tracked by git)
- `.gitignore` — Files/folders to ignore in git

## Security
- Never share your `.env` file or API keys publicly.
- The `.gitignore` is set to prevent sensitive files from being committed.

## License
MIT
