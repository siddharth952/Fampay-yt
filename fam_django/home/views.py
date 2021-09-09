import asyncio
from django.shortcuts import render
from .yt_session import getChannelStatus, getListVideos
from .models import Video
from .managedatabase import delete_videos_database,  add_to_database


def home(request):
    context = {}
    if request.method == "POST":
        #Search field
        user_search_data = request.POST['searched']
        
        # Let us access in the template, info of each video
        res = getListVideos(user_search_data)['items']

        print(res[0]['kind'])
        # Clear the database
        delete_videos_database()
        # Add to database
        add_to_database(res)
        
        context = {
        'videos': Video.objects.all(),
        'searched': user_search_data,
        }
        
        return render(request, 'home/home.html', context)
    else:
    
    #refresh = asyncio.create_task()
        return render(request, 'home/home.html', {})
