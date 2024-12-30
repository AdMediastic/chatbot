# Flask Chatbot with Ollama API

This is a simple chatbot application built using Flask and the Ollama API. It allows users to interact with a language model (`llama3.1:8b`) via a web interface. The chatbot streams responses from the Ollama API in real-time and displays them in a beautifully designed UI.

## Features

- User-friendly web interface to interact with the chatbot.
- Real-time response streaming from the Ollama model.
- Code syntax highlighting for responses that include code snippets.
- Simple and clean UI design using HTML, CSS, and JavaScript.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.x
- Flask
- Requests (for handling API requests)
- Ollama API running locally on your machine.

### Installing Python Dependencies

1. Install the required dependencies using `pip`:

    ```bash
    pip install flask requests
    ```

2. Make sure that the Ollama API server is up and running on `localhost:11434`.

## Setup Instructions

### 1. Start the Ollama API Server

Ensure that the Ollama API is running locally. You can follow the documentation from [Ollama API Docs](https://github.com/ollama/ollama/blob/main/docs/api.md) to start the Ollama API on your machine.

### 2. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/your-repo/flask-chatbot.git
cd flask-chatbot
```
