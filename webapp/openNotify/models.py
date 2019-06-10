from __future__ import unicode_literals
from django.db import models
from django_mysql.models import JSONField, Model

# Create your models here.


class APIResponse(models.Model):

    # url = models.CharField(max_length=200)
    data = JSONField()

    class Meta:
        db_table = "passtimejson"

    def __str__(self):
        return self.name

#
# class BookExample(models.Model):
#     id = models.BigAutoField(primary_key=True, editable=False)
#     name = models.CharField(max_length=100)
#     detail_text = models.TextField()
#     detail_json = JSONField()  # requires Django-Mysql package
#
#     class Meta:
#         managed = True
#         db_table = 'book_example'
#         verbose_name = 'Book Example'
#         verbose_name_plural = 'Book Examples'