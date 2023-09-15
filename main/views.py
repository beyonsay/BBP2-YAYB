# 'main(request)': Displays the main page of the application and retrieves public content items for display.

# 'content(request, contentID)': Displays a specific content item based on the provided 'contentID' in the URL.

# 'search_suggestions(request)': Provides search suggestions based on a query parameter and returns them as a JSON response.

# 'get_content_by_category(request)': Placeholder for serving content by category, returns an empty JSON response. This is needed for the filtering of ECD content at the bottom of the page

# 'category(request, category)': Displays content items that match a specified 'category'.

# 'teesandcees(request)': Renders the terms and conditions page.

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import loader
from .models import Content

def main(request):
  allcontent = Content.objects.filter(visible="public")
  print(allcontent)

  return render(request, 'main/main.html', {'allcontent': allcontent})

def content(request, contentID):
  file = Content.objects.get(idContent=contentID)

  print(contentID)
  print(file.file)
  return render(request, 'main/content.html', {'content': file})

def search_suggestions(request):
    query = request.GET.get('q')
    suggestions = []

    if query:
        suggestions = Content.objects.filter(title__icontains=query).values_list('title', flat=True)[:5]  # Limit to 5 suggestions

    return JsonResponse({'suggestions': suggestions})

def get_content_by_category(request):

  return JsonResponse( safe=False)

def category(request, category):
  allcontent = Content.objects.filter(visible="public").filter(topics=category)

  return render(request, 'main/category.html', {'allcontent': allcontent})

def teesandcees(request):
  template = loader.get_template('main/teesandcees.html')
  return HttpResponse(template.render())
