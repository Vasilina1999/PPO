from django.shortcuts import render, redirect


def index(request):
      return render(request, 'new/new_home.html')





def about(request):
   return render(request, 'main/about.html')