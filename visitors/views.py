from django.contrib import messages
from django.shortcuts import (
    render, redirect, get_object_or_404
)
from visitors.forms import VisitorForm
from visitors.models import Visitor

def register_visitor(request):
    form = VisitorForm()

    if request.method == "POST":
        form = VisitorForm(request.POST)

        if form.is_valid():
            visitor = form.save(commit=False)

            visitor.related_concierge = request.user.concierge
            visitor.save()

            messages.success(
                request,
                "O visitante foi registrado com sucesso."
            )

    context = {
        "form": form,
        "page_name": "Registrar Visitantes",
    }

    return render(request, "visitors/register-visitor.html", context)

def visitor_informations(request, id):
    visitor = get_object_or_404(
        Visitor,
        id=id
    )

    context = {
        "page_name": "Visitante",
        "visitor": visitor,
    }

    return render(request, "visitors/visitor.html", context)