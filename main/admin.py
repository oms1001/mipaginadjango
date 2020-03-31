from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from .models import Obra, ObraFecha

class ObraAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Title/date", {'fields': ["obra_title", "obra_published"]}),
        ("URL", {'fields': ["obra_slug"]}),
        ("Series", {'fields': ["obra_fecha"]}),
        ("Content", {"fields": ["obra_content"]}),
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
        }

admin.site.register(ObraFecha)
admin.site.register(Obra,ObraAdmin)
