
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('myauth/', include('app_auth.urls')),
    path('', include('app_advertisiments.urls'))
]

