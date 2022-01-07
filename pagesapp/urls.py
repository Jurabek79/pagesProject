from django.urls import path
from .views import homepageView, Aboutniki  # .views.py ni ichidagi homepageView classli funcsiyani chaqirib ishlatadi

urlpatterns = [
    path('inurl/', homepageView.as_view(), name='home'), # bu urls.py ishlagan payti anashu urlsga kirilsa "homepageView.as_view()" faqat classlar shunday chaqirlidadi
    path('about_url/', Aboutniki.as_view(), name='about')
]

