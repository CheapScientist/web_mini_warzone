from django.http import HttpResponse

def index(request):
    line1 = '<h1 style = "text-align: center">hello world</h1>'
    line2 = '<img src = "https://cdn.cloudflare.steamstatic.com/steam/apps/570/header.jpg?t=1650611880" width = 1500>'
    return HttpResponse(line1+line2)
