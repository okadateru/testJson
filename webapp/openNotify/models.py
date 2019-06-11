from __future__ import unicode_literals
from django.db import models
from django_mysql.models import JSONField, Model

import json

# Create your models here.
def my_default():
    return {'foo': 'bar'}

class APIResponse(models.Model):

    # url = models.CharField(max_length=200)
    jsondata = JSONField(default=my_default)

    class Meta:
        db_table = "passtimejson"
    jsondata = str(jsondata)

    def __str__(self):
        return self.jsondata


class NewAPIResponse(models.Model):
    image_path = models.CharField(max_length=255, default=None, verbose_name="イメージパス")
    success = models.CharField(max_length=255, default=None)
    message = models.CharField(max_length=255, default=None)
    latitude = models.DecimalField(max_digits=4, decimal_places=2, default=None)
    longtitude = models.DecimalField(max_digits=4, decimal_places=1, default=None)
    passes = models.IntegerField(default=None)
    request_timestamp = models.PositiveIntegerField(default=None)
    response_timestamp = models.PositiveIntegerField(default=None)

    class Meta:
        db_table = "Newpasstimejson"

    def __str__(self):
        return self.image_path



class ai_analysis_log(models.Model):
    image_path = models.CharField(max_length=255)
    success = models.CharField(max_length=255, default=None)
    message = models.CharField(max_length=255, default=None)
    Class = models.IntegerField(default=None)
    confidence = models.DecimalField(max_digits=5, decimal_places=4, default=None)
    request_timestamp = models.PositiveIntegerField(default=None)
    response_timestamp = models.PositiveIntegerField(default=None)

    class Meta:
        db_table = "ai_analysis_log"


"""
# int()　の()の数値NI従いZEROFILL と組み合せて使用した場合、デフォルトのスペースに代わってゼロが埋め込まれる
CREATE TABLE `ai_analysis_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `image_path` varchar(255) DEFAULT NULL,
  `success` varchar(255) DEFAULT NULL,
  `message` varchar(255) DEFAULT NULL,
  `class` int(11) DEFAULT NULL,
  `confidence` decimal(5,4) DEFAULT NULL,
  `request_timestamp` int(10) unsigned DEFAULT NULL,
  `response_timestamp` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
) ENGINE=InnoDB DEFAULT CHARSET=utf8;    
"""

