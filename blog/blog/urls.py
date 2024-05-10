from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('przyklad/', include("user.urls")),
    path('', include('mainapp.urls')),
    path("accounts/", include("django.contrib.auth.urls")),
]
