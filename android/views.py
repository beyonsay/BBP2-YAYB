# View functions for handling Android app API endpoints:

# `android_login`: Handles Android user login requests. Verifies user credentials and returns a token on success.
# - Accepts a POST request with 'username' and 'password' in the request data.
# - Validates the user's credentials and issues a token if valid.
# - Returns a JSON response with the token and user data.

# `test_token`: A test endpoint that requires authentication. Returns a simple message if the token is valid.
# - Requires authentication via SessionAuthentication or TokenAuthentication.
# - Returns a "passed!" message as a response if authentication is successful.

# `get_all_content`: Retrieves all public content from the 'main' app.
# - Requires authentication via SessionAuthentication or TokenAuthentication.
# - Retrieves all content objects with 'visible' set to "public" and serializes them.
# - Returns a JSON response with the serialized content data.

# `android_logout`: Handles Android user logout requests. Deletes the user's token.
# - Accepts a POST request to log the user out.
# - Deletes the user's token (authentication token) to log them out.
# - Returns a "Logged out successfully" message as a response.

# `get_assigned_content`: Retrieves content assigned to the authenticated user.
# - Requires authentication via SessionAuthentication or TokenAuthentication.
# - Retrieves all content objects assigned to the authenticated user and serializes them.
# - Returns a JSON response with the serialized content data.

from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer, ContentSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from main.models import Content

@api_view(['POST'])
def android_login(request):
    user = get_object_or_404(User, username=request.data['username'])

    if not user.check_password(request.data['password']):
        return Response("missing user", status=status.HTTP_404_NOT_FOUND)
    
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(user)

    return Response({'token': token.key, 'user': serializer.data})

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("passed!")

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_all_content(request):
    allcontent = Content.objects.filter(visible="public")
    serializer = ContentSerializer(allcontent, many=True, context={'request': request})  # Serialize a queryset of objects
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def android_logout(request):
    request.auth.delete()
    
    return Response("Logged out successfully")

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_assigned_content(request):
    user = request.user.id
    allcontent = Content.objects.filter(assignedUsers=user)
    serializer = ContentSerializer(allcontent, many=True, context={'request': request})  # Serialize a queryset of objects
    return Response(serializer.data)