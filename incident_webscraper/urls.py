
from django.contrib import admin
from django.urls import path, include
from scraper import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('', include('frontend.urls')), 
    path('admin/', admin.site.urls),
    path('scraper/', include('scraper.urls')),
    path('token-auth/', obtain_jwt_token),
    path('accounts/', include('django.contrib.auth.urls'))
] 

