# 'assigned(request)': Displays content assigned to the authenticated user.

# - The '@login_required' decorator ensures that only authenticated users can access this view.
# - Retrieves the authenticated user's ID using 'request.user.id'.
# - Retrieves content items from the 'Content' model where the user is assigned.
# - Renders the 'users/assigned.html' template and passes the retrieved content as 'allcontent'.

# Note: This view is intended to show content assigned to a specific user after they have logged in.

from django.shortcuts import render
from django.contrib import messages
from main.models import Content

from django.contrib.auth.decorators import login_required

@login_required
def assigned(request):
    user = request.user.id
    allcontent = Content.objects.filter(assignedUsers=user)

    return render(request, 'users/assigned.html',  {'allcontent': allcontent})