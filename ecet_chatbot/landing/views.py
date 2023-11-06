from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
# Create your views here.
def simpleLanding(req):
    # Delete this view as this is no longer in use...
    return HttpResponse("<h1>Hello !!! Landing Page !!</h1>")

def startPage(req):
    data = {'q':'qqq'}
    context = {'q0':'Hello User! How may I assist you today !', 'data':data}
    if req.method == 'POST':
        query = req.POST.get('search_query', '')
        print('Query value:: ',query)
        if req.POST['search_query']:
            data = {'q':req.POST['search_query']}
        # return render(req, 'landing/landing.html', context)
        return JsonResponse({query:'helloo'})
    else:
        return render(req, 'landing/landing.html', context)
