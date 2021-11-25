from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm


def lead_list(request):
    leads = Lead.objects.all()

    return render(request, 'leads/lead_list.html', {'leads': leads})


def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    return render(request, 'leads/lead_detail.html', {'lead': lead})


def lead_create(request):
    # form = LeadForm()
    form = LeadModelForm
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            # data = form.cleaned_data
            # agent = Agent.objects.first()
            # lead = Lead(
            #     first_name=data.get('first_name'),
            #     last_name=data.get('last_name'),
            #     age=data.get('age'),
            #     agent=agent
            # )
            # lead.save()
            form.save()
            return redirect('/leads/')
    return render(request, 'leads/lead_create.html', {'form': form})


def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect(f'/leads/{pk}/')
    return render(request, 'leads/lead_update.html', {'form': form, 'lead': lead})
