from django.contrib import admin
from .models import Recipe
from import_export.admin import ImportExportModelAdmin

class RecipeAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Recipe, RecipeAdmin)
