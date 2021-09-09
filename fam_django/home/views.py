import asyncio
from django.shortcuts import render
from .yt_session import getChannelStatus, getListVideos
from .models import Video


def home(request):
    context = {}
    if request.method == "POST":
        #Search field
        user_search_data = request.POST['searched']
        
        # Let us access in the template, info of each video
        #context['user_search'] = user_search_data
        res = getListVideos(user_search_data)['items']
        
        context = {
        'videos': res,
        'searched': user_search_data,
        }

        print(res[0]['kind'])
    
        
        # Clear the database
        Video.objects.all().delete()
        # Add to database
        for v in res:
            snippet = v['snippet']
            formated_date = snippet['publishedAt']
            vid = Video(title= snippet['title'], description= snippet['description'], publishTime= formated_date, thumbnail_url= snippet['thumbnails']['medium']['url'], url= v['id']['videoId'], channelTitle=snippet['channelTitle'])
            print("Added:",vid.title)
            vid.save()
        
        
        
        return render(request, 'home/home.html', context)
    else:
    
    #refresh = asyncio.create_task()
        return render(request, 'home/home.html', {})
