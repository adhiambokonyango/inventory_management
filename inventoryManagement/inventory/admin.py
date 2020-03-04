from django.contrib import admin

# Register your models here.
from .models import *
from import_export.admin import ImportExportActionModelAdmin


@admin.register(Desktop, Laptop, Mobile)
class ViewAdmin(ImportExportActionModelAdmin):
    pass
