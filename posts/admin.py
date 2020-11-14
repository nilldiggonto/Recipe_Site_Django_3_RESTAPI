from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','timestamp','updated']
    prepopulated_fields = {'slug':('title',)}
    list_display_links = ['title']
    list_filter = ['updated','timestamp']
    search_fields = ['title','content']
    # list_editable = []