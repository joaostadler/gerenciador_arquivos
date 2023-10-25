from django.contrib import admin
from django.urls import path
from gerencia_arquivos.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', index),
   # path('', TemplateView.as_view(template_name="index.html")), 
] 
