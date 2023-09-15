# URL patterns for the 'android' app:
# - 'android_login': Handles Android login requests.
# - 'android_logout': Handles Android logout requests.
# - 'test_token': Handles requests for testing tokens.
# - 'get_all_content': Handles requests to retrieve all content.
# - 'get_assigned_content': Handles requests to retrieve assigned content.
from django.urls import re_path
from . import views

app_name = 'android'

urlpatterns = [
    re_path('android_login', views.android_login),
    re_path('android_logout', views.android_logout),
    re_path('test_token', views.test_token),
    re_path('get_all_content', views.get_all_content),
    re_path('get_assigned_content', views.get_assigned_content),
]