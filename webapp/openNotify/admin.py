from django.contrib import admin
from .models import APIResponse, NewAPIResponse,Ai_analysis_log


# Register your models here.

admin.site.register(APIResponse)
admin.site.register(NewAPIResponse)
admin.site.register(Ai_analysis_log)