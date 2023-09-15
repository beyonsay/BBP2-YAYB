# Defining the 'Content' model:

# The 'Content' model represents content items and has fields like 'title', 'file', 'visible', 'tag', 'topics', 'language', and 'assignedUsers'.
# - It uses various choice fields for 'tag', 'topics', 'language', and 'visible'.
# - 'assignedUsers' is a ManyToMany field representing users assigned to this content.

# 'MyModelAdmin' is a custom admin class for the 'Content' model:
# - Customizes the display of 'Content' objects in the Django admin interface.
# - Defines 'list_display', 'search_fields', 'list_per_page', and 'formfield_overrides' for the admin interface.
# - Adds a custom method 'display_assigned_users' to display assigned users in the admin panel.

# The 'Meta' class inside the 'Content' model specifies the database table name.

# The '__str__' method defines how 'Content' instances are displayed as strings (e.g., in the admin interface).

# 'admin.site.register(Content, MyModelAdmin)' registers the 'Content' model with the Django admin interface and associates it with the 'MyModelAdmin' custom admin class.

from django.db import models
import uuid
from django.contrib.auth.models import User
from django.contrib import admin
from django.forms import CheckboxSelectMultiple

class Content(models.Model):
    TAGS = (
        ('video', 'Video'),
        ('image', 'Image'),
        ('pdf', 'Pdf'),
    )

    TOPICS = (
        ('Baby Development', 'Baby Development'),
        ('Baby Health', 'Baby Health'),
        ('Parent Health', 'Parent Health'),
    )

    LANG = (
        ('English', 'English'),
        ('IsiXhosa', 'IsiXhosa'),
        ('ChiShona', 'ChiShona'),
        ('Afrikaans', 'Afrikaans'),
    )

    VISIBILITY = (
        ('public', 'Public'),
        ('private', 'Private'),
    )

    idContent = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=500)
    file = models.FileField()
    visible = models.CharField(max_length=10, choices=VISIBILITY)
    tag = models.CharField(max_length=10, choices=TAGS)
    topics = models.CharField(max_length=30, choices=TOPICS)
    language = models.CharField(max_length=15, choices=LANG)
    assignedUsers = models.ManyToManyField(User, blank=True)

    class Meta:
        db_table = 'Content'

    def __str__(self):
        return self.title

class MyModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'visible', 'tag', 'topics', 'language', 'display_assigned_users']
    search_fields = ('title',)

    list_per_page = 20

    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

    def display_assigned_users(self, obj):
        return ", ".join([user.username for user in obj.assignedUsers.all()])

    display_assigned_users.short_description = 'Assigned Users'

class ModelAdmin(admin.ModelAdmin):
        list_display = ['title', 'visible', 'tag', 'topics', 'language', 'assignedUsers']


