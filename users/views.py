from django.shortcuts import render

def index(request):
    # Django context dict, 
    context = {
        "page_name": "Início",
    }

    return render(request, "index.html", context)