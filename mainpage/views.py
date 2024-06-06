from django.shortcuts import render
from .models import Home, About, Profile, Category, Skills, Portfolio

def index(request):

    # Home
    home = Home.objects.latest('updated')

    # About
    about = About.objects.first()
    profiles = Profile.objects.first()

    # Skills
    categories = Category.objects.all()

    # Portfolio
    portfolios = Portfolio.objects.all()

    eachsection = {
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'portfolios': portfolios
    }


    return render(request, 'index.html', eachsection)