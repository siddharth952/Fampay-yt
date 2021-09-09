from googleapiclient.discovery import build
from urllib.error import HTTPError
from .keys import API_KEY
'''
build(serviceName, version, http=None, discoveryServiceUrl=DISCOVERY_URI, 
developerKey=None, model=None, requestBuilder=HttpRequest, 
credentials=None, cache_discovery=True, cache=None, 
client_options=None, adc_cert_path=None, adc_key_path=None, 
num_retries=1)

https://github.com/googleapis/google-api-python-client/blob/main/docs/start.md

'''
yt_service = build('youtube', 'v3', developerKey=API_KEY)

'''
Returns search results that match the query parameters.
By default, result set identifies matching video, channel, 
and playlist resources, configure queries to only retrieve a specific type of resource.
'''
def getListVideos(keyword:str, page_token=''):
    # Call the API
   
    req = yt_service.search().list(
        part = 'snippet',
        maxResults = '25',
        q = keyword,
        type = 'video',
        pageToken = page_token
    )
        
    try:
       res = req.execute()
       
    except HttpError as e:
        print('Error response status code : {0}, reason : {1}'.format(e.status_code, e.error_details))
    return res



def getChannelStatus(channel:str):
    # Call the API
    req = yt_service.channels().list(
        part = 'status',
        forUsername = channel
        )
    res = req.execute()
    return res
    

