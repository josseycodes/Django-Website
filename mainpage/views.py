from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import HomeSection, AboutSection, SkillCategory, PortfolioItem

def home(request):
    home_section = HomeSection.objects.first()
    about_section = AboutSection.objects.first()
    skill_categories = SkillCategory.objects.all()
    portfolio_items = PortfolioItem.objects.all()
    
    context = {
        'home_section': home_section,
        'about_section': about_section,
        'skill_categories': skill_categories,
        'portfolio_items': portfolio_items,
    }
    
    return render(request, 'yourapp/home.html', context)
