from django.shortcuts import render
from .models import RssFeed, FeedItem
from .forms import RssFeedForm

# Create your views here.
def show_channels(request):

    context = {
        'channels': RssFeed.objects.all()
    } 

    return render(request, 'rssfeeds/channels.html', context)

def enroll_channel(request):

    form = RssFeedForm()
    context = {'form': form}

    return render(request, 'rssfeeds/feed_enroll_form.html', context)

def show_singlechannel(request, channel_id):

    channel_detail = RssFeed.objects.get(id=channel_id)
    feed_items = FeedItem.objects.filter(feed_belongs_to=channel_id)

    context = {
        'channel_detail': channel_detail,
        'feed_items': feed_items
    }

    if not channel_detail:
        return render(
            request, 
            'rssfeeds/error.html', 
            {
                'err_msg': "Channel id is not valid" + link_id
            }
        )

    return render(request, 'rssfeeds/single_channel.html', context)

def welcomePageView(request):

    return render(request, 'welcome.html')
