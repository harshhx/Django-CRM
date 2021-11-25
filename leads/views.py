from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Lead, Agent
from .forms import LeadForm


def lead_list(request):
    leads = Lead.objects.all()

    return render(request, 'leads/lead_list.html', {'leads': leads})


def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    return render(request, 'leads/lead_detail.html', {'lead': lead})


def lead_create(request):
    form = LeadForm()
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            agent = Agent.objects.first()
            lead = Lead(
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                age=data.get('age'),
                agent=agent
            )
            lead.save()
            return redirect('/leads/')
    return render(request, 'leads/lead_create.html', {'form': form})
