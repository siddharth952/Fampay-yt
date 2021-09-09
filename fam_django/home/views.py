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
        
        # Clear the database
        delete_videos_database()
        
        
        #Search field
        user_search_data = request.POST['searched']
        
        # Let us access in the template, info of each video
        data = getListVideos(user_search_data)
        
        # Sorting
        sortby = ''
        if request.GET.get('sortby'):
            sortby = request.GET.get('sortby')
            
        res = data['items']
        # Add to database
        add_to_database(res)
        
        
        # Database Paginator
        paginator_ = Paginator(sort_filter_videos(sort_by=sortby), 8)
        page = request.GET.get('page')
        video_build_list = paginator_.get_page(page)
        
        
        # For Pagination YoutubeAPI
        # next_page_token = data['nextPageToken']
        # if page == '2':
        #     prev_page_token = data['prevPageToken']
        #     data = getListVideos(user_search_data, page_token=next_page_token)
        
        
        
        
        context = {
        'videos': video_build_list,
        'video_build_list': video_build_list,
        'searched': user_search_data,
        }
        
        return render(request, 'home/home.html', context)
    else:
    
        # Sorting
        sortby = ''
        if request.GET.get('sortby'):
            sortby = request.GET.get('sortby')
            
        # Database Paginator
        paginator_ = Paginator(sort_filter_videos(sort_by=sortby), 10)
        page = request.GET.get('page')
        video_build_list = paginator_.get_page(page)
    
        
        
        context = {
        'videos': video_build_list,
        'video_build_list': video_build_list,
        }
        
        return render(request, 'home/home.html', context)
