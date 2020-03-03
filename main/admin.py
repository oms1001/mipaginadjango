from django.contrib import admin
from .models import Entrada
from tinymce.widgets import TinyMCE
from django.db import models



class EntradaAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Title/date", {'fields': ["entrada_title", "entrada_published"]}),
        ("Content", {"fields": ["entrada_content"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }


admin.site.register(Entrada,EntradaAdmin)

