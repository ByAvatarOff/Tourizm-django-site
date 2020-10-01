from django.urls import path
from . import views
from django.contrib.auth import views as authViews


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('login', views.login1, name="login"),
    path('profile', views.profile, name="profile"),
    path('register', views.register, name='register'),
    path('logout', authViews.LogoutView.as_view(next_page='home'), name='logout'),
    path('tours', views.tours, name='tours'),
    path('country', views.country, name='country'),
]
