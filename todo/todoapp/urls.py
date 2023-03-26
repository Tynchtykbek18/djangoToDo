from django.contrib import admin
from django.urls import path
from todoapp.views import todoappView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todoapp/', todoappView),
]