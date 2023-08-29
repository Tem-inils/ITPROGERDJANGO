from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'mainapp/home_page.html')
def about(request):
    return render(request, 'mainapp/about.html')
def catalog(request):
    return render(request, 'mainapp/catalog.html')