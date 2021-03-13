from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
app_name = 'ask'
urlpatterns = [
    path('', views.index, name='main_page'),
    path('login/', auth_views.LoginView.as_view(template_name='qa/login.html',), name='login'),
    path('signup/', views.signup, name='signup'),
    path('question/<int:question_id>/', views.question, name='question'),
    path('ask/', views.ask, name='ask'),
    path('popular/', views.popular, name='popular'),
    path('new/', views.test, name='new'),
    path('name/', views.get_name, name='name'),
    path('thanks/', views.thanks, name='thanks'),

]

