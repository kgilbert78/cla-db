from django.db import models


# Create your models here.
class File(models.Model):
    name = models.CharField(max_length=150)  # change if using id as name
    display_name = models.CharField(max_length=150)
    primary_filepath = models.CharField(max_length=300)
    # ^ change to "url"?
    primary_format = models.CharField(max_length=12)
    file_text = models.TextField()
    category = models.CharField(max_length=50)
    description = models.TextField
    orig_doc_date = models.DateField()
    # option for range of dates:
    # https://docs.djangoproject.com/en/4.2/ref/contrib/postgres/fields/#daterangefield
    # varchar date_accuracy - "month day year", "month year", "year", and "decade" - perhaps better indicated with single letters: MDY, MY, Y, and D. or combine this with insight from studying date libraries
    # varchar auth_level - Who is allowed to view it. (May not include this to start.)


    # Approval stuff - may not include to start
    # timestamp upload_time
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

class Keyword(models.Model):
    associated_keyword = models.CharField(max_length=200) # may change length - coordinate it with keyword output params
    file = models.ManyToManyField(File) # creates bridge table for me
    # https://docs.djangoproject.com/en/4.2/ref/models/fields/#manytomanyfield

    def __str__(self) -> str:
        return self.associated_keyword
