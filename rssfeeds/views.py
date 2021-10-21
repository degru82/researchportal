from django.shortcuts import render

# Create your views here.

feed_list = [
    {
        'name': 'transport feed', 
        'link': 'trns_fd',
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
        'link': 'hlth_fd',
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
        'link': 'town_fd',
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

def show_singlechannel(request, link_id):

    feed_obj = None
    for fd in feed_list:
        if link_id == fd['link']:
            feed_obj = fd
            break
    else:
        print('------')
        print(link_id)
        return render(request, 'rssfeeds/error.html', {'err_msg': "Channel id is not valid" + link_id})

    context = feed_obj
    return render(request, 'rssfeeds/single_channel.html', context)

def welcomePageView(request):

    return render(request, 'welcome.html')
