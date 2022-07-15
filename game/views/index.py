from django.shortcurts import render

def index(request):
    return render(request, "multends/web.html")

