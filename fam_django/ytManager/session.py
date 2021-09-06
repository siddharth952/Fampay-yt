from googleapiclient.discovery import build
from keys import API_KEY
'''
build(serviceName, version, http=None, discoveryServiceUrl=DISCOVERY_URI, 
developerKey=None, model=None, requestBuilder=HttpRequest, 
credentials=None, cache_discovery=True, cache=None, 
client_options=None, adc_cert_path=None, adc_key_path=None, 
num_retries=1)

https://github.com/googleapis/google-api-python-client/blob/main/docs/start.md

'''
yt_service = build('youtube', 'v3', developerKey=API_KEY)

# Call the API
req = yt_service.channels().list(
    part='status',
    forUsername='siddharth952'
    )
res = req.execute()
print(res)
