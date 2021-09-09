import asyncio
from django.shortcuts import render
from .yt_session import getChannelStatus, getListVideos
from .models import Video
from .managedatabase import *
#from django.core.paginator import Paginator  

def home(request):
    context = {}
    if request.method == "POST":
        #Search field
        user_search_data = request.POST['searched']
        
        # Let us access in the template, info of each video
        data = getListVideos(user_search_data)
        res = data['items']
        
        # For Pagination
        # page = request.GET.get('page')
        # next_page_token = data['nextPageToken']
        # if page > 1:
        #     prev_page_token = data['prevPageToken']
        
        
        # Clear the database
        delete_videos_database()
        # Add to database
        add_to_database(res)
        
        context = {
        'videos': sort_filter_videos(sort_by='publishTime'),
        'searched': user_search_data,
        }
        
        return render(request, 'home/home.html', context)
    else:
    
    #refresh = asyncio.create_task()
        return render(request, 'home/home.html', {})
