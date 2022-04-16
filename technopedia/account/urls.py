from django.urls import path
from account import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home/', views.Home.as_view(), name='home'),
    path('login/', views.MyLogin.as_view(), name='loginpage'),
    path('logout/', views.MyLogout.as_view(), name='logout'),
    path('signup/', views.signuphandle, name='signup'),
    path('profile/', views.ProfileTemplateView.as_view(), name='profile'),
    path('contact', views.ContactTemplateView.as_view(), name='contactus'),
    path('detail/<int:pk>', views.UserDetailView.as_view(), name="userdetail"),
    path('password_reset/', auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]
