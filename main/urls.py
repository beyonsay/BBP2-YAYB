"""
URL configuration for yayb2 project.

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

# URL patterns for the 'main' app:

# - The empty path ('') maps to the 'main' view, the main page of the application.
# - 'get_content' maps to the 'get_content_by_category' view, possibly for fetching content by category.
# - 'teesandcees/' maps to the 'teesandcees' view, likely for terms and conditions.
# - 'content/<str:contentID>/' maps to the 'content' view, where 'contentID' is a variable in the URL.
# - 'category/<str:category>/' maps to the 'category' view, where 'category' is a variable in the URL.

# The 'if settings.DEBUG:' block adds a URL pattern for serving media files in debug mode:
# - When the Django project is in DEBUG mode (development), it serves media files using the development server.
# - This is done by appending a URL pattern that maps to media files to the 'urlpatterns'.
# - The 'settings.MEDIA_URL' and 'settings.MEDIA_ROOT' settings determine where media files are served from.

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [
    path('', views.main, name='main'),
    path('get_content', views.get_content_by_category, name='get_content_by_category'),
    path('teesandcees/', views.teesandcees, name='teesandcees'),
    path('content/<str:contentID>/', views.content, name='content'),
    path('category/<str:category>/', views.category, name='category'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
