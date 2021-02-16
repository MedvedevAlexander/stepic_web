from django.urls import path
from . import views

urlpatterns = [
    path('', views.test, name='main_page'),
    path('login/', views.test, name='login'),
    path('signup/', views.test, name='signup'),
    path('question/<int:quetion_id>/', views.test, name='question'),
    path('ask/', views.test, name='ask'),
    path('popular/', views.test, name='popular'),
    path('new/', views.test, name='new')
]

