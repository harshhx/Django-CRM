from django.urls import path
from django.contrib.auth.views import LoginView
from .views import (
    LeadListView,
    LeadDetailView,
    LeadCreateView,
    LeadUpdateView,
    LeadDeleteView,
    AssignLeadView
)

app_name = 'leads'

urlpatterns = [
    # path('', lead_list, name='lead-list'),
    path('', LeadListView.as_view(), name='lead-list'),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    path('create/', LeadCreateView.as_view(), name='lead-create'),
    path('<int:pk>/update', LeadUpdateView.as_view(), name='lead-update'),
    path('<int:pk>/delete', LeadDeleteView.as_view(), name='lead-delete'),
    path('<int:pk>/assign', AssignLeadView.as_view(), name='lead-assign'),
]
