from django import forms
from testapp.models import MovieModel
class Movie_Form(forms.ModelForm):
    Release_Date=forms.DateField()
    Movie_name=forms.CharField(max_length=30)
    Hero_name=forms.CharField(max_length=30)
    Heroine_name=forms.CharField(max_length=30)
    rating=forms.IntegerField()

    class Meta:
        model=MovieModel
        fields='__all__'
