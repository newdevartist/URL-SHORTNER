# Step 1: Setting Up Your Django Project
# Follow the standard Django project setup process

# Step 2: Define Database Models
# In your app's models.py, define the database models for the URL shortener
from django.db import models

class ShortenedURL(models.Model):
    short_url = models.CharField(max_length=20)
    long_url = models.URLField("URL", unique=True)

# Step 3: Performing Database Migrations
# Run the database migrations to create the ShortenedURL model

# Step 4: Create Forms
# Create a forms.py in your Django app folder to define a form for taking input from the user
from django import forms

class UrlForm(forms.Form):
    url = forms.CharField(label="URL")

# Step 5: Write Views
# Define the views to handle the URL shortening functionality
from django.http import HttpResponse
from .models import ShortenedURL
# Write the view functions to handle URL shortening and redirection

# Step 6: Include URLs
# Include the URL patterns for your app in the main urls.py file
from django.urls import path, include
from . import views

urlpatterns = [
    path('shorten', views.shorten, name='shorten'),
    path('<str:shortened_part>', views.redirect, name='redirect'),
]

# Step 7: Run Your Django Application
# Launch the Django development server and access your URL shortener web application
#These steps provide a high-level overview of the process.In the overalla process we need to build a simple user interface 