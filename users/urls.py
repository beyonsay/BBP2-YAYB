# URL pattern for the 'users' app:

# - The empty path ('') maps to the 'assigned' view, the main view for the 'users' app.
# - The 'name' parameter assigns the name 'assigned' to this URL pattern for easy reference in templates and views.

from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.assigned, name='assigned'),
]