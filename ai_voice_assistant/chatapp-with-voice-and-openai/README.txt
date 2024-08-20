# Voice-Enabled Chat Application with OpenAI and IBM Watson

## Project Overview
This project is a voice-enabled chat application that leverages OpenAI's GPT-3.5 for text processing and IBM Watson's Speech-to-Text and Text-to-Speech services for voice interaction capabilities. It allows users to interact through voice commands, receive text responses processed by GPT-3.5, and hear the responses spoken back using IBM Watson's Text-to-Speech.

## Features
- **Voice to Text**: Converts user's spoken input to text using IBM Watson Speech-to-Text.
- **Text Processing**: Processes the transcribed text using OpenAI's GPT-3.5 model to generate relevant responses.
- **Text to Speech**: Converts the AI-generated text responses back to speech using IBM Watson Text-to-Speech.

## Prerequisites
- Python 3.10 or above
- Docker
- An API key for IBM Watson Speech-to-Text and Text-to-Speech services
- An API key for OpenAI

## Setup and Installation
1. **Clone the Repository**:
git clone https://github.com/<your-github-username>/voice-chatapp-openai-watson.git
cd voice-chatapp-openai-watson

2. **Install Dependencies**:
- Create a virtual environment (optional but recommended):
  ```
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
  ```
- Install required Python packages:
  ```
  pip install -r requirements.txt
  ```

3. **Environment Variables**:
- Create a `.env` file in the project root directory and add your API keys:
  ```
  OPENAI_API_KEY=your_openai_api_key_here
  WATSON_API_KEY=your_watson_api_key_here
  ```

4. **Running the Application**:
- Start the server:
  ```
  python server.py
  ```
- The application should now be running on `http://localhost:8000`.

## Usage
Navigate to `http://localhost:8000` in your web browser. You should see the interface for the voice-enabled chat application. Speak into your microphone to interact with the chatbot, and receive both textual and spoken responses.

## Contributing
Contributions to the project are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature.
3. Commit your changes.
4. Push to the branch.
5. Open a pull request.

