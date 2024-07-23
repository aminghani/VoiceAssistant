import requests
import json

def send_message(message):
    # The URL for the Rasa webhook
    url = "http://localhost:5005/webhooks/rest/webhook"
    
    # The payload containing the message
    payload = {
        "sender": "user",
        "message": message
    }
    
    # Send a POST request to the Rasa server
    response = requests.post(url, json=payload)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        bot_responses = response.json()
        
        # Extract and return the bot's messages
        return [resp['text'] for resp in bot_responses if 'text' in resp]
    else:
        return [f"Error: Received status code {response.status_code}"]

"""
# Example usage
user_message = "Hello"
bot_responses = send_message(user_message)

print(f"User: {user_message}")
for response in bot_responses:
    print(f"Bot: {response}")
"""
