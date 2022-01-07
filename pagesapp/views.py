from django.shortcuts import render
from django.views.generic import TemplateView # templatelarni import qilib chaqirib ishlatish uchun kk buladi

# Create your views here.
class homepageView(TemplateView):  # homepage degan class yaratilib bu funcsiya home.html ni olib qaytaradi
    template_name = 'home.html'

class Aboutniki(TemplateView):  # Aboutniki degan class yaratilib bu funcsiya about.html ni olib qaytaradi
    template_name = 'about.html'
