from django.core.mail import send_mail
from django.shortcuts import reverse
from django.views import generic

from leads.forms import AgentCreateForm
from leads.models import Agent
from .mixins import OrganizerAndLoginRequiredMixin


class AgentListView(OrganizerAndLoginRequiredMixin, generic.ListView):
    template_name = 'agents/agent_list.html'
    context_object_name = 'agents'

    def get_queryset(self):
        request_user_profile = self.request.user.userprofile
        return Agent.objects.filter(organisation=request_user_profile)


class AgentCreateView(OrganizerAndLoginRequiredMixin, generic.CreateView):
    template_name = 'agents/agent_create.html'
    form_class = AgentCreateForm

    def get_success_url(self):
        return reverse('agents:agent-list')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password("Password@123")
        user.is_organizer = False
        user.is_agent = True
        user.save()
        agent = Agent(
            user=user,
            organisation=self.request.user.userprofile
        )
        agent.save()

        send_mail(
            subject="You are added as an agent",
            message="You are added to our Costumer Relationship Management system. Please login to get access to your "
                    "dashboard",
            from_email="test@test.com",
            recipient_list=[user.email]
        )

        return super(AgentCreateView, self).form_valid(form)


class AgentDetailView(OrganizerAndLoginRequiredMixin, generic.DetailView):
    template_name = 'agents/agent_detail.html'

    context_object_name = 'agent'

    def get_queryset(self):
        request_user_profile = self.request.user.userprofile
        return Agent.objects.filter(organisation=request_user_profile)


class AgentUpdateView(OrganizerAndLoginRequiredMixin, generic.UpdateView):
    template_name = 'agents/agent_update.html'
    form_class = AgentCreateForm

    def get_queryset(self):
        request_user_profile = self.request.user.userprofile
        return Agent.objects.filter(organisation=request_user_profile)

    def get_success_url(self):
        return reverse('agents:agent-detail', args=([self.object.id]))


class AgentDeleteView(OrganizerAndLoginRequiredMixin, generic.DeleteView):
    template_name = 'agents/agent_delete.html'

    def get_queryset(self):
        request_user_profile = self.request.user.userprofile
        return Agent.objects.filter(organisation=request_user_profile)

    def get_success_url(self):
        return reverse('agents:agent-list')
