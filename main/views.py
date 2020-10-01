from django.shortcuts import render, redirect
from .models import TaskO
from .forms import TaskForm, FilterTours
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def country(request):
    return render(request, 'main/country.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


def login1(request, *args, **kwargs):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            context['error'] = "Логин или пароль неправильные"
    return render(request, 'registration/login.html', context)


def profile(request):
    return render(request, 'registration/profile.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password == password2:
            User.objects.create_user(username, email, password)
            return redirect(reverse("home"))

    return render(request, 'registration/register.html')


def tours(request):
    tasks = TaskO.objects.order_by('-id')
    form = FilterTours(request.POST)
    if form.is_valid():
        if form.cleaned_data["min_price"]:
            tasks = tasks.filter(price__gte=form.cleaned_data["min_price"])

        if form.cleaned_data["max_price"]:
            tasks = tasks.filter(price__lte=form.cleaned_data["max_price"])

        if form.cleaned_data["data"]:
            tasks = tasks.filter(data=form.cleaned_data["data"])

        if form.cleaned_data["country"]:
            tasks = tasks.filter(country=form.cleaned_data["country"])

    return render(request, 'main/tours.html', {'title': 'Главная страница сайта', 'tasks': tasks, 'form': form})

