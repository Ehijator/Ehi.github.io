from django.urls import path
from . import views
from django.conf.urls.static import static



urlpatterns = [
    path('',views.About,name='Landing'),
    path('Experience/',views.Experience,name='Experience'),
    path('Education/',views.Education,name='Education'),
    path('Skills/',views.Skills,name='Skills'),
    path('Projects/',views.Projects,name='Projects'),
    path('Interests/',views.Interests,name='Interests'),
    
]