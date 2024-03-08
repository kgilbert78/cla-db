from django.db import models
import uuid  # https://docs.python.org/3/library/uuid.html


# Create your models here.
class Keyword(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    associated_keyword = models.CharField(
        max_length=200
    )  # may change length - coordinate it with keyword output params

    def __str__(self) -> str:
        return self.associated_keyword


class File(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    name = models.CharField(max_length=150)  # change if using id as name
    document = models.FileField(upload_to="")
    display_name = models.CharField(max_length=150)
    document_format = models.CharField(max_length=12)
    document_text = models.TextField()
    category = models.CharField(max_length=50)
    description = models.TextField()
    orig_doc_date = models.DateField()
    orig_doc_date_range_end = models.DateField()
    # option for range of dates:
    # https://docs.djangoproject.com/en/4.2/ref/contrib/postgres/fields/#daterangefield
    # varchar date_accuracy - "month day year", "month year", "year", and "decade" - perhaps better indicated with single letters: MDY, MY, Y, and D. or combine this with insight from studying date libraries
    # varchar auth_level - Who is allowed to view it. (May not include this to start.)
    keyword = models.ManyToManyField(Keyword)  # creates bridge table for me
    # https://docs.djangoproject.com/en/4.2/ref/models/fields/#manytomanyfield

    # timestamp upload_time
    # upload_timestamp = models.DateField(auto_now_add=True)

    # Approval stuff - may not include to start
    # varchar suggested_name
    # varchar suggested_date
    # text suggested_description
    # text suggested_keywords_list
    # boolean approved
    # timestamp approval_time
    # int uploader_user_id FK
    # int approved_by_user_id FK

    def __str__(self) -> str:
        return self.display_name
