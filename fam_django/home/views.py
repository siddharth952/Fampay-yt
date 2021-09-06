from django.shortcuts import render


# Test
videos = [
    {
        'title': 'Unboxing the new Ps5',
        'author': 'UnboxingTherpy',
        'date_uploaded': '03-2-19',
        'url': 'https://youtu.be/embed/5pUKnoGcPWQ'
    },
    {
        'title': 'Unboxing the new Xbox',
        'author': 'UnboxingTherpy',
        'date_uploaded': '03-2-20'
    },
    {
        'title': 'Unboxing the new Pc',
        'author': 'UnboxingTherpy',
        'date_uploaded': '03-2-22'
    },
    {
        'title': 'Unboxing the new Wii',
        'author': 'UnboxingTherpy',
        'date_uploaded': '13-5-21'
    },
]




def home(request):
    # Let us access in the template, info of each video
    context = {
        'videos': videos
    }
    return render(request, 'home/home.html', context)