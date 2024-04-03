from django.contrib import admin
from testapp.models import MovieModel
# Register your models here.
class Movie_Admin(admin.ModelAdmin):
    list_display = ['Release_Date','Movie_name','Hero_name','Heroine_name','rating']

admin.site.register(MovieModel,Movie_Admin)
