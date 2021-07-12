from googleapiclient.discovery import build
import pprint
api_key = 'AIzaSyCbV5smoNcEJcmRdkPXE31UskmeIBTMEk8'
service = build('youtube', 'v3', developerKey=api_key)
request = service.subscriptions().list(
    part="subscriberSnippet",

    mySubscribers = True
)
respone = request.execute()
pprint.pprint(respone)
service.close()