from django.shortcuts import render

# Create your views here.
def show_people(request):
    context = {}
    return render(request, 'subscribers/people_list.html', context)

def show_interest(request):
    context = {}
    return render(request, 'subscribers/interest_list.html', context)