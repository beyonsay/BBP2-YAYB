"""
URL configuration for bbp2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Main URL Configuration:

# - Configures the Django admin site header, title, and index title.
# - Includes URL patterns from various Django apps using 'include' and 'path'.

# URL Patterns:
# - '' (empty path) includes URL patterns from the 'main' app.
# - 'assigned/' includes URL patterns from the 'users' app, likely related to assigned content.
# - '' (empty path) also includes URL patterns from the 'android' app.
# - 'login' maps to Django's built-in LoginView with a custom template for user login.
# - 'logout' maps to Django's built-in LogoutView with a custom template for user logout.
# - 'admin/' maps to the Django admin site.

# Note: The 'include' function is used to include URL patterns from other Django apps, and 'path' maps URL patterns to views or includes.

# The admin site's header, title, and index title are customized to display 'You and Your Baby' in the admin panel.

from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views

admin.site.site_header = 'You and Your Baby Admin Site'
admin.site.title = 'You and Your Baby Admin Site'
admin.site.index_title = 'You and Your Baby Admin'

urlpatterns = [
    path('', include('main.urls')),
    path('assigned/', include('users.urls')),
    path('', include('android.urls')),
    path('login', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('admin/', admin.site.urls),
]
