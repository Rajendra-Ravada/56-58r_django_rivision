from django.shortcuts import render
from django.http import HttpResponse , JsonResponse

# Create your views here.

def home(request):
    # return  render(request,'home.html')
    # return HttpResponse("hello world")
    qp1 = request.GET.get("name","ravi")
    data = {"student_name": qp1,"age":25,"gender":"male"}
    return JsonResponse (data , status=200)




movies = [

     {
        "title": "Baahubali: The Beginning",
        "year": 2015,
        "director": "S. S. Rajamouli",
        "language": "Telugu",
        "genre": "Action / Fantasy",
        "rating": 6.0
    },
     {
        "title": "Baahubali: The Conclusion",
        "year": 2017,
        "director": "S. S. Rajamouli",
        "language": "Telugu",
        "genre": "Action / Fantasy",
        "rating": 8.2
    },
     {
        "title": "RRR",
        "year": 2022,
        "director": "S. S. Rajamouli",
        "language": "Telugu",
        "genre": "Action / Drama",
        "rating": 7.0
    },
     {
        "title": "KGF: Chapter 1",
        "year": 2018,
        "director": "Prashanth Neel",
        "language": "Kannada",
        "genre": "Action / Crime",
        "rating": 9.2
    },
     {
        "title": "KGF: Chapter 2",
        "year": 2022,
        "director": "Prashanth Neel",
        "language": "Kannada",
        "genre": "Action / Crime",
        "rating": 7.3
    }
]
def movies_list(request):
    filtered_data = []
    r1 = float(request.GET.get("r1",6))
    r2 = float(request.GET.get("r2",8))
    for movie in movies:
        if movie["rating"] >r1 and movie["rating"]<r2:
            filtered_data.append(movie)
    return JsonResponse({"data":filtered_data})
