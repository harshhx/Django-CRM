from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from django.views import generic

from leads.forms import AgentCreateForm
from leads.models import Agent


class AgentListView(LoginRequiredMixin, generic.ListView):
    template_name = 'agents/agent_list.html'
    context_object_name = 'agents'

    def get_queryset(self):
        request_user_profile = self.request.user.userprofile
        return Agent.objects.filter(organisation=request_user_profile)


class AgentCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'agents/agent_create.html'
    form_class = AgentCreateForm

    def get_success_url(self):
        return reverse('agents:agent-list')

    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.organisation = self.request.user.userprofile
        agent.save()
        return super(AgentCreateView, self).form_valid(form)


class AgentDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'agents/agent_detail.html'

    context_object_name = 'agent'

    def get_queryset(self):
        request_user_profile = self.request.user.userprofile
        return Agent.objects.filter(organisation=request_user_profile)


class AgentUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'agents/agent_update.html'
    form_class = AgentCreateForm

    def get_queryset(self):
        request_user_profile = self.request.user.userprofile
        return Agent.objects.filter(organisation=request_user_profile)

    def get_success_url(self):
        return reverse('agents:agent-detail', args=([self.object.id]))


class AgentDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'agents/agent_delete.html'

    def get_queryset(self):
        request_user_profile = self.request.user.userprofile
        return Agent.objects.filter(organisation=request_user_profile)

    def get_success_url(self):
        return reverse('agents:agent-list')
