from django.shortcuts import render

# Create your views here.

feed_list = [
    {
        'name': 'transport feed', 
        'contents': [
            {
                'title': 'transport title 1',
                'description': 'transport description 1',
            },
            {
                'title': 'transport title 2',
                'description': 'transport description 2',
            },
            {
                'title': 'transport title 3',
                'description': 'transport description 3',
            },
        ]
    },
    {
        'name': 'health feed',
        'contents': [ 
            {
                'title': 'health title 1',
                'description': 'health description 1',
            },
            {
                'title': 'health title 2',
                'description': 'health description 2',
            },
            {
                'title': 'health title 3',
                'description': 'health description 3',
            },
        ]
    },
    {
        'name': 'town feed',
        'contents': [ 
            {
                'title': 'town title 1',
                'description': 'town description 1',
            },
            {
                'title': 'town title 2',
                'description': 'health description 2',
            },
            {
                'title': 'town title 3',
                'description': 'town description 3',
            },
        ]
    },
]

def show_channels(request):
    context = {
        'channels': feed_list
    } 
    return render(request, 'rssfeeds/channels.html', context)

def show_singlechannel(request):

    context = {}
    return render(request, 'rssfeeds/single_channel.html', context)

def welcomePageView(request):

    return render(request, 'welcome.html')
