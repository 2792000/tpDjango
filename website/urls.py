from django.urls import path

from . import views

#domain.com/website/...
urlpatterns=[
path('',views.home_view, name='home'),
path('a',views.about_view, name='about'),
]