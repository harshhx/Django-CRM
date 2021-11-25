from django.shortcuts import render
from .models import Lead


def lead_list(request):

    leads = Lead.objects.all()

    return render(request, 'leads/lead_list.html', {'leads': leads})
