from rest_framework import serializers
from .models import File, Keyword


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = [
            "id",
            "document",
            "name",
            "display_name",
            # "path",
            "document_format",
            "document_text",
            "category",
            "description",
            "orig_doc_date",
            "keyword",
        ]
        depth = 1  # nests Keyword data in json response, instead of just id


class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = ["id", "associated_keyword"]
