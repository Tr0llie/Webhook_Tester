# Webhook_Tester
A simple script that'll let you test your webhook ratelimit

> # NOTE
> DO NOT USE THIS TO ABUSE SOMEONE's WEBHOOK.
> 
> I am not responsible for any of the damage caused
> 
> This repo is use for testing webhooks, not spamming them.

*Gooluck!*

# Startup 
make a virtual env so the python script can run correctly

Then
```pip install requests```

# Configure
In the var named **WEBHOOK**, insert your webhook url 

in the var named **PAYLOAD**, insert your needed context 

The **BATCH** var is for how many message should be sent per batch, This is to test the rate limit of the webhook.

The **INTERVAL** var is how many second the program should wait before sending another request. This is used to test rate limit of xyz webhook

To stop the program **Ctrl+C**
