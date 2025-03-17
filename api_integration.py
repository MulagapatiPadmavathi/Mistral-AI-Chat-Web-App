import os
import requests
import logging

API_KEY = os.getenv("MISTRAL_API_KEY")  # Ensure you set this in the environment
API_URL = "https://api.mistral.ai/v1/chat/completions"

logging.basicConfig(filename="logs/error.log", level=logging.ERROR)

def get_response(prompt):
    """Send a prompt to Mistral API and return the response."""
    try:
        if not API_KEY:
            return "Error: API key is missing."

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "mistral-small",
            "messages": [{"role": "user", "content": prompt}]
        }
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()

        if "choices" in response_json and response_json["choices"]:
            return response_json["choices"][0]["message"]["content"]

        return "Mistral AI did not return a valid response."
    
    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed: {e}")
        return "Error: Unable to process request. Try again later."
