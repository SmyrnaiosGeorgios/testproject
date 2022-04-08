from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name','city','address','description']

@admin.register(Cardgame)
class CardgameAdmin(admin.ModelAdmin):
    list_display = ['title','publisher','description','releasedate','logo']

@admin.register(Referee)
class RefereeAdmin(admin.ModelAdmin):
    list_display = ['name','lastname','gender','description']

@admin.register(CategoryStore)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']