from django.contrib import messages
from django.shortcuts import render, redirect
from visitors.forms import VisitorForm

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

    return render(request, "visitors/register_visitor.html", context)