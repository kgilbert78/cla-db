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

    def create(self, request, *args, **kwargs):
        data = request.data

        new_file = File.objects.create(
            name=data["name"],
            display_name=data["display_name"],
            primary_filepath=data["primary_filepath"],
            primary_format=data["primary_format"],
            file_text=data["file_text"],
            category=data["category"],
            description=data["description"],
            orig_doc_date=data["orig_doc_date"],
        )
        new_file.save()

        # add existing keywords by id
        for keyword_id in data["keyword"]:
            keyword_obj = Keyword.objects.get(id=keyword_id)
            new_file.keyword.add(keyword_obj)

            # for POST request data format like this:
            # {
            #     "name": "filename",
            #     ...etc...
            #     "keyword": [1,2,3]
            # }

        # TO DO
        # add new keywords by keyword name
        # check that they don't exist already and only add them if they don't
        # if they do exist, assign the existing one that matches

        serializer = FileSerializer(new_file)
        return Response(serializer.data)


class KeywordViewSet(viewsets.ModelViewSet):
    serializer_class = KeywordSerializer

    def get_queryset(self):
        keywords = Keyword.objects.all()
        return keywords
