from dotenv import load_dotenv
import requests
from typing import Optional
import os
load_dotenv()
APPLICATION_TOKEN =  os.getenv("LF_TOKEN")

BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "ad90a74f-3f20-4fda-8767-cd073e2a026f"
FLOW_ID = "15d06b80-51ad-4db9-bf38-3b9010a4d1f8"
ENDPOINT = "trail"
def get_tweeks(query):
    return {
        "TextInput-JXN8i": {
            "input_value": query
        }
    }

def run_flow(message: str,
  endpoint: str,
  output_type: str = "chat",
  input_type: str = "chat",
  tweaks: Optional[dict] = None,
  application_token: Optional[str] = None) -> dict:
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{endpoint}"

    payload = {
        "input_value": message,
        "output_type": output_type,
        "input_type": input_type,
    }
    headers = None
    if tweaks:
        payload["tweaks"] = tweaks
    if application_token:
        headers = {"Authorization": "Bearer " + application_token, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

def extract_output_text(response):
    try:
        # Traverse the response dictionary to find the proper output text
        output_data = response.get('outputs', [])[0].get('outputs', [])[0].get('results', {}).get('text', {}).get('data', {}).get('text', '')
        
        # Return the cleaned output text
        return output_data.strip()
    
    except (IndexError, KeyError) as e:
        # Handle any possible errors in case the structure is different or missing keys
        return f"Error extracting text: {e}"
    
def ask_ai(input):
    tweeks = get_tweeks(input)
    response = run_flow("",ENDPOINT, tweaks=tweeks, application_token=APPLICATION_TOKEN)
    return extract_output_text(response)
