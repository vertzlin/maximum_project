from django.urls import path
from .views import profile_view, login_view, logout_view

urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),

]
