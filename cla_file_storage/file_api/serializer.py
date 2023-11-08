from rest_framework import serializers
from .models import File, Keyword

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'name', 'display_name', 'primary_filepath', 'primary_format', 'file_text', 'category', 'description', 'orig_doc_date']
        depth = 1  # nests Keyword data in json response, instead of just id

class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = ['id', 'associated_keyword', 'file']