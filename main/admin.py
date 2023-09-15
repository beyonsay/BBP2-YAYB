# Registering models with the Django admin interface:

# `admin.site.register(Content, MyModelAdmin)`: Registers the 'Content' model with the admin interface.
# - Allows administrators to manage 'Content' objects through the admin panel.
# - 'MyModelAdmin' is an optional custom admin class that can be used to customize the admin interface for 'Content'.

from django.contrib import admin

from .models import Content, MyModelAdmin


admin.site.register(Content, MyModelAdmin)