from django.urls import path
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from . import views

def my_login_view(request):
    response = auth_views.LoginView.as_view()(request)
    if request.user.is_authenticated:
        return redirect('admin:index')
    return response

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/login/', my_login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('search/', views.search, name='search'),
    path('createpost/', views.create_post_view, name='createpost'),
    path('posty/', views.post_list, name='post_list'),
]
