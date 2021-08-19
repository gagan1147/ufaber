from django.urls import path
from .views import TaskList,TaskCreate,CustomLogin,Signup
from django.contrib.auth.views import LogoutView


urlpatterns =[
    path('',TaskList.as_view(),name="tasks"),
    path('create-task/',TaskCreate.as_view(),name="task-create"),
    path('login/',CustomLogin.as_view(),name="login"),
    path('logout/',LogoutView.as_view(next_page='login'),name="logout"),
    path('signup/',Signup.as_view(),name='signup')
]