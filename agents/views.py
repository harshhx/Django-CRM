from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from django.views import generic

from leads.forms import AgentCreateForm
from leads.models import Agent


class AgentListView(LoginRequiredMixin, generic.ListView):
    template_name = 'agents/agent_list.html'
    context_object_name = 'agents'

    def get_queryset(self):
        return Agent.objects.all()


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
    queryset = Agent.objects.all()
    context_object_name = 'agent'


class AgentUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'agents/agent_update.html'
    form_class = AgentCreateForm
    queryset = Agent.objects.all()

    def get_success_url(self):
        return reverse('agents:agent-detail', args=([self.object.id]))


class AgentDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'agents/agent_delete.html'
    queryset = Agent.objects.all()

    def get_success_url(self):
        return reverse('agents:agent-list')
