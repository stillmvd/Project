from django.contrib import admin

from .models import Traks, Comments


@admin.register(Traks)
class TraksAdmin(admin.ModelAdmin):
    """
    
    
    
    """
    list_display = (
        'name', 
        'performer', 
        'album', 
        'date_relised', 
        'trak')

    list_filter = (
        'performer', 
        'album', 
        'date_relised')

    search_fields = (
        'name', 
        'performer', 
        'album', 
        'date_relised')

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    """
    
    
    
    """    
    list_display = (
        'text_comment', 
        'user_name', 
        'name_track')

    list_filter = (
        'user_name', 
        'name_track')

    search_fields = (
        'user_name', 
        'name_track')

