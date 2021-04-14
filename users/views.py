from django.shortcuts import render
from visitors.models import Visitor

def index(request):
    all_visitors = Visitor.objects.all()

    # Django context dict, 
    context = {
        "page_name": "Início",
        "visitors": all_visitors,
    }

    return render(request, "index.html", context)