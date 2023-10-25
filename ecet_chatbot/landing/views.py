from django.http import HttpResponse
from django.shortcuts import render
HttpResponse
# Create your views here.
def simpleLanding(req):
    # Delete this view as this is no longer in use...
    return HttpResponse("<h1>Hello !!! Landing Page !!</h1>")

def startPage(req):
    data = {'q':'qqq'}
    context = {'q0':'Hello User! How may I assist you today !', 'data':data}
    if req.method == 'POST':
        # print(req.POST['search_query'])
        if req.POST['search_query']:
            data = {'q':req.POST['search_query']}
        return render(req, 'landing/landing.html', context)
    else:
        return render(req, 'landing/landing.html', context)
