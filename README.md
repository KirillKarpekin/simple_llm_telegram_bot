# Telegram LLM Bot

A simple Telegram bot that responds to users using a **large language model (LLM)** via **OpenRouter** and **LangChain**.  
The bot takes text messages from users and returns a reversed or processed response (based on the system prompt).

---

## 🔹 Features

- Uses **LangChain** to manage LLMs and prompts
- Connects to **OpenRouter** (supports any LLM provided by the service)
- Asynchronous Telegram bot using `python-telegram-bot` v20+
- Handles all text messages and replies automatically
- `.env` file stores API keys securely (not uploaded to GitHub)

---

## 💻 Requirements

- Python 3.10+
- Telegram Bot Token
- OpenRouter API Key

### Install Dependencies

```bash
pip install -r requirements.txt

### Example requirements.txt:

python-telegram-bot==20.7
langchain
langchain-openai
python-dotenv
openai

⚙️ Setup

1. Create a .env file in the project root:

TELEGRAM_BOT_TOKEN=your_telegram_bot_token
OPENROUTER_API_KEY=your_openrouter_api_key

2. Make sure .gitignore contains:

.env
__pycache__/
*.pyc
venv/

🚀 Running the Bot
-python bot.py

🧠 How it Works
-User sends a message to the bot
-Bot formats a prompt using LangChain
-Prompt is sent to the OpenRouter LLM
-The response is returned to the user in Telegram

🔧 Possible Improvements
-Chat history storage
-Retrieval-Augmented Generation (RAG) with documents
-Asynchronous streaming of LLM responses
-Handling Telegram commands (/help, /about)
-Customizing model behavior through system prompts

📂 Project Structure
telegram-llm-bot/
│
├─ bot.py             # Main bot code
├─ requirements.txt   # Dependencies
├─ .gitignore         # Ignored files
├─ README.md          # This file
└─ .env               # API keys (not in GitHub)

⚠️ Security
-Never upload .env with API keys to a public repository
-Limit the frequency of LLM requests to avoid hitting API limits