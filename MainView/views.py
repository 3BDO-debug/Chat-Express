from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'home-page.html')

def auth_page(request):
    return render(request, 'login-register.html')

def profile_page(request):
    return render(request, 'profile.html')

def fb_page_details(request):
    return render(request, 'page-details.html')