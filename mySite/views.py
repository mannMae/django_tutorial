from django.http import HttpResponse
from django.shortcuts import render

def base_response(request):
    return HttpResponse("HIHIHI")

def render_index(request):
    return render(request, "index.html")