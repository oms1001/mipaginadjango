from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Obra, ObraFecha
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .forms import NewUserForm



# Single slug Sentdex

def single_slug(request, single_slug):
    # first check to see if the url is in categories.

    categories = [c.category_slug for c in ObraFecha.objects.all()]
    if single_slug in categories:
        matching_series = ObraFecha.objects.filter(category_slug=single_slug)
        series_urls = {}

        for m in matching_series.all():
            part_one = Obra.objects.filter(obra_fecha__obra_fecha=m.obra_fecha).earliest("obra_published")
            series_urls[m] = part_one.obra_slug

        return render(request=request,
                      template_name='main/fecha.html',
                      context={"obra_fechas": matching_series, "part_ones": series_urls})
    obras = [o.obra_slug for o in Obra.objects.all()]

    if single_slug in obras:
        this_obra = Obra.objects.get(obra_slug=single_slug)

        return render(request = request,
                      template_name='main/obra.html',
                      context = {"obra":this_obra})



# Create your views here.
def homepage(request):
    return render(request = request,
                  template_name='main/home.html',
                  context = {"fechas":ObraFecha.objects.all})
def header(request):
    return render(request = request,
                  template_name='main/header.html',
                  context = {"fechas":ObraFecha.objects.all})

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form = UserCreationForm(request.POST)
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Nueva cuenta creada: {username}")
            login(request, user)
            return redirect("main:homepage")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request = request,
                        template_name = "main/register.html",
                        context={"form":form})


    form = NewUserForm
    return render(request = request,
                  template_name = "main/register.html",
                  context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Saliste de tu cuenta")
    return redirect("main:homepage")


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "main/login.html",
                    context={"form":form})

                
def construccion(request):
    return render(request = request,
                  template_name='main/construccion_quechua.html',
                  context = {"entradas":Obra.objects.all})


    
