from django.shortcuts import render
from testapp.form import Movie_Form
from testapp.models import MovieModel
# Create your views here.
def movie_index(request):
    return render(request,'testapp/index.html')

def movie_Add(request):
    form=Movie_Form(request.GET)
    if form.is_valid():
        form.save()
        form = Movie_Form()
    return render(request,'testapp/add.html',{'form':form})

def movie_list(request):
    lmovies=MovieModel.objects.all()
    return render(request,'testapp/list.html',{'lmovies':lmovies})


