from django.db import models

# Create your models here.

# Home Section Model
class HomeSection(models.Model):
    welcome_text = models.CharField(max_length=200)
    welcome_image = models.ImageField(upload_to='home_images/')

    def __str__(self):
        return self.welcome_text


# About Section Model
class AboutSection(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    description = models.TextField()
    profile_image = models.ImageField(upload_to='about_images/')
    linkedin = models.URLField(max_length=200, blank=True, null=True)
    github = models.URLField(max_length=200, blank=True, null=True)
    twitter = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title


# Skill Section Model
class SkillCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.category.name})"


# Portfolio Section Model
class PortfolioItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='portfolio_images/')
    url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title

