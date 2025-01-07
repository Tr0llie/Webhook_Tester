"""
LICENSED UNDER MIT LICENSE
COPYRIGHT @ 2025 tr0llie 
"""
# ALSO IF YOU USE THIS TO SPAM SOMEONE'S WEBHOOK WITH PORN, FUCK U AND FUCK UR MOM, UR USELESS 
import requests
import time
WEBHOOK = "https://webhook-example.com" # PUT URL WEBHOOK URL HERE
PAYLOAD = {
    "content": "This rate limit tester was created by tr0llie, view repo here https://github.com/Tr0llie/Webhook_Tester/new/main . \n if your webhook is being spammed, please do not share your webhook url with anyone, if you are hosting it on an online service, set up an enviroment variable. ",
    "username": "Rate Limit Tester - Tr0llie"  
}
BATCH = 1 #Deafult is one but feel free to change it
INTERVAL = 1 # Deafult is one second but feel free to change
def send_post_requests():
    try:
        while True: 
            for i in range(MESSAGES_PER_BATCH):
                response = requests.post(WEBHOOK_URL, json=PAYLOAD)
                print(f"Message {i+1}: Status Code = {response.status_code}, Response = {response.text}")
                # If it is being rate limited, the script will stop as this is a ratelimit tester 
                if response.status_code != 200:
                    print("Error detected. Stopping...")
                    return # IF you dont want it to stop, remove the return keyword 
            print(f"Waiting {INTERVAL} seconds before the next batch...")
            time.sleep(INTERVAL)
    except KeyboardInterrupt:
        print("Script stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    send_post_requests()
