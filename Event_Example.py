import requests
import json
import os
import sys

# API endpoint and headers
url = "https://api.ailicia.live/v1/events"
headers = {
    "Authorization": "YOUR_API_KEY",  # Replace with your API key
    "Content-Type": "application/json"
}

# Path for the log file
log_file_path = os.path.join(os.getcwd(), "AI_LICIA_LOG.txt")

def clear_log_file():
    """Clear the log file at the start of execution."""
    with open(log_file_path, "w") as log_file:
        log_file.write("")  # Empty the file

def log_message(message):
    """Append a message to the log file."""
    with open(log_file_path, "a") as log_file:
        log_file.write(message + "\n")

# Clear the log file at the start
clear_log_file()

# Capture input1 and input2 from command-line arguments
if len(sys.argv) > 2:
    input1 = sys.argv[1]
    input2 = sys.argv[2]
    log_message(f"Input1 passed as argument: {input1}")
    log_message(f"Input2 passed as argument: {input2}")
else:
    input1 = "UNKNOWN_INPUT1"  # Fallback value if no input1 is provided
    input2 = "UNKNOWN_INPUT2"  # Fallback value if no input2 is provided
    log_message("Missing arguments. Using fallback values.")

# Define the payload for ai_licia
payload = {
    "eventType": "GAME_EVENT",
    "data": {
        "channelName": "YOUR_CHANNEL_NAME",  # Replace with your channel name (lowercase)
        "content": (
            f"THIS IS A PLACEHOLDER TEXT SHOWCASING {input1} AND {input2} AS EXAMPLES OF STREAMER.BOT VARIABLES."
        )
    }
}

# Log the payload for debugging
log_message(f"Payload being sent to the API: {json.dumps(payload, indent=2)}")

# Send the POST request
try:
    response = requests.post(url, headers=headers, json=payload)
    
    # Log the response details
    log_message(f"Response Status Code: {response.status_code}")
    log_message(f"Response Content: {response.text}")

    # Check for successful response
    if response.status_code == 200:
        print("Request succeeded!")
        log_message("Request succeeded!")
    else:
        print(f"Error: {response.status_code} - {response.text}")
        log_message(f"Error: {response.status_code} - {response.text}")

except Exception as e:
    print(f"An exception occurred: {e}")
    log_message(f"An exception occurred: {e}")
