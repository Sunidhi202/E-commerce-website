from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as users_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('signup/', users_views.signup, name='signup'),
    path('resetpassword/', users_views.resetpassword, name='resetpassword'),
    #TODO
    # path('phoneNumberVerification/', users_views.phoneNumberVerification, name='phoneNumberVerification'),
    path('login/', users_views.userlogin, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='shop\index.html'), name='logout')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)