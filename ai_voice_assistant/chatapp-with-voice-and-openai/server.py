import base64
import json
from flask import Flask, render_template, request, jsonify
from worker import speech_to_text, text_to_speech, openai_process_message
from flask_cors import CORS
import os

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/speech-to-text', methods=['POST'])
def speech_to_text_route():
    audio_binary = request.data  # Get the user's speech from their request
    try:
        text = speech_to_text(audio_binary)  # Call speech_to_text function to transcribe the speech
        response = jsonify({'text': text})
        response.status_code = 200
    except Exception as e:
        response = jsonify({'error': 'Failed to process speech', 'details': str(e)})
        response.status_code = 500
    return response

@app.route('/process-message', methods=['POST'])
def process_message_route():
    user_message = request.json.get('userMessage')  # Get user's message from their request
    voice = request.json.get('voice', 'default')  # Get user's preferred voice from their request or use default

    try:
        openai_response_text = openai_process_message(user_message)
        openai_response_text = os.linesep.join([s for s in openai_response_text.splitlines() if s])
        openai_response_speech = text_to_speech(openai_response_text, voice)
        openai_response_speech_b64 = base64.b64encode(openai_response_speech).decode('utf-8')

        response = jsonify({
            "openaiResponseText": openai_response_text,
            "openaiResponseSpeech": openai_response_speech_b64
        })
        response.status_code = 200
    except Exception as e:
        app.logger.error(f"Error processing message: {str(e)}")
        response = jsonify({
            'error': 'Failed to process message',
            'details': str(e)
        })
        response.status_code = 500
    return response

if __name__ == "__main__":
    app.run(port=8000, host='0.0.0.0')
