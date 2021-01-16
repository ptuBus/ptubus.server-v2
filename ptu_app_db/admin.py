from django.contrib import admin
from ptu_app_db.models import AppDB


@admin.register(AppDB)
class AppDBAdmin(admin.ModelAdmin):
    fields = ("file_key",)
    list_display = ("file_key",)
