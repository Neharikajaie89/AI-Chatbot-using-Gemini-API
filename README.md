# AI Chatbot using Gemini API

A simple AI chatbot built with **Python** and the **Google Gemini API**. This project allows users to interact with Google's Gemini AI model through a command-line or Python-based chatbot application.

## ✨ Features

* 🤖 AI-powered chatbot using Gemini API
* 🐍 Built with Python
* 💬 Natural-language conversations
* 🔑 Secure API key configuration using environment variables
* ⚡ Fast AI-generated responses
* 🧩 Simple and beginner-friendly implementation

## 🛠️ Technologies Used

* **Python 3.x**
* **Google Gemini API**
* **Google Gen AI Python SDK**
* **python-dotenv**

## 📁 Project Structure

```text
AI-Chatbot-using-Gemini-API/
│
├── main.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/AI-Chatbot-using-Gemini-API.git
cd AI-Chatbot-using-Gemini-API
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Get a Gemini API Key

Create a Gemini API key using **Google AI Studio**.

Create a `.env` file in the project directory:

```env
GEMINI_API_KEY=your_api_key_here
```

### 5. Run the chatbot

```bash
python main.py
```

The chatbot will start and you can begin sending messages to the Gemini AI model.

## 🔐 Environment Variables

The project uses an environment variable to keep the Gemini API key secure.

Example `.env`:

```env
GEMINI_API_KEY=your_api_key_here
```

Make sure `.env` is included in `.gitignore`:

```gitignore
.env
venv/
__pycache__/
```

**Never upload your API key to GitHub or share it publicly.**

## 💡 How It Works

The chatbot follows a simple workflow:

1. The user enters a message.
2. Python sends the message to the Gemini API.
3. Gemini processes the prompt.
4. The API returns an AI-generated response.
5. The chatbot displays the response to the user.
6. The process continues until the user exits the chatbot.

## 📦 Example `requirements.txt`

```text
google-genai
python-dotenv
```

## 🖥️ Example

```text
You: Hello!
Gemini: Hello! How can I help you today?

You: Explain Python in simple words.
Gemini: Python is a beginner-friendly programming language...
```

## 🔮 Future Improvements

* [ ] Add a graphical user interface
* [ ] Store conversation history
* [ ] Add streaming responses
* [ ] Add voice input and output
* [ ] Support multiple Gemini models
* [ ] Add chat export functionality
* [ ] Deploy the chatbot as a web application

## 🤝 Contributing

Contributions are welcome!

1. Fork this repository.
2. Create a new branch.
3. Make your changes.
4. Commit your changes.
5. Push your branch.
6. Create a Pull Request.

## 📄 License

This project is open source and available under the **MIT License**.

---

⭐ If you found this project useful, consider giving it a star!
