from googleapiclient.discovery import build
import pprint, json
api_key = 'AIzaSyCbV5smoNcEJcmRdkPXE31UskmeIBTMEk8'
service = build('youtube', 'v3', developerKey=api_key)
request = service.channels().list(
    part="snippet",
    id = 'UCpLo996bL7AdzNeRlY9DZEA'
)
respone = request.execute()
pprint.pprint(respone)
service.close()
