# import package
import africastalking


# Initialize SDK
username = "sandbox"    # use 'sandbox' for development in the test environment
api_key = "c933b6fc73c642f245ab81fd688a43e7eae3510937214ba0860518b6c7cdcc37"  # use your sandbox app API key for
                                                                              # development in the test environment
africastalking.initialize(username, api_key)


# Initialize a service e.g. SMS
sms = africastalking.SMS

# Use the service synchronously
response = sms.send("Hello Message!", ["256705920191"])

# Or use it asynchronously
def on_finish(error, response):
    if error is not None:
        raise error
    print(response)
