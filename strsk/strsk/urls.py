from django.contrib import admin
from django.conf import settings # new
from django.contrib.auth import views as auth_views
from django.urls import path, include # new
from django.conf.urls.static import static # new
from invitation import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',user_views.home,name='invite-home' ),
    path('def_wish',user_views.def_wish,name='def_wish'),
    path('bday',user_views.bday,name='bday'),
    path('birthday',user_views.birthday,name='birthday'),
    path('home1',user_views.home1,name='home' ),
    path('wish',user_views.wish,name='wish' ),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]

if not settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
