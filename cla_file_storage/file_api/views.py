from rest_framework import viewsets
from rest_framework.response import Response
from .models import File, Keyword
from .serializer import FileSerializer, KeywordSerializer
from django.conf import settings
import shutil
import os


# Create your views here.
class FileViewSet(viewsets.ModelViewSet):
    serializer_class = FileSerializer

    def get_queryset(self):
        files = File.objects.all()
        return files

    def add_keywords(self, keyword_data):
        # add keywords in request that aren't already in the db keywords
        for each_keyword in keyword_data:
            inDB = Keyword.objects.filter(associated_keyword=each_keyword).exists()
            # TO DO: identify similar keywords and re-assign to existing one (ie. singular/plural or noun/verb for the same thing)
            if inDB == False:
                new_keyword = Keyword.objects.create(associated_keyword=each_keyword)
                new_keyword.save()

    def create(self, request, *args, **kwargs):
        data = request.data

        initial_path = data["document"]
        new_path = settings.MEDIA_ROOT + data["name"] + "." + data["document_format"]
        # shutil.copyfile(initial_path, new_path)

        new_file = File.objects.create(
            name=data["name"],
            document=data["document"],
            display_name=data["display_name"],
            path=new_path,
            document_format=data["document_format"],
            document_text=data["document_text"],
            category=data["category"],
            description=data["description"],
            orig_doc_date=data["orig_doc_date"],
        )
        new_file.save()

        # this is how to access the data that's built into the FileField
        print("FILE DATA:")
        print("document.name =", new_file.document.name)
        print("document.size =", new_file.document.size)
        print("document.file =", new_file.document.file, "\n")
        # name & file are the same - set file.name to os.path.basename?

        self.add_keywords(data["keyword"])

        # associate the keywords to the new file by keyword text
        for each_keyword in data["keyword"]:
            keyword_obj = Keyword.objects.get(associated_keyword=each_keyword)
            # if duplicate keywords are in the db, this line will error:
            # file_api.models.Keyword.MultipleObjectsReturned: get() returned more than one Keyword -- it returned 4!

            new_file.keyword.add(keyword_obj)

            # for POST request data format like this:
            # {
            #     "name": "filename",
            #     ...etc...
            #     "keyword": ["harvesting", "survey"]
            # }

        serializer = FileSerializer(new_file)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        file_obj = self.get_object()
        data = request.data

        self.add_keywords(data["keyword"])

        keyword_ids = []
        for keyword in data["keyword"]:
            inDB = Keyword.objects.filter(associated_keyword=keyword).exists()
            if inDB == False:
                new_keyword = Keyword.objects.create(associated_keyword=keyword)
                new_keyword.save()

            current = Keyword.objects.get(associated_keyword=keyword)
            keyword_ids.append(current.id)

        file_obj.name = data["name"]
        file_obj.document = data["document"]
        file_obj.display_name = data["display_name"]

        if file_obj.path != data["path"]:
            os.rename(file_obj.path, data["path"])
            file_obj.path = data["path"]

        file_obj.document_format = data["document_format"]
        file_obj.file_text = data["file_text"]
        file_obj.category = data["category"]
        file_obj.description = data["description"]
        file_obj.orig_doc_date = data["orig_doc_date"]
        file_obj.keyword.set(keyword_ids)

        file_obj.save()

        serializer = FileSerializer(file_obj)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        file_obj = self.get_object()
        file_name = file_obj.name
        feedback = {
            "message": f"You do not have permission to delete the file '{file_name}'."
        }

        if request.user.is_staff:
            selected_file = self.get_object()
            selected_file.delete()
            # insert code to actually delete file from storage?
            # or code to move to a designated "trash" folder on the server to look through before really deleting?
            feedback = {"message": f"The file '{file_name}' has been deleted"}

        return Response(feedback)

    def partial_update(self, request, *args, **kwargs):
        file_obj = self.get_object()
        data = request.data

        keyword_ids = []
        try:
            self.add_keywords(data["keyword"])

            for keyword in data["keyword"]:
                inDB = Keyword.objects.filter(associated_keyword=keyword).exists()
                if inDB == False:
                    new_keyword = Keyword.objects.create(associated_keyword=keyword)
                    new_keyword.save()

                current = Keyword.objects.get(associated_keyword=keyword)
                keyword_ids.append(current.id)
        except KeyError:
            pass

        file_obj.name = data.get("name", file_obj.name)
        file_obj.document = data.get("document", file_obj.document)
        file_obj.display_name = data.get("display_name", file_obj.display_name)

        if file_obj.path != data["path"]:
            os.rename(file_obj.path, data["path"])
            file_obj.path = data.get("path", file_obj.path)

        file_obj.document_format = data.get("document_format", file_obj.document_format)
        file_obj.file_text = data.get("file_text", file_obj.file_text)
        file_obj.category = data.get("category", file_obj.category)
        file_obj.description = data.get("description", file_obj.description)
        file_obj.orig_doc_date = data.get("orig_doc_date", file_obj.orig_doc_date)
        if keyword_ids:
            file_obj.keyword.set(keyword_ids)
        # TO DO: option to delete individual keywords

        file_obj.save()
        serializer = FileSerializer(file_obj)
        return Response(serializer.data)


class KeywordViewSet(viewsets.ModelViewSet):
    serializer_class = KeywordSerializer

    def get_queryset(self):
        keywords = Keyword.objects.all()
        return keywords
