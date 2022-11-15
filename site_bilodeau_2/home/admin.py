from django.contrib import admin
from .models import Team, PageDeRedirection, TextePageDAccueil

# Register your models here.

admin.site.register(Team)
admin.site.register(PageDeRedirection)
admin.site.register(TextePageDAccueil)