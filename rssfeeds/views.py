from django.shortcuts import render

# Create your views here.
def show_channels(request):
    context = {}
    return render(request, 'rssfeeds/channels.html', context)
