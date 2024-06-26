from django.shortcuts import render
from movie.models import Movie
from django.http import HttpResponse

# Create your views here.
def getallMovies(request):
    #getting all data from Movie model
    #select * from Movie;
    all_movies=Movie.objects.all()
    print(all_movies)
    for movie in (all_movies):
        print(movie.id,movie.name,movie.release_date)
    #return HttpResponse("Hello i am learning django")
    data={}
    data['movies']=all_movies
    return render(request,'movie/index.html',context=data)
