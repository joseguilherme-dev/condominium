from django.shortcuts import render
from visitors.models import Visitor

def index(request):
    # Last 5 visitors
    last_visitors = Visitor.objects.all().order_by('-id')[:5]

    # Django context dict, 
    context = {
        "page_name": "Início",
        "visitors": last_visitors,
    }

    return render(request, "index.html", context)