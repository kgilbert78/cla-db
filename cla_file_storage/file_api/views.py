from rest_framework import viewsets
from rest_framework.response import Response
from .models import File, Keyword
from .serializer import FileSerializer, KeywordSerializer

# Create your views here.
class FileViewSet(viewsets.ModelViewSet):
    serializer_class = FileSerializer

    def get_queryset(self):
        files = File.objects.all()
        return files
    

class KeywordViewSet(viewsets.ModelViewSet):
    serializer_class = KeywordSerializer

    def get_queryset(self):
        keywords = Keyword.objects.all()
        return keywords