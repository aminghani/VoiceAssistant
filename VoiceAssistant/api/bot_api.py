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
        
        #print(f"bot_responses: {bot_responses}")
        control_json = None
        if len(bot_responses) > 1 and bot_responses[1]['custom'] is not None:
            control_json = bot_responses[1]['custom']
        return bot_responses[0]['text'], control_json 
    else:
        return f"Error: Received status code {response.status_code}", None

"""
# Example usage
user_message = "Hello"
bot_responses = send_message(user_message)

print(f"User: {user_message}")
for response in bot_responses:
    print(f"Bot: {response}")
"""
