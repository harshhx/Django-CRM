from django.contrib import admin
from django.urls import path, include
from leads.views import LandingView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', landing, name='landing'),
    path('', LandingView.as_view(), name='landing'),
    path('leads/', include('leads.urls', namespace='leads'))
]
