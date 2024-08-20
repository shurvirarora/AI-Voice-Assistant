import requests
from openai import OpenAI, APIError, RateLimitError

openai_client = OpenAI()

def speech_to_text(audio_binary):
    base_url = "https://sn-watson-stt.labs.skills.network"
    api_url = f"{base_url}/speech-to-text/api/v1/recognize"
    params = {'model': 'en-US_Multimedia'}

    try:
        response = requests.post(api_url, params=params, data=audio_binary)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        data = response.json()
        if 'results' in data:
            text = data['results'][0]['alternatives'][0]['transcript']
            print('Recognized text:', text)
            return text
        else:
            return "No text recognized."
    except requests.RequestException as e:
        print(f"Network error during Speech to Text: {str(e)}")
        return None

def text_to_speech(text, voice=""):
    base_url = "https://sn-watson-stt.labs.skills.network"
    api_url = f"{base_url}/text-to-speech/api/v1/synthesize"
    if voice != "" and voice != "default":
        api_url += f"?voice={voice}"

    headers = {'Accept': 'audio/wav', 'Content-Type': 'application/json'}
    json_data = {'text': text}

    try:
        response = requests.post(api_url, headers=headers, json=json_data)
        response.raise_for_status()
        print('Text to Speech response:', response)
        return response.content
    except requests.RequestException as e:
        print(f"Network error during Text to Speech: {str(e)}")
        return None

def openai_process_message(user_message):
    prompt = "Act like a personal assistant. You can respond to questions, translate sentences, summarize news, and give recommendations."
    try:
        openai_response = openai_client.chat.completions.create(
            model="gpt-3.5-turbo", 
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": user_message}
            ],
            max_tokens=4000
        )
        response_text = openai_response.choices[0].message.content
        print("OpenAI response:", openai_response)
        return response_text
    except (APIError, RateLimitError) as e:
        print(f"OpenAI error: {str(e)}")
        return "An error occurred while processing your message. Please try again later."

