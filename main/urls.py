from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
    path ("", views.homepage, name="homepage"),
    path("register", views.register, name="register"),
    path('tinymce/', include('tinymce.urls')),
    path("logout", views.logout_request, name="logout"),
    path("login", views.login_request, name="login"),
    path("contacto", views.contacto, name="contacto"),
    path("manifiesto", views.manifiesto, name="contacto"),
    path("construccion_quechua", views.construccion, name="construccion"),
    path("<single_slug>", views.single_slug, name="single_slug"),
]
