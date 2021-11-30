from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from agents.mixins import OrganizerAndLoginRequiredMixin
from .forms import LeadModelForm, SignUpForm
from .models import Lead


class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = SignUpForm

    def get_success_url(self):
        return reverse('login')


class LandingView(TemplateView):
    template_name = 'landing.html'


class LeadListView(LoginRequiredMixin, ListView):
    template_name = 'leads/lead_list.html'
    context_object_name = 'leads'

    def get_queryset(self):
        user = self.request.user
        if user.is_organizer:
            queryset = Lead.objects.filter(organisation=user.userprofile)
        else:
            queryset = Lead.objects.filter(organisation=user.agent.organisation)
            queryset = queryset.filter(agent__user=user)

        return queryset


class LeadDetailView(LoginRequiredMixin, DetailView):
    template_name = 'leads/lead_detail.html'

    context_object_name = 'lead'

    def get_queryset(self):
        user = self.request.user
        if user.is_organizer:
            queryset = Lead.objects.filter(organisation=user.userprofile)
        else:
            queryset = Lead.objects.filter(organisation=user.agent.organisation)
            queryset = queryset.filter(agent__user=user)

        return queryset


class LeadCreateView(OrganizerAndLoginRequiredMixin, CreateView):
    template_name = 'leads/lead_create.html'
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads:lead-list')

    def form_valid(self, form):
        send_mail(
            subject="A new Lead has been created",
            message="To view the lead please visit the website",
            from_email="test@test.com",
            recipient_list=['test@test2.com']
        )
        return super(LeadCreateView, self).form_valid(form)


class LeadUpdateView(OrganizerAndLoginRequiredMixin, UpdateView):
    template_name = 'leads/lead_update.html'
    form_class = LeadModelForm

    def get_queryset(self):
        user = self.request.user
        queryset = Lead.objects.filter(organisation=user.userprofile)
        return queryset

    def get_success_url(self):
        return reverse('leads:lead-detail', args=([self.object.id]))


class LeadDeleteView(OrganizerAndLoginRequiredMixin, DeleteView):
    template_name = 'leads/lead_delete.html'

    def get_queryset(self):
        user = self.request.user
        queryset = Lead.objects.filter(organisation=user.userprofile)
        return queryset

    def get_success_url(self):
        return reverse('leads:lead-list')

#
# def lead_delete(request, pk):
#     lead = Lead.objects.get(id=pk)
#     lead.delete()
#     return redirect('/leads/')
#
# def landing(request):
#     return render(request, 'landing.html')
#
# def lead_list(request):
#     leads = Lead.objects.all()
#
#     return render(request, 'leads/lead_list.html', {'leads': leads})
#
# def lead_detail(request, pk):
#     lead = Lead.objects.get(id=pk)
#     return render(request, 'leads/lead_detail.html', {'lead': lead})
#
# def lead_create(request):
#     # form = LeadForm()
#     form = LeadModelForm
#     if request.method == "POST":
#         form = LeadModelForm(request.POST)
#         if form.is_valid():
#             # data = form.cleaned_data
#             # agent = Agent.objects.first()
#             # lead = Lead(
#             #     first_name=data.get('first_name'),
#             #     last_name=data.get('last_name'),
#             #     age=data.get('age'),
#             #     agent=agent
#             # )
#             # lead.save()
#             form.save()
#             return redirect('/leads/')
#     return render(request, 'leads/lead_create.html', {'form': form})
#
# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadModelForm(instance=lead)
#     if request.method == "POST":
#         form = LeadModelForm(request.POST, instance=lead)
#         if form.is_valid():
#             form.save()
#             return redirect(f'/leads/{pk}/')
#     return render(request, 'leads/lead_update.html', {'form': form, 'lead': lead})
