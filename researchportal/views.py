from django.http import HttpResponse
from django.shortcuts import render


def welcomePageView(request):

    return render(request, 'welcome.html')