from django.urls import path
from django.contrib.auth import views as auth_views
# So 'views.py' does not get mixed up with the line above, we give it an alias with "import as"

from . import views

app_name = "accounts"

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="accounts/logout.html"), name="logout"),
    path("signup/", views.SignUp.as_view(), name='signup'),
]


