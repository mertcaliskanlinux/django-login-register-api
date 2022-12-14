from django.urls import path,include
from . import views
print("burasi urls")

urlpatterns = [
    path('login',views.LoginView.as_view()),
    path('register',views.RegisterView.as_view()),
    path('refresh',views.RefreshView.as_view()),

]
