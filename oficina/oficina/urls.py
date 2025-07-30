from django.contrib import admin
from django.urls import path, include
from gestao.views import custom_logout  # Adicione esta linha


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("gestao.urls")),
    path('accounts/logout/', custom_logout, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')), 
]
