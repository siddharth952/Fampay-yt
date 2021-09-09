import asyncio
from django.core import paginator
from django.shortcuts import render
from .yt_session import getChannelStatus, getListVideos
from .models import Video
from .managedatabase import *
from django.core.paginator import Paginator  

def home(request):
    context = {}
    if request.method == "POST":
        #Search field
        user_search_data = request.POST['searched']
        
        # Let us access in the template, info of each video
        data = getListVideos(user_search_data)
        
        
        
        # paginator_ = Paginator
        # page = request.GET.get('page')
        
        
        # For Pagination YoutubeAPI
        # next_page_token = data['nextPageToken']
        # if page == '2':
        #     prev_page_token = data['prevPageToken']
        #     data = getListVideos(user_search_data, page_token=next_page_token)
        sortby = ''
        if request.GET.get('sortby'):
            sortby = request.GET.get('sortby')
            
        res = data['items']
        
        # Clear the database
        delete_videos_database()
        # Add to database
        add_to_database(res)
        
        context = {
        'videos': sort_filter_videos(sort_by=sortby),
        'searched': user_search_data,
        }
        
        return render(request, 'home/home.html', context)
    else:
    
    #refresh = asyncio.create_task()
        return render(request, 'home/home.html', {})
