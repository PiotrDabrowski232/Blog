from django.urls import path, include 
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from . import views
from .views import logout_view

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
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('captcha/', include('captcha.urls')),
    path('post/<int:post_id>/add_comment/', views.add_comment, name='add_comment'),
    path('logout/', logout_view, name='logout'),
    path('search/', views.search, name='search')
]
