from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import ProfileSerializer
from .models import UserProfile

# Create your views here.
def index(request):
    return render(request, 'index.html')

class ProfileViewSet(viewsets.ModelViewSet):

    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer