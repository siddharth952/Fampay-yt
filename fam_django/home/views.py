import asyncio
from django.shortcuts import render
from .yt_session import getChannelStatus, getListVideos



def home(request):
    context = {}
    if request.method == "POST":
        #Search field
        user_search_data = request.POST['searched']
        
        # Let us access in the template, info of each video
        #context['user_search'] = user_search_data
        res = getListVideos(user_search_data)
        context = {
        'videos': res
        }
        return render(request, 'home/home.html', context)
    else:
    
    #refresh = asyncio.create_task()
        return render(request, 'home/home.html', {})
