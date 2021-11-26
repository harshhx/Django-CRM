from django.contrib import admin
from django.urls import path, include
from leads.views import landing
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing, name='landing'),
    path('leads/', include('leads.urls', namespace='leads'))
]
