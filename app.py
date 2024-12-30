import os
import requests
import json  # Importing the correct json module
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

OLLAMA_API_URL = "http://localhost:11434/api/generate"  # Correct API URL for Ollama

# Function to call Ollama API and get a response
def get_ollama_response(message):
    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama3.1:8b",  # Model you are using
        "prompt": message        # Message sent by the user
    }

    try:
        # Make the POST request with streaming
        response = requests.post(OLLAMA_API_URL, json=data, headers=headers, stream=True)

        # Check if the response is successful
        response.raise_for_status()

        # Initialize an empty string to accumulate the response
        full_response = ""
        
        # Iterate over the streamed chunks
        for chunk in response.iter_lines():
            if chunk:
                # Decode and parse the JSON chunk
                try:
                    chunk_data = chunk.decode('utf-8')
                    json_data = json.loads(chunk_data)  # Using json.loads here for parsing
                    print(f"Received chunk: {json_data}")  # Log the chunk data for debugging
                    
                    # Concatenate the response part
                    if 'response' in json_data:
                        full_response += json_data['response']
                    
                    # If 'done' is true, stop accumulating and return the response
                    if json_data.get('done', False):
                        break

                except Exception as e:
                    print(f"Error while processing chunk: {e}")
                    continue

        # Return the complete response after streaming
        return full_response.strip() or "No response from model."

    except requests.exceptions.RequestException as e:
        print(f"Error connecting to Ollama API: {e}")
        return f"Error connecting to Ollama API: {e}"

    except Exception as e:
        print(f"General Error: {e}")
        return f"General Error: {e}"

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# API endpoint to interact with the chatbot
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['message']
    bot_response = get_ollama_response(user_input)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
