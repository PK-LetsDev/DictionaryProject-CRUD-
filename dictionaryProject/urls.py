from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('dictionary/', include('dictionary.urls')),
    path('admin/', admin.site.urls),
]
