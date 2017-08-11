# Import the helper gateway class
from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException
# Specify your login credentials
username = "emupuya"
apikey   = "73ec71f21c21e25e0b496c37845ebfa08d2dc3ab431a6a97b74b70dd5340a3a5"


def send_verification_sms(phone_number,code):
    # Specify the numbers that you want to send to in a comma-separated list
    # Please ensure you include the country code (+256 for Uganda)
    # to      = "+256705920191"
    to      = phone_number
    # And of course we want our recipients to know what we really do
    message = "Tossapp verification code: "+str(code)
    # Create a new instance of our awesome gateway class
    gateway = AfricasTalkingGateway(username, apikey)
    # Any gateway errors will be captured by our custom Exception class below,
    # so wrap the call in a try-catch block
    try:
        # Thats it, hit send and we'll take care of the rest.

        results = gateway.sendMessage(to, message)
        success_message = ''
        for recipient in results:
            # status is either "Success" or "error message"
            success_message += 'number=%s;status=%s;messageId=%s;cost=%s' % (recipient['number'],
                                                                             recipient['status'],
                                                                             recipient['messageId'],
                                                                             recipient['cost'])
            print success_message

        return success_message
    except AfricasTalkingGatewayException, e:
        print 'Encountered an error while sending: %s' % str(e)