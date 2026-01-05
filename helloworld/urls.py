from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include(('website.urls', 'website'), namespace='website')),
    path('admin/', admin.site.urls),
]
