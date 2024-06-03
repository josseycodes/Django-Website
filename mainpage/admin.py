from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import HomeSection, AboutSection, SkillCategory, Skill, PortfolioItem

admin.site.register(HomeSection)
admin.site.register(AboutSection)
admin.site.register(SkillCategory)
admin.site.register(Skill)
admin.site.register(PortfolioItem)
